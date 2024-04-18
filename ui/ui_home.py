import customtkinter
from utils.clear_frame import clear_frame
from PIL import Image
from database.connection.db_connection import Db_connection
from database.db_table import Db_table
from database.db_product import Db_product
from database.db_preset import Db_preset

class Ui_home:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        self.root.unbind("<Return>")

        clear_frame(self.square_frame)
        self.ui_images()
        self.ui_widgets()
        self.manual_frame.place_forget()

    def ui_images(self):
        # https://pixabay.com/vectors/it-business-icons-computers-722950/
        self.air_image = Image.open("images/home_images/water.png")
        self.air_image = customtkinter.CTkImage(dark_image=self.air_image,
                                                    light_image=self.air_image, 
                                                    size=(80, 107))
        
        self.tanah_image = Image.open("images/home_images/soil.png")
        self.tanah_image = customtkinter.CTkImage(dark_image=self.tanah_image,
                                                    light_image=self.tanah_image, 
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

        table_info = Db_table(self.__username).read_table()
        table_unoccupied = table_occupied = 0
        for i in table_info:
            if i[1]:
                table_occupied += 1
            else:
                table_unoccupied += 1

#################################################################################

        #============================================ Start Water Frame ============================================
        self.water_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=250, height=189,
                                                corner_radius=15,
                                                fg_color="#006495")
        self.water_frame.place(x=14, y=0)

        self.waterimage_label = customtkinter.CTkLabel(master=self.water_frame, text=None, image=self.air_image)
        self.waterimage_label.place(x=20, y=41)

        # ===== EC =====
        self.water_frame_text1 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="EC", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text1.place(x=108, y=35)

        self.water_frame_data1 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="8.5", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.water_frame_data1.place(x=148, y=33)

        self.water_frame_label1 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.water_frame_label1.place(x=190, y=30)
        
        # ===== PH =====
        self.water_frame_text2 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="PH", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text2.place(x=108, y=82)

        self.water_frame_data2 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="0", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.water_frame_data2.place(x=148, y=81)

        
        # ===== FLOW =====
        self.water_frame_text3 = customtkinter.CTkLabel(master=self.water_frame,
                                                            text="Flow", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.water_frame_text3.place(x=108, y=127)

        self.water_frame_data3 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="0", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.water_frame_data3.place(x=148, y=126)

        self.water_frame_label3 = customtkinter.CTkLabel(master=self.water_frame,
                                                        text="l/s", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.water_frame_label3.place(x=190, y=123)
        #============================================ End Water Frame ============================================

        #============================================ Start Soil Frame ============================================
        self.soil_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                width=250, height=189,
                                                corner_radius=15,
                                                fg_color="#B17E5B")
        self.soil_frame.place(x=284, y=0)

        self.soilimage_label = customtkinter.CTkLabel(master=self.soil_frame, text=None, image=self.tanah_image)
        self.soilimage_label.place(x=20, y=41)

        # ===== EC =====
        self.soil_frame_text1 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="EC", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text1.place(x=108, y=35)

        self.soil_frame_data1 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="0.6", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soil_frame_data1.place(x=148, y=33)

        self.soil_frame_label1 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="ms/cm", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.soil_frame_label1.place(x=190, y=30)
        
        # ===== PH =====
        self.soil_frame_text2 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="PH", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text2.place(x=108, y=82)

        self.soil_frame_data2 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="0", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soil_frame_data2.place(x=148, y=81)

        
        # ===== HUMIDITY =====
        self.soil_frame_text3 = customtkinter.CTkLabel(master=self.soil_frame,
                                                            text="Flow", font=("Poppins", 10, "bold"),
                                                            text_color="#ffffff")
        self.soil_frame_text3.place(x=108, y=127)

        self.soil_frame_data3 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="60", font=("Poppins", 20, "bold"),
                                                        text_color="#ffffff", justify='right')
        self.soil_frame_data3.place(x=148, y=126)

        self.soil_frame_label3 = customtkinter.CTkLabel(master=self.soil_frame,
                                                        text="%", font=("Poppins", 10),
                                                        text_color="#ffffff")
        self.soil_frame_label3.place(x=190, y=123)
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

        self.data1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data1.place(x=146, y=60)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="%",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=58)
        
        # ====== Channel B =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel B",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=113)

        self.data1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data1.place(x=146, y=111)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="%",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=109)
        
        # ====== Channel C =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel C",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=164)

        self.data1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data1.place(x=146, y=163)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="%",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=161)
        
        # ====== Channel D =====
        self.text1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="Channel D",
                                            font=("Poppins", 10), text_color="#006495")
        self.text1.place(x=35, y=216)

        self.data1 = customtkinter.CTkLabel(master=self.flow_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data1.place(x=146, y=215)

        self.label1 = customtkinter.CTkLabel(master=self.flow_frame,
                                                text="%",
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

        self.data1 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data1.place(x=146, y=60)

        self.label1 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="mm",
                                                font=("Poppins", 10), text_color="#006495")
        self.label1.place(x=186, y=58)
        
        # ====== Light =====
        self.text2 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Light Intensity",
                                            font=("Poppins", 10), text_color="#006495")
        self.text2.place(x=35, y=113)

        self.data2 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data2.place(x=146, y=111)

        self.label2 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="lux",
                                                font=("Poppins", 10), text_color="#006495")
        self.label2.place(x=186, y=109)
        
        # ====== Temperature =====
        self.text3 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Temperature",
                                            font=("Poppins", 10), text_color="#006495")
        self.text3.place(x=35, y=164)

        self.data3 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data3.place(x=146, y=163)

        self.label3 = customtkinter.CTkLabel(master=self.weather_frame,
                                                text="C",
                                                font=("Poppins", 10), text_color="#006495")
        self.label3.place(x=186, y=161)
        
        # ====== Humidity =====
        self.text4 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="Humidity",
                                            font=("Poppins", 10), text_color="#006495")
        self.text4.place(x=35, y=216)

        self.data4 = customtkinter.CTkLabel(master=self.weather_frame,
                                            text="0",
                                            font=("Poppins", 16, "bold"), text_color="#006495")
        self.data4.place(x=146, y=215)

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
        # self.switch = customtkinter.CTkSwitch(master=self.input, width=55, height=29, switch_width=52, switch_height=27,
        #                                       border_color="#006495", fg_color="#ffffff",
        #                                       border_width=2, text=None, progress_color="#006495", variable=self.switch_var,
        #                                       onvalue="on", offvalue="off", command=self.toggle_view)
        # self.switch.place(x=266, y=16)
        
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

class NumericCTkEntry(customtkinter.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(validate='key', validatecommand=(self.register(self.validate_input), '%P'))

    def validate_input(self, new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False
