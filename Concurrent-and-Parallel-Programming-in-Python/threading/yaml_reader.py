import importlib
import threading
import time

import yaml
from multiprocessing import Queue


class YamlPipelineExecutor(threading.Thread):
    # The constructor takes a pipeline_location parameter, which is the file path of the YAML configuration. 
    # It initializes various dictionaries to keep track of queues, workers, and their relationships.
    def __init__(self, pipeline_location):
        super(YamlPipelineExecutor, self).__init__()
        self._pipline_location = pipeline_location
        self._queues = {}
        self._workers = {}
        self._queue_consumers = {}
        self._downstream_queues = {}

    # This method opens and reads the YAML configuration file using the yaml.safe_load method. 
    def _load_pipeline(self):
        with open(self._pipline_location, 'r') as inFile:
            self._yaml_data = yaml.safe_load(inFile)

    #  Iterates over the queues section of the loaded YAML data. For each queue defined, it creates a Queue object (from the multiprocessing module) and maps the queue's name to this object in the _queues dictionary. 
    # These queues are used for passing messages between different workers.
    def _initialize_queues(self):
        for queue in self._yaml_data['queues']:
            queue_name = queue['name']
            self._queues[queue_name] = Queue()

    def _initialize_workers(self):
        """
        Processes the workers section of the YAML data. For each worker:

        Dynamically loads the worker class using importlib and the specified module path and class name in the YAML.
        Initializes the worker with the appropriate input and output queues, and any input values specified.
        Handles multiple instances of the same worker if specified, creating a list of worker instances for each worker name.
        Maps output queues to workers and keeps track of the number of instances consuming from each input queue.
        """
        for worker in self._yaml_data['workers']:
            # Putting it all together, this line of code dynamically imports a module based on the path provided in worker['location'], 
            # then retrieves a class from that module using the class name provided in worker['class']
            WorkerClass = getattr(importlib.import_module(worker['location']), worker['class'])
            input_queue = worker.get('input_queue')
            output_queues = worker.get('output_queues')
            worker_name = worker['name']
            num_instances = worker.get('instances', 1)

            self._downstream_queues[worker_name] = output_queues
            if input_queue is not None:
                self._queue_consumers[input_queue] = num_instances
            init_params = {
                'input_queue': self._queues[input_queue] if input_queue is not None else None,
                'output_queue': [self._queues[output_queue] for output_queue in output_queues] \
                    if output_queues is not None else None
            }

            input_values = worker.get('input_values')
            if input_values is not None:
                init_params['input_values'] = input_values

            self._workers[worker_name] = []
            for i in range(num_instances):
                self._workers[worker_name].append(WorkerClass(**init_params))

    def _join_workers(self):
        """
        wait until all process finishes
        """
        for worker_name in self._workers:
            for worker_thread in self._workers[worker_name]:
                worker_thread.join()

    def process_pipeline(self):
        """
        This method is the main entry point for setting up and starting the pipeline process. 
        It loads the pipeline configuration, initializes queues, and workers, 
        but does not start the worker threads
        """
        self._load_pipeline()
        print("yaml data\n",self._yaml_data)
        #  This allows for inter-thread communication.
        self._initialize_queues()
        print("Initialized queues:\n", list(self._queues.keys()))
        self._initialize_workers()
        for worker_name, worker_instances in self._workers.items():
            print(f"Worker {worker_name} has {len(worker_instances)} instances initialized.")
        # for the process_pipeline() method in the YamlPipelineExecutor class to wait for all worker threads 
        # to complete before proceeding further. Here's why:
        self._join_workers()

    def log_progress(self):
        active_workers = sum(1 for workers in self._workers.values() for worker in workers if worker.is_alive())
        queue_sizes = {queue_name: queue.qsize() for queue_name, queue in self._queues.items()}
        print(f"Active Workers: {active_workers}, Queue Sizes: {queue_sizes}")

    def run(self):
        self.process_pipeline()

        while True:
            total_workers_alive = 0
            worker_stats = []
            to_del = []
            self.log_progress()
            for worker_name in self._workers:
                total_worker_threads_alive = 0
                for worker_thread in self._workers[worker_name]:
                    if worker_thread.is_alive():
                        total_worker_threads_alive += 1
                total_workers_alive += total_worker_threads_alive
                if total_worker_threads_alive == 0:
                    if self._downstream_queues[worker_name] is not None:
                        for output_queue in self._downstream_queues[worker_name]:
                            number_of_consumers = self._queue_consumers[output_queue]
                            for i in range(number_of_consumers):
                                self._queues[output_queue].put('DONE')

                    to_del.append(worker_name)

                worker_stats.append([worker_name, total_worker_threads_alive])
            print(worker_stats)
            if total_workers_alive == 0:
                break

            queue_stats = []
            for queue in self._queues:
                queue_stats.append([queue, self._queues[queue].qsize()])
            
            print(queue_stats)

            for worker_name in to_del:
                del self._workers[worker_name]

            time.sleep(1)
