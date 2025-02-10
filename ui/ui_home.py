import customtkinter,time
from utils.clear_frame import clear_frame
from PIL import Image
from database.connection.db_connection import Db_connection
from database.db_preset import Db_preset
# from hardware.light_intensity import lightSensorReader
from hardware.Temperature import read_dht_sensor
from hardware.Rain_intensity import rainSensor
from hardware.ph import pHSensor
# from hardware.water_flow import flowSensor
from hardware.light_flow import light_flowSensor
from hardware.serial_read import SerialReader
from hardware.Pressure import PressureSensor
import threading

class Ui_home:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        # self.root.unbind("<Return>")
        
        
        # Inisialisasi Sensor Reader     
        # self.light_reader = lightSensorReader()
        # self.light_reader.start_reading()
        self.rain_reader = rainSensor()
        self.pH_reader = pHSensor()
        self.pressure_reader = PressureSensor()
        # self.flow_reader = flowSensor(pins=[6, 12, 21, 27])
        self.light_flow_reader = light_flowSensor()
        self.light_flow_reader.start()
        
        self.water_soil = SerialReader(port="/dev/serial0", baudrate=9600)
        self.water_soil.connect()
        self.water_soil.start_reading()
        
        clear_frame(self.square_frame)
        self.ui_images()
        self.ui_widgets()
        self.manual_frame.place_forget()
        
        # self.update_lightSensor()
        self.update_temperature()
        self.update_rainSensor()
        self.update_pHSensor()
        self.update_light_flowSensor()
        self.update_water_soil()
        self.update_pressure_sensor()
        # self.update_flowSensor()
        # self.run()
        
    def update_pressure_sensor(self):
        # Ambil data dari sensor `tekanan`
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

        # Jadwalkan pembaruan berikutnya
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
        # self.category_label.configure(text=category)
        # self.flow1Value.configure(text=f"s{flow_rates:.1f}")
        # for i, rate in enumerate(flow_rates):
        #         print(f"Flow Sensor {i + 1}: {rate:.2f} LPM")
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
        
    # def update_lightSensor(self):
    #     light_value = self.light_reader.last_lux  
    #     self.lightData.configure(text=f"{light_value:.1f}")  # Perbarui label dengan nilai lux
    #     # print(f"Lux: {light_value:.2f}")
        
    #     # Panggil ulang fungsi ini setiap 1000 ms (1 detik)
    #     self.root.after(1000, self.update_lightSensor)
    
    def on_closing(self):
        # Hentikan pembacaan sensor sebelum menutup aplikasi
        # self.light_reader.stop_reading()
        self.rainData.close()  # Tutup koneksi SPI saat aplikasi ditutup
        self.destroy()
    
    def run(self):
        while True:
            self.update_lightSensor()
            time.sleep(1)

    def ui_images(self):
        # https://pixabay.com/vectors/it-business-icons-computers-722950/
        self.water_image = Image.open("images/home_images/water.png")
        self.water_image = customtkinter.CTkImage(dark_image=self.water_image,
                                                    light_image=self.water_image, 
                                                    size=(80, 107))
        
        self.soil_image = Image.open("images/home_images/soil.png")
        self.soil_image = customtkinter.CTkImage(dark_image=self.soil_image,
                                                    light_image=self.soil_image, 
                                                    size=(80, 107))
        
        self.categorypil_image = Image.open("images/home_images/category.png")
        self.category_image = customtkinter.CTkImage(dark_image=self.categorypil_image,
                                                        light_image=self.categorypil_image, 
                                                        size=(58, 58))
        
        self.productpil_image = Image.open("images/home_images/product.png")
        self.product_image = customtkinter.CTkImage(dark_image=self.productpil_image,
                                                    light_image=self.productpil_image, 
                                                    size=(58, 58))
        
        self.waiterpil_image = Image.open("images/home_images/waiter.png")
        self.waiter_image = customtkinter.CTkImage(dark_image=self.waiterpil_image,
                                                    light_image=self.waiterpil_image, 
                                                    size=(58, 58))
        
        self.tablepil_image = Image.open("images/home_images/table.png")
        self.table_image = customtkinter.CTkImage(dark_image=self.tablepil_image,
                                                    light_image=self.tablepil_image, 
                                                    size=(58, 58))
        
        self.off_btn = Image.open("images/home_images/off-btn.png")
        self.off_btn = customtkinter.CTkImage(dark_image=self.off_btn,
                                                light_image=self.off_btn,
                                                size=(60, 60))
        
        self.on_btn = Image.open("images/home_images/on-btn.png")
        self.on_btn = customtkinter.CTkImage(dark_image=self.on_btn,
                                                light_image=self.on_btn,
                                                size=(60, 60))
        
        self.ceklis = Image.open("images/home_images/ceklis.png")
        self.ceklis = customtkinter.CTkImage(dark_image=self.ceklis,
                                                light_image=self.ceklis,
                                                size=(10.94, 8.38))

    def ui_widgets(self):
        # self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
        #                                            width=1678, height=50,
        #                                            corner_radius=0)
        # self.topbar_frame.place(x=0, y=0)
        # self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
        #                                            font=("arial black", 25),
        #                                            text_color="#ffffff", 
        #                                            text="Home")
        # self.topbar_label.place(x=20, y=5)

