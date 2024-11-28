import adafruit_dht
import board
import time
import RPi.GPIO as GPIO  # Impor pustaka GPIO

GPIO.cleanup()
# Inisialisasi DHT11 pada pin D13
dht_device = adafruit_dht.DHT11(board.D17) #pin fisik 13

def read_dht_sensor():
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if temperature is not None and humidity is not None:
            # print("Pembacaan sensor DHT berhasil")
            return temperature, humidity
        else:
            print("Hasil tidak valid")
            return None, None
    except RuntimeError as e:
        print(f"Kesalahan saat membaca sensor: {e}")
        return None, None
    except Exception as e:
        print(f"Kesalahan lain: {e}")
        return None, None

def main():
    try:
        while True:
            temperature, humidity = read_dht_sensor()
            if temperature is not None and humidity is not None:
                print(f"temperature: {temperature:.1f} °C")
                print(f"Kelembapan: {humidity:.1f} %")
            else:
                print("Gagal mendapatkan pembacaan. Coba lagi!")

            time.sleep(0.1)  # Tunggu 3 detik sebelum pembacaan berikutnya
    except KeyboardInterrupt:
        print("Program dihentikan")
    finally:
        GPIO.cleanup()  # Bersihkan GPIO saat keluar

if __name__ == "__main__":
    main()