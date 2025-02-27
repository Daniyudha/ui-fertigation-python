import mysql.connector
import customtkinter
from tkinter import messagebox

class ManualInputApp:
    def __init__(self, root):
        self.root = root
        self.create_ui()
        self.db_connect()
        self.load_presets()

    def db_connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RedAnt69!",
            database="ferti_monitoring"
        )
        self.cursor = self.conn.cursor()

    def create_ui(self):
        self.input_frame = customtkinter.CTkFrame(master=self.root, width=291, height=500, fg_color="#ffffff")
        self.input_frame.place(x=30, y=55)
        
        self.dropdown = customtkinter.CTkComboBox(master=self.input_frame, width=291, height=45, 
                                                  fg_color="#E1F8FF", text_color="#006495", border_color="#E1F8FF", 
                                                  values=[], font=("Poppins", 12), command=self.load_selected_preset)
        self.dropdown.place(x=0, y=0)
        
        self.input_name = customtkinter.CTkEntry(master=self.input_frame, width=225, height=45, 
                                                  fg_color="#E1F8FF", text_color="#006495", border_color="#E1F8FF",
                                                  font=("Poppins", 12), placeholder_text="Input Plant Name", placeholder_text_color="#93CCEC")
        self.input_name.place(x=0, y=55)
        
        self.save_button = customtkinter.CTkButton(master=self.input_frame, width=56, height=45, corner_radius=10,
                                                   text="Save", command=self.save_manual_data)
        self.save_button.place(x=235, y=55)

        # Input Fields
        self.data_ec = self.create_entry("EC", 118)
        self.data_ph = self.create_entry("PH", 168)
        self.data_hum = self.create_entry("Humidity", 218)
        self.data_vol = self.create_entry("Volume", 268)
        self.data_plant = self.create_entry("Population", 318)
    
    def create_entry(self, label, y_pos):
        customtkinter.CTkLabel(master=self.input_frame, text=label, font=("Poppins", 12), text_color="#006495").place(x=0, y=y_pos)
        entry_frame = customtkinter.CTkFrame(master=self.input_frame, width=151, height=45, fg_color="#E1F8FF")
        entry_frame.place(x=130, y=y_pos - 12)
        entry = customtkinter.CTkEntry(master=entry_frame, width=132, height=44, fg_color="#E1F8FF", 
                                       text_color="#006495", border_color="#E1F8FF", font=("Poppins", 20, "bold"),
                                       placeholder_text="00", placeholder_text_color="#93CCEC", justify="center")
        entry.place(x=0, y=0)
        return entry

    def save_manual_data(self):
        plant_name = self.input_name.get()
        ec = self.data_ec.get()
        ph = self.data_ph.get()
        humidity = self.data_hum.get()
        volume = self.data_vol.get()
        population = self.data_plant.get()

        if not plant_name or not ec or not ph or not humidity or not volume or not population:
            messagebox.showwarning("Input Error", "Semua bidang harus diisi!")
            return

        try:
            self.cursor.execute("""
                INSERT INTO presets (name, ec, ph, humidity, volume, population)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (plant_name, ec, ph, humidity, volume, population))
            self.conn.commit()
            messagebox.showinfo("Success", "Data berhasil disimpan!")
            self.load_presets()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
    
    def load_presets(self):
        self.cursor.execute("SELECT name FROM presets")
        presets = [row[0] for row in self.cursor.fetchall()]
        self.dropdown.configure(values=presets)
    
    def load_selected_preset(self, selected_preset):
        self.cursor.execute("SELECT * FROM preset WHERE plant_name = %s", (selected_preset,))
        preset = self.cursor.fetchone()
        if preset:
            self.input_name.delete(0, "end")
            self.input_name.insert(0, preset[1])
            self.data_ec.delete(0, "end")
            self.data_ec.insert(0, preset[2])
            self.data_ph.delete(0, "end")
            self.data_ph.insert(0, preset[3])
            self.data_hum.delete(0, "end")
            self.data_hum.insert(0, preset[4])
            self.data_vol.delete(0, "end")
            self.data_vol.insert(0, preset[5])
            self.data_plant.delete(0, "end")
            self.data_plant.insert(0, preset[6])

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ManualInputApp(root)
    root.mainloop()
