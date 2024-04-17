from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_preset(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()

    def create_preset(self, name: str, ec: float, ph: float, humidity: float, volume: float, population: float):
        self.__entry_items = {"name": name, "ec": ec, "ph": ph, "humidity": float, "volume": float, "population": int}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""INSERT INTO presets (name, ec, ph, humidity, volume, population) 
                                    VALUES (%s, %s, %s, %s, %s, %s);""", (name, ec, ph, humidity, volume, population))
                self.mysql_connection.commit()
            except Exception as error:
                if "Incorrect integer value" in str(error):
                    messagebox.showerror(title="ID", message=f"Enter an integer value!")
                elif "Duplicate entry" in str(error):
                    messagebox.showerror(title="ID", message=f"ID already exists, try another one.")
                else:
                    messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Preset: {name}, successfully registered.")
                log().info(f'User: "{self.__username}" created the "{name}" Preset')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close

    def read_preset(self) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT * FROM presets
                                order by name""")
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def update_preset(self, new_name, new_ec, new_ph, new_humidity, new_volume, new_population):
        self.__entry_items = {"name": new_name, "ec": new_ec, "ph": new_ph, "humidity": new_humidity, "volume": new_volume, "pupulation": new_population}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""UPDATE presets
                                    SET name = %s, ec = %s, ph = %s, humidity = %s, volume = %s, population = %s
                                    WHERE Preset = %s""", (new_name, new_ec, new_ph, new_humidity, new_volume, new_population))
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Preset: {new_name}, updated successfully!")
                log().info(f'User: "{self.__username}" updated the "{new_name}" Preset')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def delete_category(self, name: str):
        try:
            self.cursor.execute("DELETE FROM presets WHERE name = %s", (name,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            messagebox.showinfo(title=None, message=f"{name.capitalize()} Preset successfully deleted")
            log().info(f'User: "{self.__username}" Preset the "{name}" Preset')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_category(self, typed: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM presets WHERE name LIKE %s", ("%" + typed + "%",))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()
