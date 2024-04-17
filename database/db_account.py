from database.connection.db_connection import Db_connection
from tkinter import messagebox
from utils.log import log

class Db_account(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()
    
    def creation_date(self) -> str:
        try:
            self.cursor.execute("""SELECT creation_date FROM account
                                WHERE username = %s""", (self.__username,))
            self.account_date = self.cursor.fetchone()[0]
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.account_date
        finally:
            self.cursor.close()
            self.mysql_connection.close()
            
    def update_password(self, username: str, currentpassword: str, newpassword: str):
        try:
            self.cursor.execute("""UPDATE account
                                SET password = %s
                                WHERE username = %s and PASSWORD = %s""", (newpassword, username, currentpassword))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            messagebox.showinfo(title=None, message=f"Password updated successfully!")
            log().info(f'User: "{self.__username}" updated password.')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def delete_account(self, username: str, password: str):
        try:
            self.cursor.execute("DELETE FROM account WHERE username = %s and PASSWORD = %s", (username, password))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" deleted their own account')
            messagebox.showinfo(title=None, message=f"Account deleted successfully!")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def last_login(self) -> str:
        try:
            self.cursor.execute("""SELECT last_login FROM account 
                                WHERE username = %s""", (self.__username,))
            self.last_logininfo = self.cursor.fetchone()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.last_logininfo
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def check_account(self, password: str) -> True:
        try:
            self.cursor.execute("""SELECT * FROM account 
                                WHERE username = %s AND password = %s""", (self.__username, password))
            self.result = self.cursor.fetchone()
        except Exception as error:
            messagebox.showerror("Error", f"{error}")
        else:
            if self.result:
                return True
        finally:
            self.cursor.close()
            self.mysql_connection.close()
