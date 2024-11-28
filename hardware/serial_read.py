import serial
import threading
import time


class SerialReader:
    def __init__(self, port, baudrate, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.running = True
        self.ser = None
        self.data = {
            "ec_air": None,
            "kelembaban": None,
            "suhu": None,
            "konduktivitas": None,
            "ph": None,
            "nitrogen": None,
            "fosfor": None,
            "kalium": None,
            "salinitas": None,
            "tds": None,
        }
        self.init_serial()

    def init_serial(self):
        """Inisialisasi koneksi serial."""
        try:
            self.ser = serial.Serial(
                self.port, self.baudrate, timeout=self.timeout
            )
            print(f"Serial port {self.port} berhasil dibuka.")
        except serial.SerialException as e:
            print(f"SerialException: {e}. Tidak dapat membuka port {self.port}")
            self.running = False

    def read_data(self):
        """Fungsi untuk membaca data dari serial port secara terus-menerus."""
        while self.running:
            try:
                if self.ser.in_waiting > 0:
                    # Baca data dari serial dan hilangkan whitespace
                    line = self.ser.readline().decode("utf-8").strip()
                    print(f"Data diterima: {line}")  # Debugging

                    # Proses data sesuai format
                    self.process_line(line)

                time.sleep(0.1)

            except serial.SerialException as e:
                print(f"SerialException: {e}. Mencoba memulai ulang...")
                self.restart_serial()
            except OSError as e:
                print(f"OSError: {e}. Mencoba memulai ulang...")
                self.restart_serial()
            except Exception as e:
                print(f"Error tidak terduga: {e}")

    def process_line(self, line):
        """Proses setiap baris data yang diterima."""
        try:
            if line.startswith("EC_Air:"):
                self.data["ec_air"] = int(line.split(":")[1].strip())
            elif line.startswith("Kelembaban:"):
                self.data["kelembaban"] = int(line.split(":")[1].strip())
            elif line.startswith("Suhu:"):
                self.data["suhu"] = float(line.split(":")[1].strip()) / 10.0
            elif line.startswith("Konduktivitas:"):
                self.data["konduktivitas"] = float(line.split(":")[1].strip())
            elif line.startswith("pH:"):
                self.data["ph"] = float(line.split(":")[1].strip()) / 10.0
            elif line.startswith("Nitrogen:"):
                self.data["nitrogen"] = int(line.split(":")[1].strip())
            elif line.startswith("Fosfor:"):
                self.data["fosfor"] = int(line.split(":")[1].strip())
            elif line.startswith("Kalium:"):
                self.data["kalium"] = int(line.split(":")[1].strip())
            elif line.startswith("Salinitas:"):
                self.data["salinitas"] = float(line.split(":")[1].strip())
            elif line.startswith("TDS:"):
                self.data["tds"] = float(line.split(":")[1].strip())
        except (ValueError, IndexError) as e:
            print(f"Error memproses data: {e}. Data: {line}")

    def restart_serial(self):
        """Fungsi untuk mereset koneksi serial."""
        try:
            if self.ser:
                self.ser.close()
            time.sleep(2)
            self.init_serial()
        except Exception as e:
            print(f"Gagal memulai ulang serial port: {e}")
            self.running = False

    def start_reading(self):
        """Mulai thread pembacaan data."""
        self.thread = threading.Thread(target=self.read_data, daemon=True)
        self.thread.start()

    def stop_reading(self):
        """Hentikan thread pembacaan data."""
        self.running = False
        if self.thread.is_alive():
            self.thread.join()
        if self.ser:
            self.ser.close()
        print("Pembacaan data dihentikan.")

    def print_data(self):
        """Cetak data terbaru ke layar."""
        print(
            f"EC Air: {self.data['ec_air']}, "
            f"Kelembaban: {self.data['kelembaban']}, "
            f"Suhu: {self.data['suhu']}, "
            f"Konduktivitas: {self.data['konduktivitas']}, "
            f"pH: {self.data['ph']}, "
            f"Nitrogen: {self.data['nitrogen']}, "
            f"Fosfor: {self.data['fosfor']}, "
            f"Kalium: {self.data['kalium']}, "
            f"Salinitas: {self.data['salinitas']}, "
            f"TDS: {self.data['tds']}"
        )


if __name__ == "__main__":
    try:
        reader = SerialReader(port="/dev/serial0", baudrate=9600)
        if reader.running:
            reader.start_reading()
            print("Membaca data sensor. Tekan Ctrl+C untuk keluar.")
            while reader.running:
                reader.print_data()
                time.sleep(2)
    except KeyboardInterrupt:
        print("Pengguna menghentikan program.")
    finally:
        if reader.running:
            reader.stop_reading()
