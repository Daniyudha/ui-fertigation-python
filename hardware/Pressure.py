import spidev
import threading
import logging
import time


class PressureSensor:
    def __init__(self, spi_channel=1, adc_channel=2, max_speed_hz=1350000, v_ref=5.0, max_voltage=5.0, max_pressure=12.0, update_interval=1.0):
        if not (0 <= adc_channel <= 7):
            raise ValueError("Channel ADC harus antara 0-7.")

        self.spi_channel = spi_channel
        self.adc_channel = adc_channel
        self.max_speed_hz = max_speed_hz
        self.v_ref = v_ref
        self.max_voltage = max_voltage
        self.max_pressure = max_pressure
        self.update_interval = update_interval
        self.running = False

        self.current_data = {
            "voltage": 0.0,
            "adc_value": 0,
            "pressure": 0.0
        }

        self.spi = spidev.SpiDev()
        try:
            self.spi.open(0, spi_channel)
            self.spi.max_speed_hz = max_speed_hz
            logging.info(f"SPI diinisialisasi pada channel {spi_channel}.")
        except FileNotFoundError:
            logging.error("SPI device tidak ditemukan. Pastikan SPI diaktifkan.")
            raise
        except Exception as e:
            logging.error(f"Kesalahan saat membuka SPI: {e}")
            raise

    def read_channel(self):
        """Membaca data mentah dari ADC MCP3008."""
        try:
            adc = self.spi.xfer2([1, (8 + self.adc_channel) << 4, 0])
            data = ((adc[1] & 3) << 8) + adc[2]

            # Pastikan data tidak melebihi batas unsigned short (0-1023 untuk MCP3008)
            if data < 0 or data > 1023:
                logging.warning(f"Nilai ADC di luar batas: {data}. Mengembalikan 0.")
                return 0
            return data
        except Exception as e:
            logging.error(f"Gagal membaca channel {self.adc_channel}: {e}")
            return 0

    def convert_volts(self, data):
        """Konversi nilai ADC ke voltase."""
        return (data * self.v_ref) / 1023.0

    def convert_to_pressure(self, voltage):
        """Konversi voltase ke tekanan (bar)."""
        return (voltage / self.max_voltage) * self.max_pressure

    def update_data(self):
        """Memperbarui nilai sensor tekanan."""
        raw_value = self.read_channel()
        voltage = self.convert_volts(raw_value)
        pressure = self.convert_to_pressure(voltage)

        self.current_data = {
            "voltage": voltage,
            "adc_value": raw_value,
            "pressure": pressure
        }

    def start_reading(self):
        """Memulai pembacaan sensor dalam thread terpisah."""
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()
        logging.info("Thread pembacaan sensor tekanan dimulai.")

    def run(self):
        """Loop utama untuk pembacaan tekanan."""
        while self.running:
            try:
                self.update_data()
                time.sleep(self.update_interval)
            except Exception as e:
                logging.error(f"Kesalahan pada loop utama: {e}")
                break

    def stop_reading(self):
        """Menghentikan pembacaan sensor."""
        self.running = False
        logging.info("Thread pembacaan sensor tekanan dihentikan.")

    def get_data(self):
        """Mengembalikan data tekanan terbaru."""
        return self.current_data

    def close(self):
        """Menutup koneksi SPI."""
        self.stop_reading()
        self.spi.close()
        logging.info("Koneksi SPI ditutup.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        sensor = PressureSensor(spi_channel=1, adc_channel=2, v_ref=5.0, max_voltage=4.5, max_pressure=12.0, update_interval=1.0)
        sensor.start_reading()

        while True:
            data = sensor.get_data()
            print(f"Voltage: {data['voltage']:.2f} V")
            print(f"ADC Value: {data['adc_value']}")
            print(f"Pressure: {data['pressure']:.2f} bar")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
    finally:
        sensor.close()
