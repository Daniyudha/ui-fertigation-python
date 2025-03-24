import customtkinter
from utils.clear_frame import clear_frame
from tkinter import ttk, messagebox
import tkinter
from database.db_waiter import Db_waiter
import serial
import time

class Ui_waiter:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        
        self.ser = serial.Serial('/dev/serial0', 9600, timeout=1)
        self.full_open_time = 13

        clear_frame(self.square_frame)
        self.ui_widgets()

    def ui_widgets(self):
        
        self.frame_one = customtkinter.CTkFrame(master=self.square_frame,
                                                width=893, height=476,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=16, y=0)
        
        self.title = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("Poppins", 24, "bold"),
                                                 text_color="#006495",
                                                 text="Manual Control")
        self.title.place(x=350, y=32)

        self.label1 = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("Poppins", 12),
                                                 text_color="#006495",
                                                 text="Channel A")
        self.label1.place(x=188, y=132)
        
        self.percent_entry = customtkinter.CTkEntry(master=self.frame_one, width=80)
        self.percent_entry.insert(0, "100")  # Default 100%
        self.percent_entry.place(x=270, y=132)

        
        self.switch1 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay1)
        self.switch1.place(x=357, y=132)

        self.label2 = customtkinter.CTkLabel(master=self.frame_one,
                                                   font=("Poppins", 12),
                                                   text_color="#006495",
                                                   text="Channel B")
        self.label2.place(x=188, y=194)
        
        self.switch2 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay2)
        self.switch2.place(x=357, y=194)

        self.label3 = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("Poppins", 12),
                                                      text_color="#006495",
                                                      text="Channel C")
        self.label3.place(x=188, y=256)
        
        self.switch3 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay3)
        self.switch3.place(x=357, y=256)

        self.label4 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Channel D")
        self.label4.place(x=188, y=318)
        
        self.switch4 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay4)
        self.switch4.place(x=357, y=318)
        
        # ===== Veritcal Line =====
        self.line = customtkinter.CTkFrame(master=self.frame_one,
                                                width=2, height=216,
                                                fg_color="#006495")
        self.line.place(x=440, y=132)
        
        self.label5 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Valve In")
        self.label5.place(x=456, y=132)
        
        self.switch5 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay5)
        self.switch5.place(x=625, y=132)
        
        self.label6 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Valve Out")
        self.label6.place(x=456, y=194)
        
        self.switch6 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay6)
        self.switch6.place(x=625, y=194)
        
        self.label7 = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("Poppins", 12),
                                                  text_color="#006495",
                                                  text="Pump")
        self.label7.place(x=456, y=256)
        
        self.switch7 = customtkinter.CTkSwitch(master=self.frame_one, width=70, height=29.75, 
                                               switch_width=70, switch_height=29.75,
                                               fg_color="#D9D9D9", button_color="#006495",
                                               button_hover_color="#006495", text=None,
                                               onvalue="on", offvalue="off", command=self.toggle_relay7)
        self.switch7.place(x=625, y=256)

        
    def toback(self):
        clear_frame(self.square_frame)
        self.ui_widgets()
        
    def send_command(self, command):
        """Mengirim perintah ke relay via Serial"""
        self.ser.write(command.encode() + b"\n")
        print(f"Perintah dikirim: {command}")

    def toggle_relay1(self):
        """Mengontrol relay berdasarkan persentase di Entry"""
        value = self.switch1.get()  # Ambil status switch (on/off)

        try:
            percentage = float(self.percent_entry.get())  # Ambil nilai persentase
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka valid untuk persentase!")
            return

        if not (0 <= percentage <= 100):
            messagebox.showerror("Error", "Persentase harus antara 0-100!")
            return

        duration = (percentage / 100) * self.full_open_time  # Hitung waktu buka

        if value == "on":
            self.send_command("5 ON 6")  # Perintah buka
            print(f"Membuka selama {duration:.2f} detik...")

            time.sleep(duration)  # Tunggu sesuai durasi

            self.send_command("5 ON 5")  # Perintah stop buka
            print("Bukaan dihentikan!")

            # time.sleep(0.5)  # Tunggu 0.5 detik sebelum mematikan relay
            # self.send_command("5 OFF 5")  # Pastikan relay mati
            # print("Relay 5 dimatikan untuk memastikan tidak tertahan.")
        else:
            self.send_command("5 OFF 6")  # Perintah tutup penuh
            print("Menutup penuh...")
            self.send_command("5 OFF 5")

            time.sleep(self.full_open_time)  # Tunggu hingga tutup penuh

            self.send_command("5 OFF 4")  # Perintah stop tutup
            print("Tutup dihentikan!")
    
    def toggle_relay2(self):
        value = self.switch2.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 3\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 3")
        else:
            self.ser.write(b"5 ON 3\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 3")
    
    def toggle_relay3(self):
        value = self.switch3.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 0\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 0")
        else:
            self.ser.write(b"5 ON 0\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 0")
               
    def toggle_relay4(self):
        value = self.switch4.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 5\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 5")
        else:
            self.ser.write(b"5 ON 5\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 5")
            
    def toggle_relay5(self):
        value = self.switch5.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 1\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 1")
        else:
            self.ser.write(b"5 ON 1\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 1")
        
    def toggle_relay6(self):
        value = self.switch6.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 6\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 6")
        else:
            self.ser.write(b"5 ON 6\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 6")
                
    def toggle_relay7(self):
        value = self.switch7.get()  # Dapatkan nilai switch
        if value == "off":
            self.ser.write(b"5 OFF 7\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 OFF 7")
        else:
            self.ser.write(b"5 ON 7\n")  # Tambahkan \n di akhir
            print("Mengirim: 5 ON 7")
