import customtkinter,time
from utils.clear_frame import clear_frame
from PIL import Image
from database.connection.db_connection import Db_connection
from database.db_table import Db_table
from database.db_product import Db_product
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

class Ui_sensor:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        self.root.unbind("<Return>")
        
        # self.rain_reader = rainSensor()
        # self.pH_reader = pHSensor()
        # self.pressure_reader = PressureSensor()
        # self.light_flow_reader = light_flowSensor()
        # self.light_flow_reader.start()
        
        # self.water_soil = SerialReader(port="/dev/serial0", baudrate=9600)
        # self.water_soil.connect()
        # self.water_soil.start_reading()
        
        clear_frame(self.square_frame)
        self.ui_images()
        self.ui_widgets()
        self.manual_frame.place_forget()
        
        # self.update_temperature()
        # self.update_rainSensor()
        # self.update_pHSensor()
        # self.update_light_flowSensor()
        # self.update_water_soil()
        # self.update_pressure_sensor()
        # self.run()


    def ui_images(self):
        # https://pixabay.com/vectors/it-business-icons-computers-722950/
        
        self.soil_image = Image.open("images/home_images/soil-icon-only.png")
        self.soil_image = customtkinter.CTkImage(dark_image=self.soil_image,
                                                    light_image=self.soil_image, 
                                                    size=(23.36, 17.3))
        
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

        #============================================ Start DHT Frame ============================================
        self.dht_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=232, height=252,
                                                corner_radius=15,
                                                fg_color="#006495")
        self.dht_frame.place(x=14, y=0)

        # ===== LABEL DHT =====
        self.dht_label = customtkinter.CTkLabel(master=self.dht_frame,
                                                text="DHT11 Sensor", font=("Poppins", 16, "bold"),
                                                text_color="#ffffff", justify='center')
        self.dht_label.place(x=50, y=16)
        
        # ===== TEMP =====
        self.temp_label = customtkinter.CTkLabel(master=self.dht_frame,
                                                            text="Air Temperature", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.temp_label.place(x=35, y=106.5)

        self.tempValue = customtkinter.CTkLabel(master=self.dht_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.tempValue.place(x=144, y=105)

        self.temp_frame_label = customtkinter.CTkLabel(master=self.dht_frame,
                                                        text="C", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.temp_frame_label.place(x=186, y=102)
        
        # ===== HUMI =====
        self.hum_label = customtkinter.CTkLabel(master=self.dht_frame,
                                                            text="Air Humidity", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.hum_label.place(x=35, y=148.5)

        self.humValue = customtkinter.CTkLabel(master=self.dht_frame,
                                                        text="0", font=("Poppins", 18, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.humValue.place(x=144, y=147)

        self.hum_frame_label = customtkinter.CTkLabel(master=self.dht_frame,
                                                        text="%", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.hum_frame_label.place(x=186, y=144)
        #============================================ End DHT ============================================

       #============================================ Start Other Sensor ============================================
        self.otherSensor_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=645, height=252,
                                                corner_radius=15,
                                                fg_color="#ffffff")
        self.otherSensor_frame.place(x=264, y=0)
        
        # ===== LABEL Other =====
        self.otherSensor_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Other Sensor", font=("Poppins", 16, "bold"),
                                                text_color="#006495", justify='center')
        self.otherSensor_label.place(x=250, y=16)
        
        # ===== Light =====
        self.light_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Light Intencity", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.light_label.place(x=35, y=64.5)
        
        self.lightValue = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.lightValue.place(x=165, y=65)

        self.light_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lux", font=("Poppins", 10),
                                                        text_color="#006495")
        self.light_frame_label.place(x=220, y=62)
        
        # ===== Rain =====
        self.rain_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Rain Intencity", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.rain_label.place(x=35, y=100.5)
        
        self.rainValue = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.rainValue.place(x=165, y=101)

        self.rain_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lux", font=("Poppins", 10),
                                                        text_color="#006495")
        self.rain_frame_label.place(x=220, y=198)
        
        # ===== ph =====
        self.ph_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Water PH", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.ph_label.place(x=35, y=136.5)
        
        self.phValue = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.phValue.place(x=165, y=137)
        
        # ===== EC Water =====
        self.ecWater_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Water Condictivity", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.ecWater_label.place(x=35, y=172.5)
        
        self.ecWaterValue = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.ecWaterValue.place(x=165, y=173)

        self.ecWater_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#006495")
        self.ecWater_frame_label.place(x=220, y=170)
        
        # ===== Pressure =====
        self.pressure_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Pressure", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.pressure_label.place(x=35, y=208.5)
        
        self.pressureValue = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.pressureValue.place(x=165, y=209)

        self.pressure_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="bar", font=("Poppins", 10),
                                                        text_color="#006495")
        self.pressure_frame_label.place(x=220, y=206)
        
        # ===== Veritcal Line =====
        self.lineOther = customtkinter.CTkFrame(master=self.otherSensor_frame,
                                                width=2, height=180,
                                                corner_radius=15,
                                                fg_color="#006495")
        self.lineOther.place(x=322.5, y=56)
        
        
        # ===== Flow 1 =====
        self.Flow1_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Flow 1", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.Flow1_label.place(x=348, y=64.5)
        
        self.Flow1Value = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.Flow1Value.place(x=465, y=65)

        self.Flow1_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lpm", font=("Poppins", 10),
                                                        text_color="#006495")
        self.Flow1_frame_label.place(x=500, y=62)
        
        # ===== Flow 2 =====
        self.Flow2_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Flow 2", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.Flow2_label.place(x=348, y=112.5)
        
        self.Flow2Value = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.Flow2Value.place(x=465, y=113)

        self.Flow2_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lpm", font=("Poppins", 10),
                                                        text_color="#006495")
        self.Flow2_frame_label.place(x=500, y=110)
        
        # ===== Flow 3 =====
        self.Flow3_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Flow 3", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.Flow3_label.place(x=348, y=160.5)
    
        self.Flow3Value = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.Flow3Value.place(x=465, y=161)

        self.Flow3_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lpm", font=("Poppins", 10),
                                                        text_color="#006495")
        self.Flow3_frame_label.place(x=500, y=158)
        
        # ===== Flow 4 =====
        self.Flow4_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                text="Flow 4", font=("Poppins", 10),
                                                text_color="#006495", justify='center')
        self.Flow4_label.place(x=348, y=208.5)
        
        self.Flow4Value = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#006495", justify='center')
        self.Flow4Value.place(x=465, y=203)

        self.Flow4_frame_label = customtkinter.CTkLabel(master=self.otherSensor_frame,
                                                        text="lpm", font=("Poppins", 10),
                                                        text_color="#006495")
        self.Flow4_frame_label.place(x=500, y=200)
        #============================================ End Other Sensor ============================================
        
        #============================================ Start Soil 1 ============================================
        self.soil1_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=438, height=211,
                                                corner_radius=15,
                                                fg_color="#B17E5B")
        self.soil1_frame.place(x=14, y=272)
                
        # ===== Icon Soil 1 =====
        self.soilimage_label = customtkinter.CTkLabel(master=self.soil1_frame, text=None, image=self.soil_image)
        self.soilimage_label.place(x=184, y=22.3)
        
        # ===== LABEL Soil 1 =====
        self.otherSensor_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Soil 1", font=("Poppins", 16, "bold"),
                                                text_color="#ffffff", justify='center')
        self.otherSensor_label.place(x=218.5, y=22)
        
        # ===== Moisture =====
        self.moisture1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Moisture", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.moisture1_label.place(x=35, y=70.5)
        
        self.moisture1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.moisture1Value.place(x=125, y=71)

        self.moisture1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="%", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.moisture1_frame_label.place(x=178, y=68)
        
        # ===== Temperature =====
        self.temp1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Temperature", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.temp1_label.place(x=35, y=102.83)
        
        self.temp1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.temp1Value.place(x=125, y=103.33)

        self.temp1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="C", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.temp1_frame_label.place(x=178, y=100.33)
        
        # ===== Conductivity =====
        self.ec1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Conductivity", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.ec1_label.place(x=35, y=135.17)
        
        self.ec1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.ec1Value.place(x=125, y=136.67)

        self.ec1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.ec1_frame_label.place(x=178, y=133.67)
        
        # ===== PH =====
        self.ph1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="PH", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.ph1_label.place(x=35, y=163.5)
        
        self.ph1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.ph1Value.place(x=125, y=164)
        
        # ===== Veritcal Line =====
        self.linesoil1 = customtkinter.CTkFrame(master=self.soil1_frame,
                                                width=2, height=133,
                                                corner_radius=15,
                                                fg_color="#ffffff")
        self.linesoil1.place(x=219, y=62)
        
        # ===== Nirtogen =====
        self.nitro1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Nirtogen", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.nitro1_label.place(x=234, y=70.5)
        
        self.nitro1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.nitro1Value.place(x=325, y=71)

        self.nitro1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="g/mL", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.nitro1_frame_label.place(x=378, y=68)
        
        # ===== Phosphorus =====
        self.fosfor1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Phosphorus", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.fosfor1_label.place(x=234, y=119)
        
        self.fosfor1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.fosfor1Value.place(x=325, y=120.5)

        self.fosfor1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="mg/L", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.fosfor1_frame_label.place(x=378, y=117.5)
        
        # ===== Potassium =====
        self.potas1_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                text="Potassium", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.potas1_label.place(x=234, y=163.5)
        
        self.potas1Value = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.potas1Value.place(x=325, y=164)

        self.potas1_frame_label = customtkinter.CTkLabel(master=self.soil1_frame,
                                                        text="mEq", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.potas1_frame_label.place(x=378, y=161)
        #============================================ End Soil 1 ============================================
        
        #============================================ Start Soil 2 ============================================
        self.soil2_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=438, height=211,
                                                corner_radius=15,
                                                fg_color="#B17E5B")
        self.soil2_frame.place(x=469, y=272)
        
        # ===== Icon Soil 2 =====
        self.soilimage_label = customtkinter.CTkLabel(master=self.soil2_frame, text=None, image=self.soil_image)
        self.soilimage_label.place(x=184, y=22.3)
        
        # ===== LABEL Soil 2 =====
        self.otherSensor_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Soil 2", font=("Poppins", 16, "bold"),
                                                text_color="#ffffff", justify='center')
        self.otherSensor_label.place(x=218.5, y=22)
        
        # ===== Moisture =====
        self.moisture2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Moisture", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.moisture2_label.place(x=35, y=70.5)
        
        self.moisture2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.moisture2Value.place(x=125, y=71)

        self.moisture2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="%", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.moisture2_frame_label.place(x=178, y=68)
        
        # ===== Temperature =====
        self.temp2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Temperature", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.temp2_label.place(x=35, y=102.83)
        
        self.temp2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.temp2Value.place(x=125, y=103.33)

        self.temp2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="C", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.temp2_frame_label.place(x=178, y=100.33)
        
        # ===== Conductivity =====
        self.ec2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Conductivity", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.ec2_label.place(x=35, y=135.17)
        
        self.ec2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.ec2Value.place(x=125, y=136.67)

        self.ec2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.ec2_frame_label.place(x=178, y=133.67)
        
        # ===== PH =====
        self.ph2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="PH", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.ph2_label.place(x=35, y=163.5)
        
        self.ph2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.ph2Value.place(x=125, y=164)
        
        # ===== Veritcal Line =====
        self.linesoil2 = customtkinter.CTkFrame(master=self.soil2_frame,
                                                width=2, height=133,
                                                corner_radius=15,
                                                fg_color="#ffffff")
        self.linesoil2.place(x=219, y=62)
        
        # ===== Nirtogen =====
        self.nitro2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Nirtogen", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.nitro2_label.place(x=234, y=70.5)
        
        self.nitro2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.nitro2Value.place(x=325, y=71)

        self.nitro2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="g/mL", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.nitro2_frame_label.place(x=378, y=68)
        
        # ===== Phosphorus =====
        self.fosfor2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Phosphorus", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.fosfor2_label.place(x=234, y=119)
        
        self.fosfor2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.fosfor2Value.place(x=325, y=120.5)

        self.fosfor2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="mg/L", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.fosfor2_frame_label.place(x=378, y=117.5)
        
        # ===== Potassium =====
        self.potas2_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                text="Potassium", font=("Poppins", 10),
                                                text_color="#ffffff", justify='center')
        self.potas2_label.place(x=234, y=163.5)
        
        self.potas2Value = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="0", font=("Poppins", 16, "bold"),
                                                        text_color="#ffffff", justify='center')
        self.potas2Value.place(x=325, y=164)

        self.potas2_frame_label = customtkinter.CTkLabel(master=self.soil2_frame,
                                                        text="mEq", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.potas2_frame_label.place(x=378, y=161)
        #============================================ End Soil 2 ============================================
        
            
    def stop_binding_return(self):
        self.root.unbind("<Return>")
        
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
