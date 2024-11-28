import RPi.GPIO as GPIO
import time
import threading
from collections import deque

# Konfigurasi GPIO
LDR_PIN = 16  # Sesuaikan pin GPIO untuk sensor LDR

class lightSensorReader:
    def __init__(self):
        # Inisialisasi deque untuk menyimpan pembacaan
        self.light_readings = deque(maxlen=10)  # Menyimpan 10 pembacaan terakhir
        self.last_lux = 0
        self.last_category = "Unknown"
        self.running = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LDR_PIN, GPIO.IN)

    def read_light_sensor(self):
        return GPIO.input(LDR_PIN)

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

    def start_reading(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.running:
            light_status = self.read_light_sensor()  # Baca status LDR (HIGH atau LOW)

            # Jika sensor mendeteksi cahaya, tambahkan nilai ke deque
            if light_status == GPIO.LOW:  # Cahaya terdeteksi
                self.light_readings.append(1)
            else:  # Gelap
                self.light_readings.append(0)

            # Hitung rata-rata dari pembacaan dalam deque
            average_light = sum(self.light_readings) / len(self.light_readings) if self.light_readings else 0
            
            # Konversi status rata-rata menjadi lux
            lux = average_light * 1000  # Sesuaikan dengan kalibrasi Anda
            self.last_lux = lux
            self.last_category = self.classify_light_intensity(lux)
            
            time.sleep(1)  # Delay antara pembacaan

    def stop_reading(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()
        GPIO.cleanup()

# Contoh Penggunaan Kode Sensor Sajagf
if __name__ == "__main__":
    try:
        light_sensor = lightSensorReader()
        light_sensor.start_reading()
        
        while True:
            print(f"Lux: {light_sensor.last_lux:.2f}, Klasifikasi: {light_sensor.last_category}")
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Program dihentikan")
    
    finally:
        light_sensor.stop_reading()
