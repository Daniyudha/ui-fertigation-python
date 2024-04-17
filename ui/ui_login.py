import customtkinter
from ui import Ui
from PIL import Image
from utils.clear_frame import clear_frame
from database.connection.db_connection import Db_connection
from tkinter import messagebox
import json
from database.connection.db_signup import Db_signup
from utils.toconvert import toconvert
from ui.ui_panel import Ui_panel
from database.connection.db_login import Db_login
from utils.log import log

class Ui_login(Ui):
    def __init__(self):
        super().__init__()
        self.main_frame = customtkinter.CTkFrame(master=self)
        self.main_frame.pack()

        self.frame_one = customtkinter.CTkFrame(master=self.main_frame, 
                                                fg_color="#E9F4F9",
                                                bg_color="#E9F4F9")
        self.frame_one.grid(row=0, column=0)

        self.frame_two = customtkinter.CTkFrame(master=self.main_frame,
                                                width=520, height=600,
                                                fg_color="#E9F4F9",
                                                bg_color="#E9F4F9")
        self.frame_two.grid(row=0, column=1)

        self.frame_three = customtkinter.CTkFrame(master=self.frame_two,
                                                  width=480, height=483,
                                                  fg_color="#ffffff",
                                                  corner_radius=10)
        self.frame_three.place(x=16, y=58.5)

        # self.frame_four = customtkinter.CTkFrame(master=self.frame_two,
        #                                          width=458, height=220,  
        #                                          fg_color="#ffffff",
        #                                          corner_radius=10)
        # self.frame_four.place(x=33, y=388)

        self.ui_images()
        self.ui_widgets()

        foods_label = customtkinter.CTkLabel(master=self.frame_one, 
                                             text="", 
                                             image=self.foods_image)
        foods_label.grid(row=0, column=0)

        log().info("Program started")

    def ui_images(self):
        # https://pixabay.com/vectors/cheeseburger-coke-food-fries-155804/
        self.foodspil_image = Image.open("images/login_images/image.png")
        self.foods_image = customtkinter.CTkImage(dark_image=self.foodspil_image,
                                                  light_image=self.foodspil_image, 
                                                  size=(500, 600))
        
        self.logo = Image.open("images/login_images/rac-logo.png")
        self.logo = customtkinter.CTkImage(dark_image=self.logo,
                                           light_image=self.logo,
                                           size=(100, 100))

        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.userpil_image = Image.open("images/login_images/user.png")
        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(16.87, 16.28))

        self.passwordpil_image = Image.open("images/login_images/password.png")
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(13.33, 16.67))
        
        self.hostpil_image = Image.open("images/login_images/host.png")
        self.host_image = customtkinter.CTkImage(dark_image=self.hostpil_image,
                                                 light_image=self.hostpil_image,
                                                 size=(32,32))
        
        self.keypasswordpil_image = Image.open("images/login_images/keypassword.png")
        self.keypassword_image = customtkinter.CTkImage(dark_image=self.keypasswordpil_image,
                                                        light_image=self.keypasswordpil_image,
                                                        size=(32,32))

        self.emailpil_image = Image.open("images/login_images/email.png")
        self.email_image = customtkinter.CTkImage(dark_image=self.emailpil_image,
                                                  light_image=self.emailpil_image,
                                                  size=(33,33))
        
        # https://pixabay.com/vectors/ok-check-to-do-agenda-icon-symbol-1976099/
        self.loggedpil_image = Image.open("images/login_images/logged.png")
        self.logged_image = customtkinter.CTkImage(dark_image=self.loggedpil_image,
                                                   light_image=self.loggedpil_image,
                                                   size=(45,45))
        
        # https://pixabay.com/vectors/false-error-is-missing-absent-x-2061131/
        self.loggedoutpil_image = Image.open("images/login_images/loggedout.png")
        self.loggedout_image = customtkinter.CTkImage(dark_image=self.loggedoutpil_image,
                                                      light_image=self.loggedoutpil_image,
                                                      size=(45,45))
        
        # https://pixabay.com/vectors/arrow-left-gray-back-computer-23255/
        self.arrowpil_image = Image.open("images/login_images/arrow.png")
        self.arrow_image = customtkinter.CTkImage(dark_image=self.arrowpil_image,
                                                  light_image=self.arrowpil_image,
                                                  size=(15,15))

        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        self.showpasswordpil_image = Image.open("images/login_images/showpassword.png")
        self.showpassword_image = customtkinter.CTkImage(dark_image=self.showpasswordpil_image,
                                                         light_image=self.showpasswordpil_image,
                                                         size=(18,14))

        self.hidepasswordpil_image = Image.open("images/login_images/hidepassword.png")
        self.hidepassword_image = customtkinter.CTkImage(dark_image=self.hidepasswordpil_image,
                                                         light_image=self.hidepasswordpil_image,
                                                         size=(18,14)) 
        
    def ui_widgets(self):
        self.logo = customtkinter.CTkLabel(master=self.frame_three,
                                           text=None,
                                           compound="center",
                                           image=self.logo)
        self.logo.place(x=190, y=16)

        self.title = customtkinter.CTkLabel(master=self.frame_three,
                                            font=("Poppins", 20, "bold"),
                                            text="Smart Fertigation System",
                                            text_color="#006495")
        self.title.place(x=105, y=116)

        self.version = customtkinter.CTkLabel(master=self.frame_three,
                                              font=("Poppins", 12),
                                              text="v 1.0.1",
                                              text_color="#006495")
        self.version.place(x=223.5, y=146)

        self.text = customtkinter.CTkLabel(master=self.frame_three,
                                           font=("Poppins", 12),
                                           text="Silahkan masukkan Username dan Password Anda",
                                           text_color="#006495")
        self.text.place(x=80, y=179)

        self.username_label = customtkinter.CTkLabel(master=self.frame_three,
                                                     font=("arial", 15),
                                                     text="  Username:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.user_image)
        self.username_label.place(x=40, y=217)

        self.__username_entry = customtkinter.CTkEntry(master=self.frame_three, 
                                                       width=400, height=60,
                                                       font=("Poppins", 17),
                                                       fg_color="#E1F8FF",
                                                       border_color="#E1F8FF",
                                                       border_width=1)
        self.__username_entry.place(x=40, y=242)

        self.password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                     font=("arial", 15),
                                                     text="  Password:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.password_image)
        self.password_label.place(x=40, y=322)
        
        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                       width=400, height=60,
                                                       font=("Poppins", 17), 
                                                       fg_color="#E1F8FF",
                                                       border_color="#E1F8FF", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=40, y=347)

        self.__hide_password = True

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#E1F8FF",
                                                             bg_color="#E1F8FF",
                                                             hover_color="#E1F8FF", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=400, y=366)

        self.login_button = customtkinter.CTkButton(master=self.frame_three,
                                                    width=400, height=40, 
                                                    fg_color="#006495", 
                                                    hover_color="#2b8dfc",
                                                    text_color="#ffffff",
                                                    text="Log in",
                                                    font=("Poppins", 12),
                                                    command=lambda:self.login(username_entry=self.__username_entry.get(),
                                                                              password_entry=self.__password_entry.get()))
        self.login_button.place(x=40, y=427)

        self.bind("<Return>", lambda _:self.login_button.invoke())

        # self.configconnection_label = customtkinter.CTkLabel(master=self.frame_four,
        #                                                      font=("arial", 15),
        #                                                      text="MySQL Configuration:",
        #                                                      text_color="#2e2e2e")
        # self.configconnection_label.place(x=27, y=20)

        # self.configconnection_button = customtkinter.CTkButton(master=self.frame_four,
        #                                                        width=400, height=40, 
        #                                                        fg_color="#fa9725",
        #                                                        hover_color="#f5a447", 
        #                                                        text_color="#ffffff", 
        #                                                        text="Configure Connection",
        #                                                        command=self.ui_configconnection)
        # self.configconnection_button.place(x=27, y=55)

        # self.createacc_label = customtkinter.CTkLabel(master=self.frame_four,
        #                                               font=("arial", 15),
        #                                               text="Don't have an account?",
        #                                               text_color="#2e2e2e")
        # self.createacc_label.place(x=27, y=106)

        # self.createacc_button = customtkinter.CTkButton(master=self.frame_three,
        #                                                 width=400, height=40, 
        #                                                 fg_color="#4bb34b", 
        #                                                 hover_color="#61bc61",
        #                                                 text_color="#ffffff", 
        #                                                 text="Sign up",
        #                                                 command=self.ui_signup)
        # self.createacc_button.place(x=27, y=141)

    def login(self, username_entry, password_entry):
        if username_entry != "" and password_entry != "":
            __password = toconvert(password_entry)
            __login = Db_login(username= username_entry, user_password= __password)

            if __login.db_connected():
                if __login.check_login():
                    self.main_frame.destroy()
                    Ui_panel(username= username_entry, root=self)
                else:
                    messagebox.showerror("Login unsuccessful!", "Invalid username or password.")

    def ui_signup(self):
        clear_frame(self.frame_three)
        clear_frame(self.frame_three)

        self.after(10, lambda:self.frame_three.configure(width=458, height=450))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))
        
        self.after(10, lambda:self.frame_three.configure(width=458, height=500))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))

        self.user_label = customtkinter.CTkLabel(master=self.frame_three,
                                                    font=("arial", 12),
                                                    text="  Username:",
                                                    compound="left",
                                                    text_color="#2e2e2e",
                                                    image=self.user_image)
        self.user_label.place(x=27, y=40)
        
        self.__username_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                        width=400, height=40, placeholder_text="Tulis Username",
                                                        font=("arial", 12), placeholder_text_color="#80CDF3",
                                                        fg_color="#EEEEEE", text_color="#006495",
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        self.__username_entry.place(x=27, y=90)
        
        self.password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                        font=("arial", 12),
                                                        text="  Password:",
                                                        compound="left",
                                                        text_color="#2e2e2e",
                                                        image=self.keypassword_image)
        self.password_label.place(x=27, y=147)

        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three, 
                                                        width=400, height=40, placeholder_text="Tulis Password",
                                                        font=("arial", 12), placeholder_text_color="#80CDF3",
                                                        fg_color="#EEEEEE", text_color="#006495",
                                                        border_color="#e3e3e3", 
                                                        border_width=1,
                                                        show="*")
        self.__password_entry.place(x=27, y=197)

        self.__hide_password = True

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                                width=1, height=1, 
                                                                image=self.hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text="",
                                                                command=self.show_password)
        self.statuspassword_button.place(x=380, y=205)

        self.email_label = customtkinter.CTkLabel(master=self.frame_three,
                                                    font=("arial", 15),
                                                    text="  Email:",
                                                    compound="left",
                                                    text_color="#2e2e2e",
                                                    image=self.email_image)
        self.email_label.place(x=27, y=254)

        self.__email_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                    width=400, height=40,
                                                    font=("arial", 17), 
                                                    fg_color="#EEEEEE", 
                                                    border_color="#e3e3e3", 
                                                    border_width=1)
        self.__email_entry.place(x=27, y=304)

        self.signup_button = customtkinter.CTkButton(master=self.frame_three, 
                                                        width=400, height=40,
                                                        fg_color="#0077ff", 
                                                        hover_color="#1f88ff",
                                                        text_color="#ffffff",
                                                        text="Sign up",
                                                        command=lambda:Db_signup(username=self.__username_entry.get(),
                                                                                user_password=self.__password_entry.get(),
                                                                                email=self.__email_entry.get()))
        self.signup_button.place(x=27, y=380)

        self.bind("<Return>", lambda _:self.signup_button.invoke())

        self.goback_button = customtkinter.CTkButton(master=self.frame_four,
                                                        width=400, height=40, 
                                                        fg_color="#5c5c5c",
                                                        hover_color="#6e6e6e", 
                                                        text_color="#ffffff",
                                                        text="Go back",
                                                        compound="left",
                                                        image=self.arrow_image,
                                                        command=self.goback_loginscreen)
        self.goback_button.place(x=27, y=41)

        if not Db_connection.db_logged():
            self.__username_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            self.__password_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            self.__email_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            self.signup_button.configure(state="disabled", fg_color="#429aff")
            self.statuspassword_button.destroy()

            messagebox.showerror("Connection", "It's not possible to register\nwith the disconnected database!")

    def ui_configconnection(self):
        clear_frame(self.frame_three)
        clear_frame(self.frame_four)

        self.after(10, lambda:self.frame_three.configure(width=458, height=450))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))

        self.after(10, lambda:self.frame_four.configure(width=458, height=120))
        self.after(10, lambda:self.frame_four.place(x=33, y=488))

        if Db_connection.db_logged():
            self.databasestatus_image = customtkinter.CTkLabel(self.frame_three, text="", image=self.logged_image)
            self.databasestatus_image.place(x=400, y=10)
        else:
            self.databasestatus_image = customtkinter.CTkLabel(self.frame_three, text="", image=self.loggedout_image)
            self.databasestatus_image.place(x=400, y=10)

        self.host_label = customtkinter.CTkLabel(master=self.frame_three,
                                                    font=("arial", 15),
                                                    text="  Host:",
                                                    compound="left",
                                                    text_color="#2e2e2e",
                                                    image=self.host_image)
        self.host_label.place(x=27, y=40)

        self.__host_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                    width=400, height=40,
                                                    font=("arial", 17), 
                                                    fg_color="#EEEEEE", 
                                                    border_color="#e3e3e3", 
                                                    border_width=1)
        self.__host_entry.place(x=27, y=90)

        self.user_label = customtkinter.CTkLabel(master=self.frame_three,
                                                    font=("arial", 15),
                                                    text="  User:",
                                                    compound="left",
                                                    text_color="#2e2e2e",
                                                    image=self.user_image)
        self.user_label.place(x=27, y=147)

        self.__username_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                        width=400, height=40,
                                                        font=("arial", 17), 
                                                        fg_color="#EEEEEE", 
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        self.__username_entry.place(x=27, y=197)

        self.password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                        font=("arial", 15),
                                                        text="  Password:",
                                                        compound="left",
                                                        text_color="#2e2e2e",
                                                        image=self.keypassword_image)
        self.password_label.place(x=27, y=254)

        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                        width=400, height=40,
                                                        font=("arial", 17), 
                                                        fg_color="#EEEEEE", 
                                                        border_color="#e3e3e3", 
                                                        border_width=1,
                                                        show="*")
        self.__password_entry.place(x=27, y=304)

        self.__hide_password = True

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                                width=1, height=1, 
                                                                image=self.hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text="",
                                                                command=self.show_password)
        self.statuspassword_button.place(x=380, y=312)

        self.saveconfig_button = customtkinter.CTkButton(master=self.frame_three,
                                                            width=400, height=40, 
                                                            fg_color="#0077ff", 
                                                            hover_color="#1f88ff",
                                                            text_color="#ffffff", 
                                                            text="Save configuration",
                                                            command=self.saveconfig_connection)
        self.saveconfig_button.place(x=27, y=380)

        self.bind("<Return>", lambda _:self.saveconfig_button.invoke())

        self.goback_button = customtkinter.CTkButton(master=self.frame_four, 
                                                        width=400, height=40,
                                                        fg_color="#5c5c5c",
                                                        hover_color="#6e6e6e", 
                                                        text_color="#ffffff", 
                                                        text="Go back",
                                                        compound="left",
                                                        image=self.arrow_image,
                                                        command=self.goback_loginscreen)
        self.goback_button.place(x=27, y=41)
    
        try:
            with open("database/connection/config.json") as file:
                __data = json.load(file)
                self.__host_entry.insert(0, __data["host"])
                self.__username_entry.configure(placeholder_text=__data["user"])
                self.__password_entry.configure(placeholder_text= "*" * len(__data["password"]))
        except:
            self.__host_entry.configure(placeholder_text="")
            self.__username_entry.configure(placeholder_text="")
            self.__password_entry.configure(placeholder_text="")
            
            config_messagebox = {"icon": "error","type": "yesno"}
            modal = messagebox.showerror("database/connection/config.json", "Error in the database configuration file.\nRestore file?", **config_messagebox)
            
            if modal == "yes":
                __data = {"host": "localhost","user": "root","password": ""}
                with open("database/connection/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
                self.ui_configconnection()

    def saveconfig_connection(self):
        if self.__username_entry.get() != "": 
            try: 
                with open("database/connection/config.json") as __file:
                    __data = json.load(__file)
                    __data["host"] = self.__host_entry.get()
                    __data["user"] = self.__username_entry.get()
                    __data["password"] = self.__password_entry.get()

                with open("database/connection/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
            except FileNotFoundError as error:
                messagebox.showerror("Error!", f"file or directory does not exist:\ndatabase/connection/config.json\n {error}")
            except Exception as error:
                messagebox.showerror("Error!", error)
            else:
                self.ui_configconnection()

    def show_password(self):
        if self.__hide_password:
            self.statuspassword_button.configure(image=self.showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.statuspassword_button.configure(image=self.hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def goback_loginscreen(self):
        clear_frame(self.frame_three)
        clear_frame(self.frame_four)

        self.after(10, lambda:self.frame_three.configure(width=458, height=350))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))
        
        self.after(10, lambda:self.frame_four.configure(width=458, height=220))
        self.after(10, lambda:self.frame_four.place(x=33, y=388))

        self.ui_images()
        self.ui_widgets()
