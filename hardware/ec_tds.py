import minimalmodbus
import RPi.GPIO as GPIO
import time

# Pengaturan GPIO untuk DE & RE
DE_RE_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(DE_RE_PIN, GPIO.OUT)

# Fungsi untuk atur arah
def set_transmit_mode():
    GPIO.output(DE_RE_PIN, GPIO.HIGH)

def set_receive_mode():
    GPIO.output(DE_RE_PIN, GPIO.LOW)

# Inisialisasi koneksi Modbus
instrument = minimalmodbus.Instrument('/dev/ttyS0', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU

try:
    # Baca data dari register pertama
    set_receive_mode()
    time.sleep(0.5)  # Jeda lebih lama untuk memastikan
    response = instrument.read_register(1, 0)
    print("Data:", response)

except IOError:
    print("Gagal berkomunikasi dengan perangkat.")

finally:
    GPIO.cleanup()
