import mysql.connector
import json
from tkinter import messagebox
import sys

class Db_connection:
    def __init__(self):
        try:
            with open("database/connection/config.json") as __file:
                __data = json.load(__file)
                self.__host = __data["host"]
                self.__user = __data["user"]
                self.__password = __data["password"]
        except Exception as error:
            messagebox.showerror("Error!", f"Error: {error}\nFile error: database/connection/config.json")

    def db_connected(self, database: str | None ="ferti_monitoring") -> True:
        try:            
            self.mysql_connection = mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                database = "ferti_monitoring"
            )
            self.cursor = self.mysql_connection.cursor()
        except Exception as error:
            error = str(error)
            if "Can't connect to MySQL server" in error:
                if "a real number is required" in error:
                    messagebox.showerror("MySQL error", "Make sure the host is entered correctly.")
                else:
                    messagebox.showerror("MySQL error", "MySQL connection issue\nCheck your MySQL Server.")
                    sys.exit()
            else:
                messagebox.showerror("MySQL error", "Check connection configurations.")
        else:
            return True

    def total_rowstable(self, table: str) -> int:
        try:
            if self.db_connected():
                self.cursor.execute("SELECT COUNT(*) FROM %s" %(table,))
                result = self.cursor.fetchall()[0][0]
                return result
        except Exception as error:
            messagebox.showerror("Error", f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    @staticmethod
    def db_logged() -> bool:
        mysql_connection = None
        try:
            with open("database/connection/config.json") as __file:
                __data = json.load(__file)
                __host = __data["host"]
                __user = __data["user"]
                __password = __data["password"]
            
            mysql_connection = mysql.connector.connect(
                host=__host,
                user=__user,
                password=__password,
                database= None
            )
            mysql_connection.cursor()
        except:
            return False
        else:
            return True
        finally:
            if mysql_connection is not None:
                mysql_connection.close()
                
    def fetch_presets(self):
        """
        Mengambil data nama preset dari tabel presets.
        """
        try:
            self.db_connected()  # Pastikan koneksi aktif
            query = "SELECT name FROM presets"
            self.cursor.execute(query)
            results = [row[0] for row in self.cursor.fetchall()]  # Ambil semua nama preset
            return results
        except Exception as e:
            print(f"Error fetching presets: {e}")
            return []
        finally:
            self.cursor.close()
            self.mysql_connection.close()
