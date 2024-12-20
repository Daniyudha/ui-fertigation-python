import serial
import threading
import logging
from time import sleep

# Konfigurasi logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SerialReader:
    def __init__(self, port="/dev/serial0", baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.data = {
            "EC_Air": 0.0,
            "Soil1": {
                "Kelembaban": 0.0,
                "Suhu": 0.0,
                "Konduktivitas": 0.0,
                "pH": 0.0,
                "Nitrogen": 0.0,
                "Fosfor": 0.0,
                "Kalium": 0.0,
            },
            "Soil2": {
                "Kelembaban": 0.0,
                "Suhu": 0.0,
                "Konduktivitas": 0.0,
                "pH": 0.0,
                "Nitrogen": 0.0,
                "Fosfor": 0.0,
                "Kalium": 0.0,
            }
        }

    def connect(self):
        """Mencoba menyambungkan serial."""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            logging.info(f"Serial port {self.port} dibuka.")
        except serial.SerialException as e:
            logging.error(f"Gagal membuka serial port {self.port}: {e}")
            raise

    def disconnect(self):
        """Menutup koneksi serial jika ada."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            logging.info("Serial port ditutup.")

    def read_line(self):
        """Membaca satu baris data dari serial."""
        try:
            if self.serial_conn.in_waiting > 0:
                return self.serial_conn.readline().decode("utf-8").strip()
        except serial.SerialException as e:
            logging.error(f"Error membaca data: {e}")
            raise
        return None

    def parse_data(self, line):
        """Memetakan data dari string ke struktur dictionary."""
        try:
            if line.startswith("EC_Air:"):
                self.data["EC_Air"] = float(int(line.split(":")[1]) / 10)
            elif line.startswith("Soil1_"):
                key, value = line.replace("Soil1_", "").split(":")
                self.data["Soil1"][key] = float(int(value) / 10)
            elif line.startswith("Soil2_"):
                key, value = line.replace("Soil2_", "").split(":")
                self.data["Soil2"][key] = float(int(value) / 10)
        except Exception as e:
            logging.error(f"Gagal memproses data '{line}': {e}")

    def run(self):
        """Loop utama untuk membaca data secara terus-menerus."""
        if not self.serial_conn:
            logging.error("Serial belum terhubung. Hubungkan dahulu.")
            return

        while True:
            try:
                line = self.read_line()
                if line:
                    logging.debug(f"Data diterima: {line}")
                    self.parse_data(line)
                    self.log_current_data()
            except serial.SerialException:
                logging.error("Koneksi serial terputus. Mencoba menyambungkan ulang...")
                self.disconnect()
                sleep(1)
                self.connect()
            except Exception as e:
                logging.error(f"Kesalahan pada loop utama: {e}")
                break

    def log_current_data(self):
        """Mencetak data terbaru ke log."""
        logging.info(
            f"EC Air: {self.data['EC_Air']}, "
            f"Soil 1: {self.data['Soil1']}, "
            f"Soil 2: {self.data['Soil2']}"
        )

    def get_data(self):
        """Mengembalikan data untuk dipakai di UI."""
        return self.data

    def start_reading(self):
        """Memulai pembacaan data di thread terpisah."""
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

# Main program untuk testing
if __name__ == "__main__":
    reader = SerialReader(port="/dev/serial0", baudrate=9600, timeout=1)
    try:
        reader.connect()
        reader.start_reading()
        while True:
            sleep(1)
            logging.info(f"Data saat ini: {reader.get_data()}")
    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")
    finally:
        reader.disconnect()
