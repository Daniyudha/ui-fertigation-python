import customtkinter
import tkinter
from tkinter import messagebox
from PIL import Image
import sys
import os
from utils.clear_frame import clear_frame
from utils.toconvert import toconvert
from utils.empty_entries import empty_entries
from database.db_account import Db_account

class Ui_account:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        self.root.unbind("<Return>")

        clear_frame(self.square_frame)
        
        self.last_login = Db_account(self.__username).last_login()[0]
        
        if not self.last_login:
            self.last_login = "First Login"

        self.ui_images()
        self.ui_widgets()

    def ui_images(self):
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.userpil_image = Image.open("images/account_images/user.png")
        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(52,52))
        
        self.creationdatepil_image = Image.open("images/account_images/creationdate.png")
        self.creationdate_image = customtkinter.CTkImage(dark_image=self.creationdatepil_image,
                                                         light_image=self.creationdatepil_image,
                                                         size=(52,52))
        
        self.lastloginpil_image = Image.open("images/account_images/lastlogin.png")
        self.lastlogin_image = customtkinter.CTkImage(dark_image=self.lastloginpil_image,
                                                      light_image=self.lastloginpil_image,
                                                      size=(52,52))
        
        self.passwordpil_image = Image.open("images/account_images/password.png")
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(52,52))
        
        self.emailpil_image = Image.open("images/account_images/email.png")
        self.email_image = customtkinter.CTkImage(dark_image=self.emailpil_image,
                                                  light_image=self.emailpil_image,
                                                  size=(52,52))
        
        self.garbagepil_image = Image.open("images/account_images/garbage.png")
        self.garbage_image = customtkinter.CTkImage(dark_image=self.garbagepil_image,
                                                    light_image=self.garbagepil_image,
                                                    size=(52,52))
        
        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        self.showpasswordpil_image = Image.open("images/account_images/showpassword.png")
        self.showpassword_image = customtkinter.CTkImage(dark_image=self.showpasswordpil_image,
                                                         light_image=self.showpasswordpil_image,
                                                         size=(25,15))

        self.hidepasswordpil_image = Image.open("images/account_images/hidepassword.png")
        self.hidepassword_image = customtkinter.CTkImage(dark_image=self.hidepasswordpil_image,
                                                         light_image=self.hidepasswordpil_image,
                                                         size=(25,15))
        
        # self.newpasswordpil_image = Image.open("images/account_images/newpassword.png")
        # self.newpassword_image = customtkinter.CTkImage(dark_image=self.newpasswordpil_image,
        #                                                 light_image=self.newpasswordpil_image,
        #                                                 size=(52,52))

        # self.confirmnewpasswordpil_image = Image.open("images/account_images/confirmnewpassword.png")
        # self.confirmnewpassword_image = customtkinter.CTkImage(dark_image=self.confirmnewpasswordpil_image,
        #                                                        light_image=self.confirmnewpasswordpil_image,
        #                                                        size=(52,52))

    def ui_widgets(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Account")
        self.topbar_label.place(x=20, y=5)

        self.square_status_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                          width=1658,
                                                          height=120,
                                                          fg_color="#ffffff")
        self.square_status_frame.place(x=10, y=60)

        self.log_out_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                      width=230, height=32,
                                                      corner_radius=4,
                                                      text_color="#ffffff",
                                                      font=("arial", 15), 
                                                      text="Log Out",
                                                      fg_color="#407ecf", 
                                                      hover_color="#6996d1",
                                                      command=self.restart_program)
        self.log_out_button.place(x=1425, y=9)

        self.userimage_label = customtkinter.CTkLabel(master=self.square_status_frame,text="", image=self.user_image)
        self.userimage_label.place(x=50, y=32)
        self.user_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text="Username:")
        self.user_label.place(x=110, y=28)
        self.username_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text=self.__username)
        self.username_label.place(x=120, y=50)


        self.divider_frame = tkinter.Frame(master=self.square_status_frame, height=80, width=1)
        self.divider_frame.place(x=552, y=20)


        self.creationdateimage_label = customtkinter.CTkLabel(master=self.square_status_frame,text="", image=self.creationdate_image)
        self.creationdateimage_label.place(x=609, y=32)
        self.date_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text="Creation date:")
        self.date_label.place(x=669, y=28)
        self.creationdate_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text=Db_account(self.__username).creation_date())
        self.creationdate_label.place(x=679, y=50)


        self.divider_frame2 = tkinter.Frame(master=self.square_status_frame, height=80, width=1)
        self.divider_frame2.place(x=1104, y=20)


        self.lastloginimage_label = customtkinter.CTkLabel(master=self.square_status_frame,text="", image=self.lastlogin_image)
        self.lastloginimage_label.place(x=1158, y=32)
        self.last_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text="Last login:")
        self.last_label.place(x=1218, y=28)
        self.lastlogin_label = customtkinter.CTkLabel(master=self.square_status_frame, font=("arial", 17), text_color="#383838", text=self.last_login)
        self.lastlogin_label.place(x=1228, y=50)


        self.others_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1658,
                                                   height=710,
                                                   fg_color="#ffffff")
        self.others_frame.place(x=10, y=190)
        self.others_frame.propagate(False)

        self.changepassword_button = customtkinter.CTkButton(master=self.others_frame,
                                                             width=535, height=80, 
                                                             fg_color="#ffffff",
                                                             border_color="#e6e6e6",
                                                             border_width=1,
                                                             image=self.password_image,
                                                             font=("arial", 17), 
                                                             text_color="#383838",
                                                             hover_color="#d9d9d9", 
                                                             text="Change Password",
                                                             command=self.ui_changepassword)
        self.changepassword_button.place(x=10, y=10)

        self.changeemail_button = customtkinter.CTkButton(master=self.others_frame,
                                                          width=535, height=80, 
                                                          fg_color="#ffffff",
                                                          border_color="#e6e6e6",
                                                          border_width=1,
                                                          image=self.email_image,
                                                          font=("arial", 17), 
                                                          text_color="#383838",
                                                          hover_color="#d9d9d9", 
                                                          text="Change Email",
                                                          command=self.ui_changeemail)
        self.changeemail_button.place(x=560, y=10)

        self.deleteaccount_button = customtkinter.CTkButton(master=self.others_frame,
                                                            width=535, height=80, 
                                                            fg_color="#ffffff",
                                                            border_color="#e6e6e6",
                                                            border_width=1,
                                                            image=self.garbage_image,
                                                            font=("arial", 17), 
                                                            text_color="#383838",
                                                            hover_color="#d9d9d9", 
                                                            text="Delete account",
                                                            command=self.ui_deleteaccount)
        self.deleteaccount_button.place(x=1110, y=10)

    def ui_changepassword(self):
        try:
            self.table_toplevel.destroy()
        except:
            pass
        
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(42,42))
        
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(42,42))
        
        self.newpasswordpil_image = Image.open("images/account_images/newpassword.png")
        self.newpassword_image = customtkinter.CTkImage(dark_image=self.newpasswordpil_image,
                                                        light_image=self.newpasswordpil_image,
                                                        size=(42,42))
        
        self.confirmnewpasswordpil_image = Image.open("images/account_images/confirmnewpassword.png")
        self.confirmnewpassword_image = customtkinter.CTkImage(dark_image=self.confirmnewpasswordpil_image,
                                                               light_image=self.confirmnewpasswordpil_image,
                                                               size=(42,42))
        
        self.__hide_password = self.__hide_newpassword = self.__hide_confirmnewpassword = True

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Change Password")
        self.table_toplevel.geometry("460x535+780+290")
        self.table_toplevel.resizable(False, False)
        self.table_toplevel.configure(bg="#ffffff")

        self.username_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Username:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.user_image)
        self.username_label.grid(row=0, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__username_entry = customtkinter.CTkEntry(master=self.table_toplevel, 
                                                       width=400, height=40,
                                                       font=("arial", 17),
                                                       fg_color="#c4c4c4",
                                                       border_color="#e3e3e3",
                                                       border_width=1)
        self.__username_entry.grid(row=1, column=0, padx=30, pady=6)
        self.__username_entry.insert(0, self.__username)
        self.__username_entry.configure(state="disabled")

        self.password_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Password:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.password_image)
        self.password_label.grid(row=2, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__password_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.grid(row=3, column=0, padx=30, pady=6)

        self.statuspassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=385, y=175)

        self.newpassword_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                        font=("arial", 15),
                                                        text="  New Password:",
                                                        compound="left",
                                                        text_color="#2e2e2e",
                                                        image=self.newpassword_image)
        self.newpassword_label.grid(row=4, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__newpassword_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                          width=400, height=40,
                                                          font=("arial", 17), 
                                                          fg_color="#EEEEEE", 
                                                          border_color="#e3e3e3", 
                                                          border_width=1,
                                                          show="*")
        self.__newpassword_entry.grid(row=5, column=0, padx=30, pady=6)

        self.statusnewpassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                                width=1, height=1, 
                                                                image=self.hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text="",
                                                                command=self.show_newpassword)
        self.statusnewpassword_button.place(x=385, y=280)

        self.confirmnewpassword_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                               font=("arial", 15),
                                                               text="  Confirm New Password:",
                                                               compound="left",
                                                               text_color="#2e2e2e",
                                                               image=self.confirmnewpassword_image)
        self.confirmnewpassword_label.grid(row=6, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__confirmnewpassword_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                                 width=400, height=40,
                                                                 font=("arial", 17), 
                                                                 fg_color="#EEEEEE", 
                                                                 border_color="#e3e3e3", 
                                                                 border_width=1,
                                                                 show="*")
        self.__confirmnewpassword_entry.grid(row=7, column=0, padx=30, pady=6)

        self.statusconfirmnewpassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                                       width=1, height=1, 
                                                                       image=self.hidepassword_image, 
                                                                       fg_color="#EEEEEE",
                                                                       bg_color="#EEEEEE",
                                                                       hover_color="#EEEEEE", 
                                                                       text="",
                                                                       command=self.show_confirmnewpassword)
        self.statusconfirmnewpassword_button.place(x=385, y=385)

        self.changepassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                             width=400, height=40, 
                                                             fg_color="#2b8dfc", 
                                                             hover_color="#4da0ff",
                                                             text_color="#ffffff",
                                                             text="Save Changes",
                                                             command=lambda:self.change_password(username=self.__username,
                                                                                                 currentpassword=self.__password_entry.get(),
                                                                                                 newpassword=self.__newpassword_entry.get(),
                                                                                                 confirmnewpassword=self.__confirmnewpassword_entry.get()))
        self.changepassword_button.grid(row=8, column=0, padx=30, pady=30)

        self.root.bind("<Return>", lambda _: self.changepassword_button.invoke())
        self.table_toplevel.protocol("WM_DELETE_WINDOW", self.reset_bind)

    def ui_changeemail(self):
        try:
            self.table_toplevel.destroy()
        except:
            pass
        
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(42,42))
        
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(42,42))
        
        self.emailpil_image = Image.open("images/account_images/email.png")
        self.email_image = customtkinter.CTkImage(dark_image=self.emailpil_image,
                                                  light_image=self.emailpil_image,
                                                  size=(42,42))
        
        self.confirmnewemailpil_image = Image.open("images/account_images/confirmnewemail.png")
        self.confirmnewemail_image = customtkinter.CTkImage(dark_image=self.confirmnewemailpil_image,
                                                            light_image=self.confirmnewemailpil_image,
                                                            size=(42,42))
        
        self.__hide_password = True
        
        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Change Email")
        self.table_toplevel.geometry("460x535+780+290")
        self.table_toplevel.resizable(False, False)
        self.table_toplevel.configure(bg="#ffffff")

        self.username_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Username:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.user_image)
        self.username_label.grid(row=0, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__username_entry = customtkinter.CTkEntry(master=self.table_toplevel, 
                                                       width=400, height=40,
                                                       font=("arial", 17),
                                                       fg_color="#c4c4c4",
                                                       border_color="#e3e3e3",
                                                       border_width=1)
        self.__username_entry.grid(row=1, column=0, padx=30, pady=6)
        self.__username_entry.insert(0, self.__username)
        self.__username_entry.configure(state="disabled")

        self.password_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Password:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.password_image)
        self.password_label.grid(row=2, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__password_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.grid(row=3, column=0, padx=30, pady=6)

        self.statuspassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=385, y=174)

        self.newemail_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  New Email:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.email_image)
        self.newemail_label.grid(row=4, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__newemail_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1)
        self.__newemail_entry.grid(row=5, column=0, padx=30, pady=6)

        self.confirmnewemail_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                            font=("arial", 15),
                                                            text="  Confirm New Email:",
                                                            compound="left",
                                                            text_color="#2e2e2e",
                                                            image=self.confirmnewemail_image)
        self.confirmnewemail_label.grid(row=6, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__confirmnewpassword_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                                 width=400, height=40,
                                                                 font=("arial", 17), 
                                                                 fg_color="#EEEEEE", 
                                                                 border_color="#e3e3e3", 
                                                                 border_width=1)
        self.__confirmnewpassword_entry.grid(row=7, column=0, padx=30, pady=6)

        self.confirm_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                      width=400, height=40, 
                                                      fg_color="#2b8dfc", 
                                                      hover_color="#4da0ff",
                                                      text_color="#ffffff",
                                                      text="Save Changes")
        self.confirm_button.grid(row=8, column=0, padx=30, pady=30)

        self.root.bind("<Return>", lambda _: self.confirm_button.invoke())
        self.table_toplevel.protocol("WM_DELETE_WINDOW", self.reset_bind)

    def ui_deleteaccount(self):
        try:
            self.table_toplevel.destroy()
        except:
            pass

        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(42,42))
        
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(42,42))

        self.garbagepil_image = Image.open("images/account_images/garbage.png")
        self.garbage_image = customtkinter.CTkImage(dark_image=self.garbagepil_image,
                                                    light_image=self.garbagepil_image,
                                                    size=(42,42))
        
        self.__hide_password = True

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Delete Account")
        self.table_toplevel.geometry("460x425+780+290")
        self.table_toplevel.resizable(False, False)
        self.table_toplevel.configure(bg="#ffffff")

        self.username_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Username:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.user_image)
        self.username_label.grid(row=0, column=0, padx=30, pady=7, sticky=tkinter.W)

        self.__username_entry = customtkinter.CTkEntry(master=self.table_toplevel, 
                                                       width=400, height=40,
                                                       font=("arial", 17),
                                                       fg_color="#c4c4c4",
                                                       border_color="#e3e3e3",
                                                       border_width=1)
        self.__username_entry.grid(row=1, column=0, padx=30, pady=7)
        self.__username_entry.insert(0, self.__username)
        self.__username_entry.configure(state="disabled")

        self.password_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial", 15),
                                                     text="  Password:",
                                                     compound="left",
                                                     text_color="#2e2e2e",
                                                     image=self.password_image)
        self.password_label.grid(row=2, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.__password_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.grid(row=3, column=0, padx=30, pady=7)

        self.statuspassword_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=385, y=179)

        self.verify_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                   font=("arial", 16),
                                                   text='  To verify, "delete account" type below:',
                                                   compound="left",
                                                   text_color="#2e2e2e",
                                                   image=self.garbage_image)
        self.verify_label.grid(row=4, column=0, padx=30, pady=6, sticky=tkinter.W)

        self.verify_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                    width=400, height=40,
                                                    font=("arial", 17), 
                                                    fg_color="#EEEEEE", 
                                                    border_color="#e3e3e3", 
                                                    border_width=1)
        self.verify_entry.grid(row=5, column=0, padx=30, pady=6)

        self.delete_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                     width=400, height=40, 
                                                     fg_color="#2b8dfc", 
                                                     hover_color="#4da0ff",
                                                     text_color="#ffffff",
                                                     text="Delete Account",
                                                     command=lambda:self.delete_account(password=self.__password_entry.get(), verify=self.verify_entry.get()))
        self.delete_button.grid(row=6, column=0, padx=30, pady=26)

        self.root.bind("<Return>", lambda _: self.delete_button.invoke())
        self.table_toplevel.protocol("WM_DELETE_WINDOW", self.reset_bind)

    def change_password(self, username: str, currentpassword: str, newpassword: str, confirmnewpassword: str):
        self.__entry_items = {"password": currentpassword, "new password": newpassword, "confirm password": confirmnewpassword}
        if not empty_entries(**self.__entry_items):
            if newpassword == confirmnewpassword:
                currentpassword = toconvert(currentpassword)
                if Db_account(self.__username).check_account(password=currentpassword):
                    Db_account(self.__username).update_password(username=username,
                                                                currentpassword=currentpassword,
                                                                newpassword=toconvert(newpassword))
                    self.restart_program()
                else:
                    messagebox.showerror(title=None, message=f"Your Password may be incorrect.")
            else:
                messagebox.showerror(title=None, message=f"Your new password do not match.")
        
        self.table_toplevel.attributes("-topmost", True)
        self.table_toplevel.attributes("-topmost", False)

    def delete_account(self, password: str, verify: str):
        self.__entry_items = {"password": password, "To verify": verify}
        if not empty_entries(**self.__entry_items):
            if verify == "delete account":
                password = toconvert(password)
                if Db_account(self.__username).check_account(password=password):
                    config_messagebox = {"icon": "error","type": "yesno"}
                    modal = messagebox.showerror(title=None, message="Do you really want to delete account?", **config_messagebox)    
                
                    if modal == "yes":
                        Db_account(self.__username).delete_account(username=self.__username, password=password)
                        self.restart_program()
                    else:
                        self.table_toplevel.destroy()
                        return
                else:
                    messagebox.showerror(title=None, message=f"Your Password may be incorrect.")
            else:
                messagebox.showerror(title=None, message=f"Verify does not match.")

        self.table_toplevel.attributes("-topmost", True)
        self.table_toplevel.attributes("-topmost", False)

    def show_password(self) -> bool:
        if self.__hide_password:
            self.statuspassword_button.configure(image=self.showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.statuspassword_button.configure(image=self.hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def show_newpassword(self) -> bool:
        if self.__hide_newpassword:
            self.statusnewpassword_button.configure(image=self.showpassword_image)
            self.__newpassword_entry.configure(show="")
            self.__hide_newpassword = False
        else:
            self.statusnewpassword_button.configure(image=self.hidepassword_image)
            self.__newpassword_entry.configure(show="*")
            self.__hide_newpassword = True

    def show_confirmnewpassword(self) -> bool:
        if self.__hide_confirmnewpassword:
            self.statusconfirmnewpassword_button.configure(image=self.showpassword_image)
            self.__confirmnewpassword_entry.configure(show="")
            self.__hide_confirmnewpassword = False
        else:
            self.statusconfirmnewpassword_button.configure(image=self.hidepassword_image)
            self.__confirmnewpassword_entry.configure(show="*")
            self.__hide_confirmnewpassword = True

    def reset_bind(self):
        self.table_toplevel.destroy()
        self.root.unbind("<Return>")

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
