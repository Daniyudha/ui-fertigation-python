import spidev
import time

class rainSensor:
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

    def convert_voltage_to_rain_intensity(self, voltage):
        """Mengonversi tegangan ke intensitas hujan."""
        return (1 - (voltage / self.v_ref)) * 100.0  # dalam mm

    def classify_rain(self, intensity):
        """Mengklasifikasikan intensitas hujan berdasarkan intensitasnya."""
        if intensity <= 2.5:
            return "Hujan Ringan"
        elif intensity <= 7.6:
            return "Hujan Sedang"
        elif intensity <= 50:
            return "Hujan Lebat"
        else:
            return "Hujan Sangat Lebat"

    def get_rain_data(self, channel=1):
        """Mengambil data intensitas hujan dan mengembalikan nilai tegangan, intensitas, dan klasifikasi."""
        adc_value = self.read_channel(channel)
        if adc_value is None:
            print("Gagal membaca data dari MCP3008.")
            return 0.0, 0.0, "Tidak ada data"

        voltage = self.convert_to_voltage(adc_value)
        rain_intensity = self.convert_voltage_to_rain_intensity(voltage)
        rain_classification = self.classify_rain(rain_intensity)

        return voltage, rain_intensity, rain_classification

    def close(self):
        """Menutup koneksi SPI."""
        self.spi.close()

# Fungsi utama untuk menjalankan pembacaan sensor secara mandiri
def main():
    rainData = rainSensor()
    try:
        while True:
            voltage, rain_intensity, rain_classification = rainData.get_rain_data(channel=1)

            # Cetak hasil ke terminal
            print(f"Tegangan: {voltage:.2f} V, Intensitas Hujan: {rain_intensity:.2f} mm, Klasifikasi: {rain_classification}")
            time.sleep(1)  # Delay 1 detik sebelum pembacaan berikutnya
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
    finally:
        rainData.close()
        print("Koneksi SPI ditutup.")

if __name__ == "__main__":
    main()
