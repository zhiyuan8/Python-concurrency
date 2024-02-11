import threading


class SquareSumWorker(threading.Thread):
    def __init__(self, n):
        self.n = n
        super().__init__()
        self.start()

    def calculate_squares(self, n):
        print(f"Starting {threading.current_thread().name}")
        sum_squares = 0
        for i in range(n):
            sum_squares += i * i
        print(
            f"{threading.current_thread().name} finished: Sum of squares is {sum_squares}"
        )

    def run(self):
        self.calculate_squares(self.n)
