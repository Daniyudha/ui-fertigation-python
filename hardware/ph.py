import spidev
import time

class pHSensor:
    def __init__(self, spi_bus=0, spi_device=1, v_ref=5.0):
        # Inisialisasi SPI untuk MCP3008
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 1350000
        self.v_ref = v_ref  # Tegangan referensi (misalnya, 5V)

    def read_channel(self, channel):
        """Membaca data dari channel yang ditentukan pada MCP3008."""
        try:
            adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
            return ((adc[1] & 3) << 8) + adc[2]
        except Exception as e:
            print(f"Error membaca channel {channel}: {e}")
            return None

    def convert_to_voltage(self, adc_value):
        """Mengonversi nilai ADC ke tegangan."""
        if adc_value is not None:
            return (adc_value / 1023.0) * self.v_ref
        return 0

    def convert_to_ph(self, voltage):
        """Mengonversi tegangan ke nilai pH."""
        if voltage == 4.2:
            return 7  # Anggap pH netral jika tegangan 4.2V
        return -6 * voltage + 31

    def classify_ph(self, ph_value):
        """Mengklasifikasikan nilai pH sebagai Asam, Netral, atau Basa."""
        if ph_value < 6:
            return "Asam"
        elif 6 <= ph_value <= 7:
            return "Netral"
        else:
            return "Basa"

    def get_ph_data(self, channel=0):
        """Mengambil data pH dan mengembalikan nilai tegangan, pH, dan klasifikasi."""
        adc_value = self.read_channel(channel)
        if adc_value is None:
            print("Gagal membaca data dari MCP3008.")
            return 0.0, 0.0, "Tidak ada data"

        voltage = self.convert_to_voltage(adc_value)
        ph_value = self.convert_to_ph(voltage)
        ph_classification = self.classify_ph(ph_value)

        return voltage, ph_value, ph_classification

    def close(self):
        """Menutup koneksi SPI."""
        self.spi.close()

# Fungsi utama untuk menjalankan pembacaan sensor secara mandiri
def main():
    sensor = pHSensor()
    try:
        while True:
            voltage, ph_value, ph_classification = sensor.get_ph_data(channel=0)

            # Cetak hasil ke terminal
            print(f"Tegangan: {voltage:.1f} V, Nilai pH: {ph_value:.1f} ({ph_classification})")
            time.sleep(1)  # Delay 1 detik sebelum pembacaan berikutnya
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
    finally:
        sensor.close()
        print("Koneksi SPI ditutup.")

if __name__ == "__main__":
    main()
