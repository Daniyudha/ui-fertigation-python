import RPi.GPIO as GPIO
import time

# Setup mode GPIO
GPIO.setmode(GPIO.BOARD)

# Konfigurasi pin untuk sensor dengan pull-up resistor
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sensor hujan
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sensor LDR

def baca_sensor_hujan():
    # Membaca nilai dari pin GPIO untuk sensor hujan
    sensor_value = GPIO.input(37)
    if sensor_value == GPIO.LOW:
        return "Terdeteksi Hujan"
    else:
        return "Tidak Terdeteksi Hujan"

def baca_sensor_ldr():
    # Membaca nilai dari pin GPIO untuk sensor LDR
    ldr_value = GPIO.input(36)
    if ldr_value == GPIO.LOW:
        return "Cahaya Terdeteksi"
    else:
        return "Gelap Terdeteksi"

def main():
    try:
        while True:
            # Membaca sensor hujan dan LDR
            hasil_hujan = baca_sensor_hujan()
            hasil_ldr = baca_sensor_ldr()

            # Menampilkan hasil pembacaan
            print(f"Hujan: {hasil_hujan}")
            print(f"LDR: {hasil_ldr}")

            # Menunggu 1 detik sebelum pembacaan berikutnya
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna")
    finally:
        # Membersihkan konfigurasi GPIO setelah selesai
        GPIO.cleanup()

if __name__ == "__main__":
    main()
