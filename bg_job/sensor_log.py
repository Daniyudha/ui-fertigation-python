from hardware.Temperature import read_dht_sensor
from hardware.Rain_intensity import rainSensor
from hardware.ph import pHSensor
from hardware.light_flow import light_flowSensor
from hardware.serial_read import SerialReader
from hardware.Pressure import PressureSensor

class Sensor_log:
    def __init__(self):
        self.__dht_sensor = read_dht_sensor()
        self.__rain_sensor = rainSensor()
        self.__ph_sensor = pHSensor()
        self.__light_flow_sensor = light_flowSensor()
        self.__serial_reader = SerialReader()
        self.__pressure_sensor = PressureSensor()

    def update_pressure_sensor(self):
        # Ambil data dari sensor tekanan
        pressure = self.pressure_reader.get_pressure(channel=2)

        # Perbarui label UI
        self.voltage_label.configure(text=f"Voltage: {pressure['voltage']:.2f} V")
        self.adc_label.configure(text=f"ADC: {pressure['adc']}")
        self.pressureValue.configure(text=f"Pressure: {pressure['pressure']:.1f}")

        # Jadwalkan pembaruan berikutnya
        self.root.after(1000, self.update_pressure_sensor)
    
    def update_water_soil(self):
        data = self.water_soil.get_data()

        # water
        ec_air = data.get("EC_Air", "waiting...")
        
        # soil 1
        hum_tanah_1 = data["Soil1"].get("Kelembaban", "waiting...")
        temp_tanah_1 = data["Soil1"].get("Suhu", "waiting...")
        ec_tanah_1 = data["Soil1"].get("Konduktivitas", "waiting...")
        ph_tanah_1 = data["Soil1"].get("pH", "waiting...")
        nitro_1 = data["Soil1"].get("Nitrogen", "waiting...")
        fosfor_1 = data["Soil1"].get("Fosfor", "waiting...")
        kalium_1 = data["Soil1"].get("Kalium", "waiting...")
        
        # soil 2
        hum_tanah_2 = data["Soil1"].get("Kelembaban", "waiting...")
        temp_tanah_2 = data["Soil1"].get("Suhu", "waiting...")
        ec_tanah_2 = data["Soil1"].get("Konduktivitas", "waiting...")
        ph_tanah_2 = data["Soil1"].get("pH", "waiting...")
        nitro_2 = data["Soil1"].get("Nitrogen", "waiting...")
        fosfor_2 = data["Soil1"].get("Fosfor", "waiting...")
        kalium_2 = data["Soil1"].get("Kalium", "waiting...")


        # Perbarui label
        self.waterECValue.configure(text=f"{ec_air}")
        
        # update ui sensor
        self.soilHumValue.configure(text=f"{hum_tanah_1}")
        self.soilECValue.configure(text=f"{ec_tanah_1}")
        self.soilpHValue.configure(text=f"{ph_tanah_1}")

        self.root.after(1000, self.update_water_soil)
        
    def stop_program(self):
        """Hentikan program."""
        self.water_soil.stop_reading()
        self.root.destroy()
        
    
    def update_light_flowSensor(self):
        lux = self.light_flow_reader.last_lux
        # category = self.light_flow_reader.last_light_category
        flow_rates = self.light_flow_reader.flow_rates
        print(flow_rates[0])
        
        self.lightValue.configure(text=f"{lux:.1f}")
        self.flow1Value.configure(text=f"{flow_rates[0]:.1f}")
        self.flow2Value.configure(text=f"{flow_rates[1]:.1f}")
        self.flow3Value.configure(text=f"{flow_rates[2]:.1f}")
        self.flow4Value.configure(text=f"{flow_rates[3]:.1f}")

        self.root.after(1000, self.update_light_flowSensor)
    
    def update_pHSensor(self):
        voltage, ph_value, ph_classification = self.pH_reader.get_ph_data(channel=0)
        self.waterpHValue.configure(text=f"{ph_value:.1f}")
        self.root.after(1000, self.update_pHSensor)

    def update_rainSensor(self):
        voltage, rain_intensity, rain_classification = self.rain_reader.get_rain_data(channel=1)
        # self.voltage_label.configure(text=f"Tegangan: {voltage:.2f} V")
        self.rainValue.configure(text=f"{rain_intensity:.1f}")
        # self.classification_label.configure(text=f"Klasifikasi: {rain_classification}")
        self.root.after(1000, self.update_rainSensor)
    
    def update_temperature(self):
        temperature, humidity = read_dht_sensor()
        if temperature is not None:
            self.tempValue.configure(text=f"{temperature:.1f}")
        else:
            self.tempValue.configure(text="N/A")  # Tampilkan "N/A" jika gagal membaca sensor
            
        if humidity is not None:
            self.humValue.configure(text=f"{humidity:.1f}")
        else:
            self.humValue.configure(text="N/A")

        # Panggil fungsi ini lagi setelah 1000 ms (1 detik)
        self.root.after(1000, self.update_temperature)
    
    def on_closing(self):
        # Hentikan pembacaan sensor sebelum menutup aplikasi
        # self.light_reader.stop_reading()
        self.rainData.close()  # Tutup koneksi SPI saat aplikasi ditutup
        self.destroy()
    
    def run(self):
        while True:
            self.update_lightSensor()
            time.sleep(1)