#################################################################################

        # table_info = Db_table(self.__username).read_table()
        # table_unoccupied = table_occupied = 0
        # for i in table_info:
        #     if i[1]:
        #         table_occupied += 1
        #     else:
        #         table_unoccupied += 1

#################################################################################

        #============================================ Start Water Frame ============================================
        self.water_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=250, height=189,
                                                corner_radius=15,
                                                fg_color="#006495")
        self.water_frame.place(x=14, y=0)

        self.waterimage_label = customtkinter.CTkLabel(master=self.water_frame, text=None, image=self.water_image)
        self.waterimage_label.place(x=20, y=41)

        # ===== EC =====
        self.water_frame_text1 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="EC", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text1.place(x=108, y=35)

        self.waterECValue = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.waterECValue.place(x=140, y=33)

        self.water_frame_label1 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.water_frame_label1.place(x=190, y=30)
        
        # ===== PH =====
        self.water_frame_text2 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="PH", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text2.place(x=108, y=82)

        self.waterpHValue = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.waterpHValue.place(x=140, y=81)

        
        # ===== PRESSURE =====
        self.water_frame_text3 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="Pressure", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text3.place(x=108, y=127)

        self.pressureValue = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.pressureValue.place(x=165, y=126)

        self.water_frame_label3 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="bar", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.water_frame_label3.place(x=200, y=123)
        #============================================ End Water Frame ============================================

        #============================================ Start Soil Frame ============================================
        self.soil_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=250, height=189,
                                                corner_radius=15,
                                                fg_color="#B17E5B")
        self.soil_frame.place(x=284, y=0)

        self.soilimage_label = customtkinter.CTkLabel(master=self.soil_frame, text=None, image=self.soil_image)
        self.soilimage_label.place(x=20, y=41)

        # ===== EC =====
        self.soil_frame_text1 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="EC", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text1.place(x=108, y=35)

        self.soilECValue = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soilECValue.place(x=148, y=33)

        self.soil_frame_label1 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.soil_frame_label1.place(x=190, y=30)
        
        # ===== PH =====
        self.soil_frame_text2 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="PH", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text2.place(x=108, y=82)

        self.soilpHValue = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soilpHValue.place(x=148, y=81)

        
        # ===== HUMIDITY =====
        self.soil_frame_text3 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="Moisture", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text3.place(x=108, y=127)

        self.soilHumValue = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soilHumValue.place(x=165, y=126)

        self.soil_frame_label3 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="%", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.soil_frame_label3.place(x=210, y=123)
        #============================================ End Soil Frame ============================================

        #============================================ Start Flow Frame ============================================
        self.flow_frame = customtkinter.CTkFrame(master=self.square_frame,
                                            width=248.5, height=266,
                                            corner_radius=10, fg_color="#ffffff")
        self.flow_frame.place(x=14, y=212)

        # ====== Title =====
        self.flow_frame_title = customtkinter.CTkLabel(master=self.flow_frame, text="Flow Meter Reader",
                                                       font=("Poppins", 12, "bold"), text_color="#006495")
        self.flow_frame_title.place(x=52, y=16)
        
        # ====== Channel A =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel A",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=63)

        self.flow1Value = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.flow1Value.place(x=146, y=60)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="LPM",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=58)
        
        # ====== Channel B =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel B",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=113)

        self.flow2Value = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.flow2Value.place(x=146, y=111)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="LPM",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=109)
        
        # ====== Channel C =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel C",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=164)

        self.flow3Value = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.flow3Value.place(x=146, y=163)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="LPM",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=161)
        
        # ====== Channel D =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel D",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=216)

        self.flow4Value = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.flow4Value.place(x=146, y=215)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="LPM",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=213)
        #============================================ End Flow Frame ============================================
        
        #============================================ Start Weather Frame ============================================
        self.weather_frame = customtkinter.CTkFrame(master=self.square_frame,
                                            width=248.5, height=266,
                                            corner_radius=10, fg_color="#ffffff")
        self.weather_frame.place(x=285.5, y=212)

        # ====== Title =====
        self.weather_frame_title = customtkinter.CTkLabel(master=self.weather_frame, text="Weather Information",
                                                       font=("Poppins", 12, "bold"), text_color="#006495")
        self.weather_frame_title.place(x=50, y=16)
        
        # ====== Rain =====
        self.text1 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Rain Intensity",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=63)

        self.rainValue = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495", justify="right")
        self.rainValue.place(x=120, y=60)

        self.label1 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="mm",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=58)
        
        # ====== Light =====
        self.text2 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Light Intensity",
                                            font=("Poppins", 10), text_color="#006495")
        self.text2.place(x=35, y=113)

        self.lightValue = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0", 
                                            font=("Poppins", 16, "bold"), text_color="#006495", justify="center")
        self.lightValue.place(x=120, y=111)

        self.label2 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="lux",
                                                font=("Poppins", 10), text_color="#006495")
        self.label2.place(x=186, y=109)
        
        # ====== Temperature =====
        self.text3 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Temperature",
                                            font=("Poppins", 10), text_color="#006495")
        self.text3.place(x=35, y=164)

        self.tempValue = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495", justify="center")
        self.tempValue.place(x=120, y=163)

        self.label3 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="C",
                                                font=("Poppins", 10), text_color="#006495")
        self.label3.place(x=186, y=161)
        
        # ====== Humidity =====
        self.text4 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Humidity",
                                            font=("Poppins", 10), text_color="#006495")
        self.text4.place(x=35, y=216)

        self.humValue = customtkinter.CTkLabel(master=self.weather_frame,
                                            text= "0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.humValue.place(x=120, y=215)

        self.label4 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="%",
                                                font=("Poppins", 10), text_color="#006495")
        self.label4.place(x=186, y=213)
        #============================================ End Weather Frame ============================================
        
        #============================================ Start Input Frame ============================================
        self.input = customtkinter.CTkFrame(master=self.square_frame,
                                            width=351, height=371,
                                            corner_radius=10, fg_color="#ffffff")
        self.input.place(x=556, y=0)
        
        self.input_title = customtkinter.CTkLabel(master=self.input, text="Input Value",
                                                  text_color="#006495", font=("Poppins", 12, "bold"))
        self.input_title.place(x=30, y=17)
        
        # ===== Switch =====
        self.button_label = customtkinter.CTkLabel(master=self.input, text="Manual",
                                                  text_color="#006495", font=("Poppins", 12))
        self.button_label.place(x=211, y=17)
        
        self.switch_var = customtkinter.StringVar(value="off")
        
        self.switch = customtkinter.CTkSwitch(master=self.input, width=55, height=29, switch_width=52, switch_height=27,
                                              variable=self.switch_var, fg_color="#D9D9D9", button_color="#006495",
                                              button_hover_color="#006495", text=None,
                                              onvalue="on", offvalue="off", command=self.toggle_view)
        self.switch.place(x=266, y=16)
        
        # ===== Start Frame Auto =====
        self.auto_frame = customtkinter.CTkFrame(master=self.input, width=291, height=300, fg_color="#ffffff")
        self.auto_frame.place(x=30, y=55)
        
        #===== Dropdown Menu =====
        self.dropdown = customtkinter.CTkComboBox(master=self.auto_frame, width=291, height=45, dropdown_fg_color="#E1F8FF", dropdown_text_color="#006495",
                                                  fg_color="#E1F8FF", text_color="#006495", border_color="#E1F8FF", button_color="#E1F8FF",
                                                  values=["option 1", "option 2", "option 3"], font=("Poppins", 12), dropdown_font=("Poppins", 12))
        self.dropdown.place(x=0, y=0)
        
        # ====== EC =====
        self.text1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="EC",
                                            font=("Poppins", 12), text_color="#006495")
        self.text1.place(x=0, y=63)

        self.data1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="1",
                                            font=("Poppins", 20, "bold"), text_color="#006495")
        self.data1.place(x=190, y=60)

        self.label1 = customtkinter.CTkLabel(master=self.auto_frame,
                                                text="ms/cm",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=234, y=55)
        
        # ====== PH =====
        self.text2 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="PH",
                                            font=("Poppins", 12), text_color="#006495")
        self.text2.place(x=0, y=113)

        self.data2 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="2",
                                            font=("Poppins", 20, "bold"), text_color="#006495")
        self.data2.place(x=190, y=110)
        
        # ====== HUMIDITY =====
        self.text1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="Humidity",
                                            font=("Poppins", 12), text_color="#006495")
        self.text1.place(x=0, y=163)

        self.data1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="50",
                                            font=("Poppins", 20, "bold"), text_color="#006495")
        self.data1.place(x=190, y=160)

        self.label1 = customtkinter.CTkLabel(master=self.auto_frame,
                                                text="%",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=234, y=155)
        
        # ====== VOLUME =====
        self.text1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="Volume",
                                            font=("Poppins", 12), text_color="#006495")
        self.text1.place(x=0, y=213)

        self.data1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="10",
                                            font=("Poppins", 20, "bold"), text_color="#006495")
        self.data1.place(x=190, y=210)

        self.label1 = customtkinter.CTkLabel(master=self.auto_frame,
                                                text="ms/cm",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=234, y=205)

        # ====== POPULATION =====
        self.text1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="Population",
                                            font=("Poppins", 12), text_color="#006495")
        self.text1.place(x=0, y=266)

        self.data1 = customtkinter.CTkLabel(master=self.auto_frame,
                                            text="1",
                                            font=("Poppins", 20, "bold"), text_color="#006495")
        self.data1.place(x=190, y=263)

        self.label1 = customtkinter.CTkLabel(master=self.auto_frame,
                                                text="ms/cm",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=234, y=258)
        # ===== End Frame Auto =====
        
        # ===== Start Frame Manual =====
        self.manual_frame = customtkinter.CTkFrame(master=self.input, width=291, height=300, fg_color="#ffffff")
        self.manual_frame.place(x=30, y=55)
        
        #===== Input Name =====
        self.input_name = customtkinter.CTkEntry(master=self.manual_frame, width=225, height=45, 
                                                  fg_color="#E1F8FF", text_color="#006495", border_color="#E1F8FF",
                                                  font=("Poppins", 12), placeholder_text="Input Plant Name", placeholder_text_color="#93CCEC")
        self.input_name.place(x=0, y=0)
        
        # ===== save btn =====
        self.save_button = customtkinter.CTkButton(master=self.manual_frame, width=56, height=45, corner_radius=10,
                                                   text=None, image=self.ceklis)
        self.save_button.place(x=235, y=0)
        self.save_button.configure(command=self.save_manual_data)

        
        # ====== EC =====
        self.text1 = customtkinter.CTkLabel(master=self.manual_frame,
                                            text="EC",
                                            font=("Poppins", 12), text_color="#006495")
        self.text1.place(x=0, y=63)
        
        self.inner_ec = customtkinter.CTkFrame(master=self.manual_frame, width=151, height=45, fg_color="#E1F8FF")
        self.inner_ec.place(x=130, y=51)

        self.data_ec = customtkinter.CTkEntry(master=self.inner_ec, width=50, height=44, fg_color="#E1F8FF", 
                                            text_color="#006495", border_color="#E1F8FF",font=("Poppins", 20, "bold"), 
                                            placeholder_text="00", placeholder_text_color="#93CCEC")
        self.data_ec.place(x=45, y=0)

        self.label1 = customtkinter.CTkLabel(master=self.inner_ec, text="ms/cm", font=("Poppins", 10), 
                                             text_color="#006495", fg_color="#E1F8FF")
        self.label1.place(x=94, y=4)
        
        # ====== PH =====
        self.text2 = customtkinter.CTkLabel(master=self.manual_frame,
                                            text="PH",
                                            font=("Poppins", 12), text_color="#006495")
        self.text2.place(x=0, y=113)
        
        self.inner_ph = customtkinter.CTkFrame(master=self.manual_frame, width=151, height=45, fg_color="#E1F8FF")
        self.inner_ph.place(x=130, y=102)

        self.data_ph = customtkinter.CTkEntry(master=self.inner_ph, width=50, height=44, fg_color="#E1F8FF", 
                                            text_color="#006495", border_color="#E1F8FF",font=("Poppins", 20, "bold"), 
                                            placeholder_text="00", placeholder_text_color="#93CCEC")
        self.data_ph.place(x=45, y=0)
        
        # ====== HUMIDITY =====
        self.text3 = customtkinter.CTkLabel(master=self.manual_frame,
                                            text="Humidity",
                                            font=("Poppins", 12), text_color="#006495")
        self.text3.place(x=0, y=163)
        
        self.inner_hum = customtkinter.CTkFrame(master=self.manual_frame, width=151, height=45, fg_color="#E1F8FF")
        self.inner_hum.place(x=130, y=153)

        self.data_hum = customtkinter.CTkEntry(master=self.inner_hum, width=50, height=44, fg_color="#E1F8FF", 
                                            text_color="#006495", border_color="#E1F8FF",font=("Poppins", 20, "bold"), 
                                            placeholder_text="00", placeholder_text_color="#93CCEC")
        self.data_hum.place(x=45, y=0)

        self.label3 = customtkinter.CTkLabel(master=self.inner_hum, text="%",
                                             font=("Poppins", 10), text_color="#006495")
        self.label3.place(x=94, y=4)
        
        # ====== VOLUME =====
        self.text4 = customtkinter.CTkLabel(master=self.manual_frame,
                                            text="Volume",
                                            font=("Poppins", 12), text_color="#006495")
        self.text4.place(x=0, y=213)
        
        self.inner_vol = customtkinter.CTkFrame(master=self.manual_frame, width=151, height=45, fg_color="#E1F8FF")
        self.inner_vol.place(x=130, y=204)

        self.data_vol = customtkinter.CTkEntry(master=self.inner_vol, width=50, height=44, fg_color="#E1F8FF", 
                                            text_color="#006495", border_color="#E1F8FF",font=("Poppins", 20, "bold"), 
                                            placeholder_text="00", placeholder_text_color="#93CCEC")
        self.data_vol.place(x=45, y=0)

        self.label4 = customtkinter.CTkLabel(master=self.inner_vol, text="m3",
                                            font=("Poppins", 10), text_color="#006495")
        self.label4.place(x=94, y=4)

        # ====== POPULATION =====
        self.text5 = customtkinter.CTkLabel(master=self.manual_frame,
                                            text="Population",
                                            font=("Poppins", 12), text_color="#006495")
        self.text5.place(x=0, y=266)
        
        self.inner_plant = customtkinter.CTkFrame(master=self.manual_frame, width=151, height=45, fg_color="#E1F8FF")
        self.inner_plant.place(x=130, y=255)

        self.data_plant = customtkinter.CTkEntry(master=self.inner_plant, width=132, height=44, fg_color="#E1F8FF", 
                                            text_color="#006495", border_color="#E1F8FF",font=("Poppins", 20, "bold"), 
                                            placeholder_text="00", placeholder_text_color="#93CCEC", justify="center")
        self.data_plant.place(x=0, y=0)
        # ===== End Frame Manual =====
        
        #============================================ End Input Frame ============================================

        #============================================ Start Frame Control ============================================
        self.control = customtkinter.CTkFrame(master=self.square_frame,
                                                width=351, height=87,
                                                corner_radius=10, fg_color="#006495")
        self.control.place(x=556, y=391)

        # ===== Timer ON =====
        self.label_on = customtkinter.CTkLabel(master=self.control,
                                            text="Timer ON",
                                            font=("Poppins", 10), text_color="#ffffff")
        self.label_on.place(x=50, y=10)

        self.hours_on = NumericCTkEntry(master=self.control,
                                            width=46, height=36, placeholder_text_color="#93CCEC",
                                            fg_color="#3185AE", placeholder_text="00", corner_radius=10,
                                            font=("Poppins", 16, "bold",), justify="center",
                                            text_color="#ffffff", border_color="#3185AE", border_width=1)
        self.hours_on.place(x=20, y=37)

        self.span_on = customtkinter.CTkLabel(master=self.control,
                                            text=":",
                                            font=("Poppins", 12, "bold"), text_color="#ffffff")
        self.span_on.place(x=71, y=40)

        self.minutes_on = NumericCTkEntry(master=self.control,
                                            width=46, height=36, placeholder_text_color="#93CCEC",
                                            fg_color="#3185AE", placeholder_text="00", corner_radius=10,
                                            font=("Poppins", 16, "bold",), justify="center",
                                            text_color="#ffffff", border_color="#3185AE", border_width=1)
        self.minutes_on.place(x=79, y=37)
        
        # ===== Vertical Span =====
        self.vertical_span = customtkinter.CTkFrame(master=self.control,
                                                width=2, height=60, fg_color="#ffffff")
        self.vertical_span.place(x=135, y=13.5)
        
        # ===== Timer OFF =====
        self.label_off = customtkinter.CTkLabel(master=self.control,
                                            text="Timer OFF",
                                            font=("Poppins", 10), text_color="#ffffff")
        self.label_off.place(x=175, y=10)

        self.hours_off = NumericCTkEntry(master=self.control,
                                            width=46, height=36, placeholder_text_color="#93CCEC",
                                            fg_color="#3185AE", placeholder_text="00", corner_radius=10,
                                            font=("Poppins", 16, "bold",), justify="center",
                                            text_color="#ffffff", border_color="#3185AE", border_width=1)
        self.hours_off.place(x=145, y=37)

        self.span_off = customtkinter.CTkLabel(master=self.control,
                                            text=":",
                                            font=("Poppins", 12, "bold"), text_color="#ffffff")
        self.span_off.place(x=196.5, y=40)

        self.minutes_off = NumericCTkEntry(master=self.control,
                                            width=46, height=36, placeholder_text_color="#93CCEC",
                                            fg_color="#3185AE", placeholder_text="00", corner_radius=10,
                                            font=("Poppins", 16, "bold",), justify="center",
                                            text_color="#ffffff", border_color="#3185AE", border_width=1)
        self.minutes_off.place(x=204.5, y=37)

        self.power_off = True

        self.statuspower_button = customtkinter.CTkButton(master=self.control,
                                                            width=1, height=1, 
                                                            image=self.off_btn, 
                                                            fg_color="#006495",
                                                            bg_color="#006495",
                                                            hover_color="#006495", 
                                                            text="",
                                                            command=self.power_btn)
        self.statuspower_button.place(x=271, y= 13.5)
        #============================================ End Frame Control ============================================

        self.poweredby = customtkinter.CTkLabel(master=self.square_frame,
                                                text="Powered by Red Ant Colony",
                                                font=("Poppins", 10), text_color="#006495")
        self.poweredby.place(x=348, y=496)

    def power_btn(self):
        if self.power_off:
            self.statuspower_button.configure(image=self.on_btn)
            print("machine ON")
            self.power_off = False
        else:
            self.statuspower_button.configure(image=self.off_btn)
            print("machine OFF")
            self.power_off = True

    def toggle_view(self):
        if self.switch_var.get() == "on":
            # Show Input Frame 2 and hide Input Frame 1
            self.auto_frame.place_forget()
            self.manual_frame.place(x=30, y=55)
        else:
            # Show Input Frame 1 and hide Input Frame 2
            self.manual_frame.place_forget()
            self.auto_frame.place(x=30, y=55)
            # Muat data ke dropdown saat beralih ke Auto
            self.load_presets()
            
    def stop_binding_return(self):
        self.root.unbind("<Return>")
        
    def load_presets(self):
        """
        Memuat data preset dari database ke dropdown.
        """
        try:
            # Ambil data dari database
            preset_names = self.db_connection.fetch_presets()

            if preset_names:
                # Jika ada data, masukkan ke dropdown
                self.dropdown.configure(values=preset_names)
            else:
                # Jika tidak ada data
                self.dropdown.configure(values=["No presets available"])
        except Exception as e:
            print(f"Error loading presets: {e}")
            self.dropdown.configure(values=["Error loading presets"])
            
    def save_manual_data(self):
        """
        Simpan data dari mode manual ke tabel presets.
        """
        try:
            name = self.input_name.get()
            ec = self.data_ec.get()
            ph = self.data_ph.get()
            humidity = self.data_hum.get()
            volume = self.data_vol.get()
            population = self.data_plant.get()

            if not name or not ec or not ph or not humidity or not volume or not population:
                raise ValueError("All fields must be filled!")

            # Simpan ke database
            self.db_connection.db_connected()
            query = """
                INSERT INTO presets (name, ec, ph, humidity, volume, population)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.db_connection.cursor.execute(query, (name, ec, ph, humidity, volume, population))
            self.db_connection.mysql_connection.commit()
            print("Data saved successfully!")

            # Reset input fields
            self.input_name.delete(0, 'end')
            self.data_ec.delete(0, 'end')
            self.data_ph.delete(0, 'end')
            self.data_hum.delete(0, 'end')
            self.data_vol.delete(0, 'end')
            self.data_plant.delete(0, 'end')

            # Perbarui dropdown
            self.load_presets()

        except Exception as e:
            print(f"Error saving manual data: {e}")


        
# root = customtkinter.CTk
# square_frame = customtkinter.CTk
# sensor = Ui_home(username= str, root = root , square_frame= square_frame)
# sensor.update_sensor_value

# root.after(5000, sensor.stop_binding_return)

class NumericCTkEntry(customtkinter.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(validate='key', validatecommand=(self.register(self.validate_input), '%P'))

    def validate_input(self, new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False
