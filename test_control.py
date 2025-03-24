import serial
import time

# Inisialisasi komunikasi serial
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Status awal
status = False

while True:
    if status:
        ser.write(b"5 OFF 7\n")  # Matikan relay
        print("Mengirim: 5 OFF 7")
    else:
        ser.write(b"5 ON 7\n")  # Nyalakan relay
        print("Mengirim: 5 ON 7")
    
    status = not status  # Toggle status
    time.sleep(5)  # Tunggu 1 detik sebelum mengirim lagi
