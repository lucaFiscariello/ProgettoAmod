import time


class ChronoMeter():
    # properties
    start_time = 0
    end_time = 0

    def start_chrono(self):
        self.start_time = self.current_milli_time()

    def stop_chrono(self):
        self.end_time = self.current_milli_time()

    def get_execution_time(self):
        return self.end_time - self.start_time

    def print_time(self):
        print(f"execution time: {self.get_execution_time()} ms")

    def current_milli_time(self):
        return round(time.time() * 1000)
