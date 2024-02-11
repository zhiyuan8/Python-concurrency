import time
import threading

# computation heavy function
def calculate_squares(n):
    print(f"Starting {threading.current_thread().name}")
    sum_squares = 0
    for i in range(n):
        sum_squares += i * i
    print(f"{threading.current_thread().name} finished: Sum of squares is {sum_squares}")

# I/O heavy function
def sleep_a_bit(i):
    print(f"Starting {threading.current_thread().name}")
    time.sleep(i)
    print(f"{threading.current_thread().name} finished: Slept for {i} seconds")

def main():
    start_time = time.time()
    current_thread_list = []
    print(f"Main thread: {threading.current_thread().name}")
    
    for i in range(1, 5):
        maximal_value = i * 100000
        t = threading.Thread(target=calculate_squares, args=(maximal_value,), name=f"CalcThread-{i}")
        t.start()
        current_thread_list.append(t)
    
    for t in current_thread_list:
        t.join()
    
    print(f"Time taken for 1st process: {time.time() - start_time}")
    
    start_time = time.time()
    current_thread_list = []
    for i in range(1, 5):
        t = threading.Thread(target=sleep_a_bit, args=(i,), name=f"SleepThread-{i}")
        t.start()
        current_thread_list.append(t)
    
    for t in current_thread_list:
        t.join()

    print(f"Time taken for 2nd process: {time.time() - start_time}")

if __name__ == "__main__":
    main()
