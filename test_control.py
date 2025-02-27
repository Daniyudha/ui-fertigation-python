import serial
import time

# Konfigurasi serial
SERIAL_PORT = '/dev/serial0+87'  # Gunakan /dev/serial0 untuk UART GPIO
BAUD_RATE = 9600

# Inisialisasi koneksi serial
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Terhubung ke {SERIAL_PORT} dengan baud rate {BAUD_RATE}")
except serial.SerialException as e:
    print(f"Gagal terhubung ke serial: {e}")
    exit()

# Fungsi untuk mengirim perintah ke ESP32
def kontrol_relay(device_id, relay_address, state):
    command = f"RELAY:{device_id}:{relay_address}:{'ON' if state else 'OFF'}\n"
    ser.write(command.encode())
    print(f"Mengirim perintah: {command.strip()}")

# Contoh penggunaan
try:
    while True:
        kontrol_relay(5, 0x0007, True)  # Nyalakan relay
        time.sleep(2)  # Delay 2 detik
        kontrol_relay(5, 0x0007, False)  # Matikan relay
        time.sleep(2)  # Delay 2 detik
except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna")
finally:
    ser.close()  # Tutup koneksi serial
    print("Koneksi serial ditutup")