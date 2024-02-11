import time
from SleepWorker import SleepyWorker
from threading import Thread
from SquareSumWorker import SquareSumWorker


def main():
    current_threads = []
    for i in range(1, 5):
        maximal_value = i * 100000
        square_sum_worker = SquareSumWorker(maximal_value)
        current_threads.append(square_sum_worker)
    for t in current_threads:
        t.join()

    current_threads = []
    for i in range(1, 5):
        sleepy_worker = SleepyWorker(i)
        current_threads.append(sleepy_worker)
    for t in current_threads:
        t.join()
    
    current_threads = []
    for i in range(2):
        t = Thread(target=SleepyWorker(i).sleep_a_bit, args=(i,))
        t.start()
        current_threads.append(t)


if __name__ == "__main__":
    main()
