from database.connection.db_connection import Db_connection
from datetime import datetime
from tkinter import messagebox

class Db_login(Db_connection):
    def __init__(self, username: str, user_password: str):
        super().__init__()
        self.__username = username
        self.__user_password = user_password

    def check_login(self) -> bool:
        try:
            self.cursor.execute("""SELECT * FROM account 
                                WHERE username = %s AND password = %s""", (self.__username, self.__user_password))
            self.result = self.cursor.fetchone()
        except Exception as error:
            messagebox.showerror("Error", f"{error}")
        else:
            if self.result:
                try:
                    self.cursor.execute("""SELECT register_login FROM account 
                                        WHERE username = %s AND password = %s""", (self.__username, self.__user_password))
                    self.last_login_date = self.cursor.fetchone()

                    self.cursor.execute("""UPDATE account SET last_login = %s 
                                        WHERE username = %s AND password = %s""", (self.last_login_date[0], self.__username, self.__user_password))
                    self.mysql_connection.commit()
                except Exception as error:
                    messagebox.showerror("Error", f"{error}")
                else:
                    self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.cursor.execute("""UPDATE account SET register_login = %s 
                                        WHERE username = %s AND password = %s""", (self.data, self.__username, self.__user_password))
                    self.mysql_connection.commit()
                    return True
                finally:
                    self.cursor.close()
                    self.mysql_connection.close()
