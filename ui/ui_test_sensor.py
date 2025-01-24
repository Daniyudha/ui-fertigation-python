from database.connection.db_connection import Db_connection
from tkinter import messagebox
from utils.log import log
from ui.ui_home import Ui_home

class DbSensor(Db_connection):
    def __init__(self):
        super().__init__()
        self.db_connected()

    def save_sensor_data(self, data: dict):
        """
        Menyimpan data sensor ke tabel `sensors`.
        
        Args:
            data (dict): Data sensor dengan struktur sebagai berikut:
                {
                    "air_temp": float,
                    "air_hum": float,
                    "light_int": float,
                    "rain_int": float,
                    "flow_1": float,
                    "flow_2": float,
                    "flow_3": float,
                    "flow_4": float,
                    "water_ph": float,
                    "water_ec": float,
                    "soil_1_hum": float,
                    "soil_1_temp": float,
                    "soil_1_ec": float,
                    "soil_1_ph": float,
                    "soil_1_nitro": float,
                    "soil_1_fosfor": float,
                    "soil_1_kalium": float,
                    "soil_2_hum": float,
                    "soil_2_temp": float,
                    "soil_2_ec": float,
                    "soil_2_ph": float,
                    "soil_2_nitro": float,
                    "soil_2_fosfor": float,
                    "soil_2_kalium": float,
                }
        """
        try:
            # Query untuk menyimpan data sensor
            insert_query = """
            INSERT INTO sensors (
                air_temp, air_hum, light_int, rain_int, 
                flow_1, flow_2, flow_3, flow_4, 
                water_ph, water_ec,
                soil_1_hum, soil_1_temp, soil_1_ec, soil_1_ph, soil_1_nitro, soil_1_fosfor, soil_1_kalium,
                soil_2_hum, soil_2_temp, soil_2_ec, soil_2_ph, soil_2_nitro, soil_2_fosfor, soil_2_kalium
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Data yang akan dimasukkan
            # values = (
            #     data.get("air_temp"), data.get("air_hum"), data.get("light_int"), data.get("rain_int"),
            #     data.get("flow_1"), data.get("flow_2"), data.get("flow_3"), data.get("flow_4"),
            #     data.get("water_ph"), data.get("water_ec"),
            #     data.get("soil_1_hum"), data.get("soil_1_temp"), data.get("soil_1_ec"), data.get("soil_1_ph"),
            #     data.get("soil_1_nitro"), data.get("soil_1_fosfor"), data.get("soil_1_kalium"),
            #     data.get("soil_2_hum"), data.get("soil_2_temp"), data.get("soil_2_ec"), data.get("soil_2_ph"),
            #     data.get("soil_2_nitro"), data.get("soil_2_fosfor"), data.get("soil_2_kalium"),
            # )
            
            values = (
                data.get("temperature"), data.get("humidity"), data.get("lux"), data.get("rain_intensity"),
                data.get("flow_rates[0]"), data.get("flow_rates[1]"), data.get("flow_rates[2]"), data.get("flow_rates[3]"),
                data.get("water_ph"), data.get("ec_air"),
                data.get("hum_tanah_1"), data.get("temp_tanah_1"), data.get("ec_tanah_1"), data.get("ph_tanah_1"),
                data.get("nitro_1"), data.get("fosfor_1"), data.get("kalium_1"),
                data.get("hum_tanah_2"), data.get("temp_tanah_2"), data.get("ec_tanah_2"), data.get("ph_tanah_2"),
                data.get("nitro_2"), data.get("fosfor_2"), data.get("kalium_2"),
            )

            # Eksekusi query
            self.cursor.execute(insert_query, values)
            self.mysql_connection.commit()

        except Exception as error:
            # Menampilkan pesan error
            messagebox.showerror(title="Database Error", message=f"Error: {error}")
        else:
            # Logging keberhasilan
            log().info('berhasil menyimpan data sensor ke database')
        finally:
            # Menutup koneksi
            self.cursor.close()
            self.mysql_connection.close()

# if __name__ == "__main__":
#     # Data dummy untuk pengujian
#     dummy_data = {
#         "air_temp": 25.5,
#         "air_hum": 60.2,
#         "light_int": 450.0,
#         "rain_int": 0.0,
#         "flow_1": 1.2,
#         "flow_2": 1.1,
#         "flow_3": 0.9,
#         "flow_4": 1.3,
#         "water_ph": 6.8,
#         "water_ec": 1.5,
#         "soil_1_hum": 25.0,
#         "soil_1_temp": 24.5,
#         "soil_1_ec": 0.8,
#         "soil_1_ph": 6.5,
#         "soil_1_nitro": 50.0,
#         "soil_1_fosfor": 30.0,
#         "soil_1_kalium": 40.0,
#         "soil_2_hum": 22.5,
#         "soil_2_temp": 23.8,
#         "soil_2_ec": 0.7,
#         "soil_2_ph": 6.4,
#         "soil_2_nitro": 48.0,
#         "soil_2_fosfor": 28.0,
#         "soil_2_kalium": 35.0,
#     }

#     # Nama pengguna

#     # Inisialisasi kelas DbSensor
#     sensor_db = DbSensor()

#     # Menyimpan data dummy ke database
#     sensor_db.save_sensor_data(dummy_data)

#     print("Data dummy berhasil disimpan (jika tidak ada error).")
