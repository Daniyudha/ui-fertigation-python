import RPi.GPIO as GPIO
import time
from collections import deque
from threading import Thread, Event


class flowSensor:
    def __init__(self, pins):
        self.pins = pins
        self.pulse_counts = [0] * len(pins)
        self.flow_rate_histories = [deque(maxlen=5) for _ in range(len(pins))]
        self.start_time = time.time()
        self.running = Event()
        self.running.clear()

        self._thread = None
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def count_pulse(self, sensor_index):
        if GPIO.input(self.pins[sensor_index]) == GPIO.LOW:
            self.pulse_counts[sensor_index] += 1
            time.sleep(0.01)

    def get_flow_rate(self, sensor_index):
        elapsed_time = time.time() - self.start_time
        if self.pulse_counts[sensor_index] == 0 or elapsed_time < 0.1:
            flow_rate = 0.0
        else:
            flow_rate = (self.pulse_counts[sensor_index] / 450.0) * (60.0 / elapsed_time)
            flow_rate = min(flow_rate, 30.0)
        self.pulse_counts[sensor_index] = 0
        self.start_time = time.time()
        return flow_rate

    def get_average_flow_rate(self, sensor_index):
        if self.flow_rate_histories[sensor_index]:
            return sum(self.flow_rate_histories[sensor_index]) / len(self.flow_rate_histories[sensor_index])
        return 0.0

    def update_flow_data(self):
        while self.running.is_set():
            for i in range(len(self.pins)):
                self.count_pulse(i)
                flow_rate = self.get_flow_rate(i)
                self.flow_rate_histories[i].append(flow_rate)

            time.sleep(0.1)

    def start(self):
        if not self.running.is_set():
            self.running.set()
            self._thread = Thread(target=self.update_flow_data)
            self._thread.start()

    def stop(self):
        self.running.clear()
        if self._thread is not None:
            self._thread.join()
        GPIO.cleanup()

    def get_sensor_data(self):
        return [
            self.get_average_flow_rate(i)
            for i in range(len(self.pins))
        ]


if __name__ == "__main__":
    try:
        # Contoh penggunaan standalone
        flow_manager = flowSensor(pins=[6, 12, 21, 27])
        flow_manager.start()

        print("Mulai membaca sensor aliran air...")
        while True:
            sensor_data = flow_manager.get_sensor_data()
            for i, flow_rate in enumerate(sensor_data):
                print(f"Sensor {i+1}: {flow_rate:.2f} LPM")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program dihentikan.")

    finally:
        flow_manager.stop()
