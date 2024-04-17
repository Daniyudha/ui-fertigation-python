from database.connection.database import Database
from tkinter import messagebox
import mysql.connector
from utils.empty_entries import empty_entries
from utils.log import log

class Db_signup(Database):
    def __init__(self, username: str, user_password: str, email: str):
        super().__init__()
        self.__username = username.strip()
        self.__user_password = user_password
        self.__email = email
        self.__entry_items = {"username":self.__username, "password":self.__user_password, "email":self.__email}  
        
        if not empty_entries(**self.__entry_items):
            if "@" not in self.__email or ".com" not in self.__email or len(self.__email) < 8:
                messagebox.showerror(title="Email field", message=f"Please enter a valid email address.")
            else:
                try:
                    self.login_tables()
                    self.cursor.execute("""INSERT INTO account (username, password, email) 
                                        VALUES (%s, md5(%s), %s);""", (self.__username, self.__user_password, self.__email))
                    self.mysql_connection.commit()
                except mysql.connector.errors.IntegrityError:
                    messagebox.showerror(title="Error!", message="Sorry, but the username is already taken.\nPlease choose a different username.")
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                else:
                    messagebox.showinfo(title=None, message="Congratulations! Your account\nhas been successfully created.")
                    log().info(f'"{self.__username}" account was created')
                finally:
                    self.cursor.close()
                    self.mysql_connection.close()
