import minimalmodbus
import serial
import time

# Konfigurasi perangkat Modbus
device_id = 1           # Device ID
baudrate = 9600         # Baudrate sensor
port = '/dev/ttyS0'     # Port serial pada Raspberry Pi, sesuaikan jika berbeda

# Inisialisasi komunikasi Modbus
try:
    instrument = minimalmodbus.Instrument(port, device_id)
    instrument.serial.baudrate = baudrate
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.stopbits = 2
    instrument.serial.timeout = 2  # Waktu tunggu respons
    print("Inisialisasi Modbus berhasil.")
except Exception as e:
    print(f"Gagal inisialisasi Modbus: {e}")

# Fungsi untuk membaca data dari register
def read_sensor_data():
    try:
        ph = instrument.read_register(6, 1)                # Register 40007
        soil_humidity = instrument.read_register(18, 1)    # Register 40019
        soil_temp = instrument.read_register(19, 1)        # Register 40020
        soil_conductivity = instrument.read_register(21, 1) # Register 40022
        soil_nitrogen = instrument.read_register(30, 1)    # Register 40031
        soil_phosphorus = instrument.read_register(31, 1)  # Register 40032
        soil_potassium = instrument.read_register(32, 1)   # Register 40033

        print(f"pH: {ph * 0.01}")
        print(f"Soil Humidity: {soil_humidity * 0.1} %")
        print(f"Soil Temperature: {soil_temp * 0.1} °C")
        print(f"Soil Conductivity: {soil_conductivity} µS/cm")
        print(f"Soil Nitrogen: {soil_nitrogen} mg/kg")
        print(f"Soil Phosphorus: {soil_phosphorus} mg/kg")
        print(f"Soil Potassium: {soil_potassium} mg/kg")

    except IOError:
        print("Gagal membaca dari sensor.")
    except Exception as e:
        print(f"Error: {e}")

# Loop untuk membaca data
try:
    while True:
        read_sensor_data()
        time.sleep(1)  # Waktu tunggu antara pembacaan
except KeyboardInterrupt:
    print("Program dihentikan.")

--------------------------------------------
import minimalmodbus
import serial
import time
import RPi.GPIO as GPIO

# Konfigurasi perangkat Modbus
device_id = 1          # Device ID
baudrate = 9600        # Baudrate sensor
port = '/dev/ttyS0'    # Port serial pada Raspberry Pi

# Pin GPIO untuk DE dan RE MAX485
DE_PIN = 17
RE_PIN = 27

# Inisialisasi GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DE_PIN, GPIO.OUT)
GPIO.setup(RE_PIN, GPIO.OUT)

try:
    # Inisialisasi komunikasi Modbus
    instrument = minimalmodbus.Instrument(port, device_id)
    instrument.serial.baudrate = baudrate
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.stopbits = 2
    instrument.serial.timeout = 2  # Timeout ditingkatkan untuk memastikan respons

    print("Inisialisasi berhasil.")
except Exception as e:
    print(f"Inisialisasi gagal: {e}")
    exit()

def enable_transmit():
    GPIO.output(DE_PIN, GPIO.HIGH)
    GPIO.output(RE_PIN, GPIO.HIGH)

def enable_receive():
    GPIO.output(DE_PIN, GPIO.LOW)
    GPIO.output(RE_PIN, GPIO.LOW)

def read_sensor_data():
    try:
        enable_receive()
        time.sleep(0.1)  

        # Membaca data sensor dari register sesuai alamat
        ph = instrument.read_register(6, 1)
        soil_humidity = instrument.read_register(18, 1)
        soil_temp = instrument.read_register(19, 1)
        soil_conductivity = instrument.read_register(21, 1)
        soil_nitrogen = instrument.read_register(30, 1)
        soil_phosphorus = instrument.read_register(31, 1)
        soil_potassium = instrument.read_register(32, 1)

        # Konversi dan cetak data
        ph_value = ph * 0.01
        humidity_value = soil_humidity * 0.1
        temp_value = soil_temp * 0.1
        conductivity_value = soil_conductivity
        nitrogen_value = soil_nitrogen
        phosphorus_value = soil_phosphorus
        potassium_value = soil_potassium

        print("Pembacaan data berhasil.")
        print(f"pH: {ph_value}")
        print(f"Soil Humidity: {humidity_value} %")
        print(f"Soil Temperature: {temp_value} °C")
        print(f"Soil Conductivity: {conductivity_value} µS/cm")
        print(f"Soil Nitrogen: {nitrogen_value} mg/kg")
        print(f"Soil Phosphorus: {phosphorus_value} mg/kg")
        print(f"Soil Potassium: {potassium_value} mg/kg")

    except IOError as e:
        print(f"Pembacaan data gagal: {e}. Pastikan konfigurasi Modbus dan koneksi sudah benar.")
    except Exception as e:
        print(f"Kesalahan tak terduga: {e}")

try:
    while True:
        print("Membaca data sensor...")
        read_sensor_data()
        time.sleep(2)
except KeyboardInterrupt:
    print("Program dihentikan")
finally:
    GPIO.cleanup()
