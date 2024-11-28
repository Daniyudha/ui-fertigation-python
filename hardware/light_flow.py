import RPi.GPIO as GPIO
import time
import threading
from collections import deque

# Pin Konfigurasi
LDR_PIN = 16  # Pin GPIO untuk sensor LDR
FLOW_PINS = [6, 12, 21, 27]  # Pin GPIO untuk sensor aliran

class light_flowSensor:
    def __init__(self):
        # Light Sensor
        self.light_readings = deque(maxlen=10)  # Simpan pembacaan terakhir
        self.last_lux = 0
        self.last_light_category = "Unknown"

        # Flow Sensor
        self.flow_readings = [deque(maxlen=5) for _ in FLOW_PINS]
        self.flow_rates = [0] * len(FLOW_PINS)
        
        # Thread Control
        self.running = threading.Event()
        self.running.clear()
        self.lock = threading.Lock()

        # GPIO Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LDR_PIN, GPIO.IN)
        for pin in FLOW_PINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_light_sensor(self):
        return GPIO.input(LDR_PIN) == GPIO.HIGH

    def classify_light_intensity(self, lux):
        if lux <= 1:
            return "Kegelapan Total"
        elif 1 < lux <= 50:
            return "Cahaya Remang-Remang"
        elif 50 < lux <= 200:
            return "Cahaya Kamar"
        elif 200 < lux <= 500:
            return "Cahaya Normal"
        elif 500 < lux <= 1000:
            return "Cahaya Terang"
        else:
            return "Cahaya Sangat Terang"

    def read_flow_sensor(self, sensor_index):
        if GPIO.input(FLOW_PINS[sensor_index]) == GPIO.LOW:
            self.flow_readings[sensor_index].append(1)
        else:
            self.flow_readings[sensor_index].append(0)
        
        # Hitung rata-rata
        average_pulse = sum(self.flow_readings[sensor_index]) / len(self.flow_readings[sensor_index]) if self.flow_readings[sensor_index] else 0
        flow_rate = average_pulse * 1000  # Sesuaikan kalibrasi
        return min(flow_rate, 30.0)  # Batas maksimum 30 LPM

    def sensor_loop(self):
        while self.running.is_set():
            with self.lock:
                # Pembacaan LDR
                light_status = self.read_light_sensor()
                
                # Sesuaikan logika pembacaan jika perlu
                self.light_readings.append(1 if light_status else 0)  # HIGH untuk terang

                # Hitung rata-rata dan kalibrasi
                average_light = sum(self.light_readings) / len(self.light_readings)
                self.last_lux = (1 - average_light) * 1000  # Balik nilai jika diperlukan
                self.last_light_category = self.classify_light_intensity(self.last_lux)

                # Flow Sensors (tidak diubah)
                for i in range(len(FLOW_PINS)):
                    self.flow_rates[i] = self.read_flow_sensor(i)

            time.sleep(0.5)

    def start(self):
        self.running.set()
        self.thread = threading.Thread(target=self.sensor_loop)
        self.thread.start()

    def stop(self):
        self.running.clear()
        if self.thread.is_alive():
            self.thread.join()
        GPIO.cleanup()


# Contoh penggunaan
if __name__ == "__main__":
    try:
        manager = light_flowSensor()
        manager.start()
        while True:
            print(f"Lux: {manager.last_lux:.2f}, Kategori: {manager.last_light_category}")
            for i, rate in enumerate(manager.flow_rates):
                print(f"Flow Sensor {i + 1}: {rate:.2f} LPM")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Program dihentikan.")
    finally:
        manager.stop()
