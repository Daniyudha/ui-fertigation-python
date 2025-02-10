import time
import threading
from database.connection.db_connection import Db_connection
from tkinter import messagebox
from utils.log import log
from hardware.Temperature import read_dht_sensor
from hardware.Rain_intensity import rainSensor
from hardware.ph import pHSensor
from hardware.light_flow import light_flowSensor
from hardware.serial_read import SerialReader
from hardware.Pressure import PressureSensor

class DbSensor(Db_connection):
    def __init__(self):
        super().__init__()
        # self.db_connected()
        if self.db_connected():
            log().info("Koneksi ke database berhasil.")
        else:
            log().error("Gagal terhubung ke database.")
        
        # Inisialisasi Sensor
        self.rain_reader = rainSensor()
        self.pH_reader = pHSensor()
        self.pressure_reader = PressureSensor()
        self.light_flow_reader = light_flowSensor()
        self.light_flow_reader.start()
        
        self.water_soil = SerialReader(port="/dev/serial0", baudrate=9600)
        self.water_soil.connect()
        self.water_soil.start_reading()
        
        self.sensor_data = {}  # Buffer untuk menyimpan data terbaru
        self.update_sensors()
        self.start_saving_data()
    
    def update_sensors(self):
        try:
            temperature, humidity = read_dht_sensor()
            if temperature is None or humidity is None:
                log().warning("DHT Sensor gagal dibaca, menggunakan data terakhir.")

            rain_intensity = self.rain_reader.get_rain_data(channel=1)[1]
            water_ph = self.pH_reader.get_ph_data(channel=0)[1]
            pressure_data = self.pressure_reader.get_data()
            pressure = pressure_data.get("pressure", None)  

            light_flow_rates = self.light_flow_reader.flow_rates
            soil_data = self.water_soil.get_data()

            soil_1 = soil_data.get("Soil1", {})
            soil_2 = soil_data.get("Soil2", {})

            self.sensor_data = {
                "air_temp": temperature if temperature else self.sensor_data.get("air_temp", None),
                "air_hum": humidity if humidity else self.sensor_data.get("air_hum", None),
                "rain_int": rain_intensity, "water_ph": water_ph,
                "flow_1": light_flow_rates[0], "flow_2": light_flow_rates[1],
                "flow_3": light_flow_rates[2], "flow_4": light_flow_rates[3],
                "soil_1_hum": soil_1.get("Kelembaban", None), "soil_1_temp": soil_1.get("Suhu", None),
                "soil_1_ec": soil_1.get("Konduktivitas", None), "soil_1_ph": soil_1.get("pH", None),
                "soil_1_nitro": soil_1.get("Nitrogen", None), "soil_1_fosfor": soil_1.get("Fosfor", None),
                "soil_1_kalium": soil_1.get("Kalium", None),
                "soil_2_hum": soil_2.get("Kelembaban", None), "soil_2_temp": soil_2.get("Suhu", None),
                "soil_2_ec": soil_2.get("Konduktivitas", None), "soil_2_ph": soil_2.get("pH", None),
                "soil_2_nitro": soil_2.get("Nitrogen", None), "soil_2_fosfor": soil_2.get("Fosfor", None),
                "soil_2_kalium": soil_2.get("Kalium", None),
            }
            
            log().info("Sensor data diperbarui.")
        
        except Exception as e:
            log().error(f"Error saat memperbarui sensor: {e}")

        # Jadwalkan pembaruan berikutnya
        threading.Timer(1, self.update_sensors).start()
    
    def start_saving_data(self):
        def save_loop():
            while True:
                self.save_sensor_data(self.sensor_data)
                time.sleep(5)  # Simpan setiap 5 detik
                
        threading.Thread(target=save_loop, daemon=True).start()
    
    def save_sensor_data(self, data: dict):
        try:
            if not self.mysql_connection.is_connected():
                self.db_connected()
            
            self.cursor = self.mysql_connection.cursor()
            insert_query = """
            INSERT INTO sensors (
                air_temp, air_hum, rain_int, water_ph,
                flow_1, flow_2, flow_3, flow_4,
                soil_1_hum, soil_1_temp, soil_1_ec, soil_1_ph,
                soil_1_nitro, soil_1_fosfor, soil_1_kalium, soil_2_hum, soil_2_temp,
                soil_2_ec, soil_2_ph, soil_2_nitro, soil_2_fosfor, soil_2_kalium
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(data.get(k, None) for k in data.keys())
            print("QUERY:", insert_query)
            print("VALUES:", values)
            self.cursor.execute(insert_query, values)
            self.mysql_connection.commit()
            log().info("Data sensor berhasil disimpan ke database.")

        except Exception as error:
            log().error(f"Error saat menyimpan data: {error}")
            messagebox.showerror(title="Database Error", message=f"Error: {error}")

if __name__ == "__main__":
    try:
        db_sensor = DbSensor()
    except KeyboardInterrupt:
        print("Program dihentikan oleh user. Membersihkan thread...")
        exit(0)

