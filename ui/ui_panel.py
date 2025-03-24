import customtkinter
from PIL import Image
from ui.ui_home import Ui_home
from ui.ui_sensor import Ui_sensor
from ui.ui_account import Ui_account
from ui.ui_product import Ui_product
from ui.ui_customer import Ui_customer
from ui.ui_category import Ui_category
from ui.ui_tables import Ui_table
from ui.ui_waiter import Ui_waiter
from utils.log import log
from utils.clear_frame import clear_frame
import serial

class Ui_panel:
    def __init__(self, username: str, root: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.root.geometry("1024x600")
        # self.root.attributes("-fullscreen", True)
        self.root.unbind("<Return>")
        
        self.ser = serial.Serial('/dev/serial0', 9600, timeout=1)

        self.main_frame = customtkinter.CTkFrame(master=self.root, 
                                                 width=1024, height=600,
                                                 corner_radius=0, fg_color="#E9F4F9")
        self.main_frame.grid(row=0, column=0)

        self.banner_frame = customtkinter.CTkFrame(master=self.main_frame, 
                                                   width=1024, height=70,
                                                   corner_radius=0,
                                                   fg_color="#E9F4F9")
        # self.banner_frame.grid(row=0, column=0)
        self.banner_frame.place(x=0, y=0)

        self.sidebar_frame = customtkinter.CTkFrame(master=self.main_frame,
                                                    width=67, height=526,
                                                    corner_radius=10,
                                                    fg_color="#ffffff",
                                                    border_color="#000000")
        # self.sidebar_frame.grid(row=0, column=0, )
        self.sidebar_frame.place(x=24, y=20)

        self.square_frame = customtkinter.CTkFrame(master=self.main_frame,
                                                   width=936, height=530,
                                                   corner_radius=0,
                                                   fg_color="#E9F4F9")
        self.square_frame.place(x=92, y=70)
        
        self.ui_images()
        self.ui_widgets()

        log().info(f'Logged in as "{self.__username}"')

        self.current_button: customtkinter.CTkButton = self.home_button
        self.button_selected(target_button=self.home_button)
        Ui_home(username=self.__username, root=self.root, square_frame=self.square_frame)

    def ui_images(self):
        # https://pixabay.com/vectors/fast-food-meal-cartoon-face-smile-7040523/
        # self.pizzapil_image = Image.open("images/global_images/pizza.png")
        # self.pizza_image = customtkinter.CTkImage(dark_image=self.pizzapil_image,
        #                                           light_image=self.pizzapil_image, 
        #                                           size=(80, 80))
        
        # for logo icon
        self.logo = Image.open("images/home_images/rac-logo.png")
        self.logo = customtkinter.CTkImage(dark_image=self.logo,
                                           light_image=self.logo,
                                           size=(47, 47))
        
        # for home icon
        self.home_icon = Image.open("images/home_images/home-btn.png")
        self.home_icon = customtkinter.CTkImage(dark_image=self.home_icon,
                                                  light_image=self.home_icon, 
                                                  size=(35, 29))
        
        # for sensor icon
        self.sensor_icon = Image.open("images/home_images/sensor-btn.png")
        self.sensor_icon = customtkinter.CTkImage(dark_image=self.sensor_icon,
                                                  light_image=self.sensor_icon, 
                                                  size=(35, 29))
        
        # for report icon
        self.report_icon = Image.open("images/home_images/report-btn.png")
        self.report_icon = customtkinter.CTkImage(dark_image=self.report_icon,
                                                  light_image=self.report_icon, 
                                                  size=(35, 29))
        
        # for tools icon
        self.tools_icon = Image.open("images/home_images/manual-ctrl-btn.png")
        self.tools_icon = customtkinter.CTkImage(dark_image=self.tools_icon,
                                                  light_image=self.tools_icon, 
                                                  size=(40, 40))
        
        # for account icon
        self.account_icon = Image.open("images/home_images/account-btn.png")
        self.account_icon = customtkinter.CTkImage(dark_image=self.account_icon,
                                                  light_image=self.account_icon, 
                                                  size=(35, 29))
        
        # for manual valve icon
        # self.malual_valve = Image.open("images/home_images/manual-ctrl.png")
        # self.malual_valve = customtkinter.CTkImage(dark_image=self.malual_valve,
        #                                           light_image=self.malual_valve, 
        #                                           size=(121, 20))

    def ui_widgets(self):
        self.pizza_label = customtkinter.CTkLabel(master=self.banner_frame, 
                                                  text="Smart Fertigation System",
                                                  text_color="#006495", 
                                                  font=("Poppins", 20, "bold"))
        self.pizza_label.place(x=400, y=20)
        
        # self.malual_valve = customtkinter.CTkButton(master=self.banner_frame,
        #                                                width=121, height=20, 
        #                                                fg_color="#E1F8FF", hover_color="#ffffff",
        #                                                text=None, image=self.malual_valve, command=self.ui_manual)
        # self.malual_valve.place(x=870, y=25)

        self.logo = customtkinter.CTkLabel(master=self.sidebar_frame,
                                           width=47, height=47,
                                           text=None, image=self.logo)
        self.logo.place(x=10, y=20)
        
        self.home_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                   width=40, height=60,
                                                   corner_radius=5, 
                                                   fg_color="#ffffff",
                                                   hover_color="#E1F8FF",
                                                   text=None,
                                                   image=self.home_icon,
                                                   font=("arial", 17),
                                                   command=self.home_interface)
        self.home_button.place(x=10, y=106.5)
        
        self.sensor_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                   width=40, height=60,
                                                   corner_radius=5, 
                                                   fg_color="#ffffff",
                                                   hover_color="#E1F8FF",
                                                   text=None,
                                                   image=self.sensor_icon,
                                                   font=("arial", 17),
                                                   command=self.sensor_interface)
        self.sensor_button.place(x=10, y=181.5)

        self.customer_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                       width=40, height=60,
                                                       corner_radius=5, 
                                                       fg_color="#ffffff",
                                                       hover_color="#E1F8FF",
                                                       text=None,
                                                       image=self.report_icon,
                                                       font=("arial", 17),
                                                       command=self.customer_interface)
        self.customer_button.place(x=10, y=256.5)

        self.manual_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                     width=40, height=60,
                                                     corner_radius=5,
                                                     fg_color="#ffffff",
                                                     hover_color="#E1F8FF",
                                                     text=None,
                                                     image=self.tools_icon,
                                                     font=("arial", 17),
                                                     command=self.waiter_interface)
        self.manual_button.place(x=10, y=331.5)

        # self.category_button = customtkinter.CTkButton(master=self.sidebar_frame,
        #                                                width=50, height=50,
        #                                                corner_radius=10, 
        #                                                fg_color="#ffffff",
        #                                                hover_color="#AFE2FF",
        #                                                text="Category",
        #                                                font=("arial", 17),
        #                                                command=self.category_interface)
        # self.category_button.place(x=5, y=209)

        # self.product_button = customtkinter.CTkButton(master=self.sidebar_frame,
        #                                               width=50, height=50,
        #                                               corner_radius=10, 
        #                                               fg_color="#ffffff",
        #                                               hover_color="#AFE2FF",
        #                                               text="Product",
        #                                               font=("arial", 17),
        #                                               command=self.product_interface)
        # self.product_button.place(x=5, y=277)


        # self.tables_button = customtkinter.CTkButton(master=self.sidebar_frame,
        #                                              width=50, height=50,
        #                                              corner_radius=10,
        #                                              fg_color="#ffffff",
        #                                              hover_color="#AFE2FF",
        #                                              text="Tables",
        #                                              font=("arial", 17),
        #                                              command=self.tables_interface)
        # self.tables_button.place(x=5, y=345)

        self.account_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                      width=40, height=60,
                                                      corner_radius=5, 
                                                      fg_color="#ffffff",
                                                      hover_color="#E1F8FF",
                                                      text=None,
                                                      image=self.account_icon,
                                                      font=("arial", 17),
                                                      command=self.account_interface)
        self.account_button.place(x=10, y=405.5)

        
        self.version = customtkinter.CTkLabel(master=self.sidebar_frame,
                                              text="V 1.0.1", font=("Poppins", 10, "bold"),
                                              text_color="#006495")
        self.version.place(x=15, y=491) 
    
    def ui_manual(self):
        # self.clear_frame(self.square_frame)

        # self.topbar()

        # self.topbar_label.configure(text="Add Customer")
        # self.searchcustomers_entry.destroy()
        # self.searchcustomers_button.destroy()

        self.frame_one = customtkinter.CTkFrame(master=self.root,
                                                width=1024, height=600,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=0, y=0)
        
        self.title = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("Poppins", 40, "bold"),
                                                 text_color="#006495",
                                                 text="Manual Control")
        self.title.place(x=355, y=46)

        self.label1 = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("Poppins", 12),
                                                 text_color="#006495",
                                                 text="Channel A")
        self.label1.place(x=188, y=173.38)
        
        self.switch1 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off")
        self.switch1.place(x=357, y=173.75)

        self.label2 = customtkinter.CTkLabel(master=self.frame_one,
                                                   font=("Poppins", 12),
                                                   text_color="#006495",
                                                   text="Channel B")
        self.label2.place(x=188, y=255.75)
        
        self.switch2 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off")
        self.switch2.place(x=357, y=256.25)

        self.label3 = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("Poppins", 12),
                                                      text_color="#006495",
                                                      text="Channel C")
        self.label3.place(x=188, y=338.87)
        
        self.switch3 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off")
        self.switch3.place(x=357, y=339)

        self.label4 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Channel D")
        self.label4.place(x=188, y=421.25)
        
        self.switch4 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off")
        self.switch4.place(x=357, y=421.75)
        
        # ===== Veritcal Line =====
        self.line = customtkinter.CTkFrame(master=self.frame_one,
                                                width=2, height=285,
                                                fg_color="#006495")
        self.line.place(x=502, y=170)
        
        self.label5 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Valve In")
        self.label5.place(x=522, y=173.38)
        
        self.switch5 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off")
        self.switch5.place(x=691, y=175.5)
        
        self.label6 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Valve Out")
        self.label6.place(x=522, y=255.75)
        
        self.switch6 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay6)
        self.switch6.place(x=691, y=256.25)
        
        self.label7 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Pump")
        self.label7.place(x=522, y=338.5)
        
        self.switch7 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay7)
        self.switch7.place(x=691, y=339)
        
        self.close_btn = customtkinter.CTkButton(master=self.frame_one,
                                                width=18.67, height=18.67, 
                                                font=("Poppins", 18.67),
                                                text_color="#006495",
                                                text="X", fg_color="#ffffff",
                                                hover_color="#ffffff",
                                                command=self.toback)
        self.close_btn.place(x=975, y=60)
        
        # self.cancel_button = customtkinter.CTkButton(master=self.frame_one,
        #                                              width=50, height=50,
        #                                              corner_radius=3,
        #                                              font=("arial", 15),
        #                                              text_color="#006495",
        #                                              text="X",
        #                                              fg_color="#5c5c5c", 
        #                                              hover_color="#6e6e6e",
        #                                              command=self.toback)
        # self.cancel_button.place(x=5, y=5)

        self.divider_frame = customtkinter.Frame(master=self.square_frame, 
                                           height=1, width=800, 
                                           bg="#dbdbdb")
        self.divider_frame.place(x=0, y=855)

        self.addcustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                          width=230, height=32,
                                                          corner_radius=3,
                                                          font=("arial", 15),
                                                          text_color="#ffffff",
                                                          text="Add Customer",
                                                          fg_color="#4bb34b", 
                                                          hover_color="#7ebf7e",
                                                          command=self.create_person)
        self.addcustomer_button.place(x=650, y=100)

        self.root.bind("<Return>", lambda _: self.addcustomer_button.invoke())

    def home_interface(self):
        Ui_home(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.home_button)
    
    def sensor_interface(self):
        Ui_sensor(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.sensor_button)

    def customer_interface(self):
        Ui_customer(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.customer_button)

    def category_interface(self):
        Ui_category(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.category_button)

    def product_interface(self):
        Ui_product(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.product_button)

    def waiter_interface(self):
        Ui_waiter(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.waiter_button)

    def tables_interface(self):
        Ui_table(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.tables_button)

    def account_interface(self):
        Ui_account(username=self.__username, root=self.root, square_frame=self.square_frame)
        self.button_selected(target_button=self.account_button)

    def button_selected(self, target_button:customtkinter.CTkButton):
        self.current_button.configure(fg_color="#ffffff")
        self.current_button = target_button
        self.current_button.configure(fg_color="#E1F8FF")

    def toback(self):
        clear_frame(self.frame_one)
        self.ui_widgets()
       
    def toggle_relay6(self):
        if self.switch7.get() == "0":
            self.ser.write(b"5 ON 7") 
        else:
            self.ser.write(b"5 OFF 7")
                
    def toggle_relay7(self):
        value = self.switch7.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 7\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 7")
        else:
            self.ser.write(b"5 ON 7\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 7")

