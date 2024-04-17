from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_waiter(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()

    def create_waiter(self, name, cell_phone) -> True:
        __entry_items = {"name": name, "cell phone": cell_phone}
        if not empty_entries(**__entry_items):
            try:
                self.cursor.execute("""INSERT INTO WAITER (name, cell_phone)
                                    VALUES (%s, %s)""", (name, cell_phone))
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Waiter: {name}, successfully registered.")
                log().info(f'User: "{self.__username}" created the "{name}" waiter')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def read_waiter(self) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT * FROM waiter
                                order by id_waiter""")
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def update_waiter(self, new_name, new_cell_phone, id_water) -> True:
        __entry_items = {"name": new_name, "cell phone": new_cell_phone}
        if not empty_entries(**__entry_items):
            try:
                self.cursor.execute("""UPDATE waiter
                                    SET name = %s, cell_phone = %s
                                    WHERE id_waiter = %s""", (new_name, new_cell_phone, id_water))
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Waiter: {new_name}, updated successfully!")
                log().info(f'User: "{self.__username}" updated the "{new_name}" waiter')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def delete_waiter(self, id_waiter: int, waiter_name: str):
        try:
            self.cursor.execute("DELETE FROM waiter WHERE id_waiter = %s", (id_waiter,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            messagebox.showinfo(title=None, message=f"{waiter_name.capitalize()} waiter successfully deleted")
            log().info(f'User: "{self.__username}" deleted the "{waiter_name}" waiter')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_waiter(self, typed: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM waiter WHERE name LIKE %s", ("%" + typed + "%",))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()
