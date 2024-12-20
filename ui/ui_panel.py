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

class Ui_panel:
    def __init__(self, username: str, root: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.root.geometry("1024x600")
        # self.root.attributes("-fullscreen", True)
        self.root.unbind("<Return>")

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
        self.tools_icon = Image.open("images/home_images/setting-btn.png")
        self.tools_icon = customtkinter.CTkImage(dark_image=self.tools_icon,
                                                  light_image=self.tools_icon, 
                                                  size=(35, 29))
        
        # for account icon
        self.account_icon = Image.open("images/home_images/account-btn.png")
        self.account_icon = customtkinter.CTkImage(dark_image=self.account_icon,
                                                  light_image=self.account_icon, 
                                                  size=(35, 29))

    def ui_widgets(self):
        self.pizza_label = customtkinter.CTkLabel(master=self.banner_frame, 
                                                  text="Smart Fertigation System",
                                                  text_color="#006495", 
                                                  font=("Poppins", 20, "bold"))
        self.pizza_label.place(x=400, y=20)

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

        self.waiter_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                     width=40, height=60,
                                                     corner_radius=5,
                                                     fg_color="#ffffff",
                                                     hover_color="#E1F8FF",
                                                     text=None,
                                                     image=self.tools_icon,
                                                     font=("arial", 17),
                                                     command=self.waiter_interface)
        self.waiter_button.place(x=10, y=331.5)

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
