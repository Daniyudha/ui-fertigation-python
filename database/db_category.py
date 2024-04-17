from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_category(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()

    def create_category(self, id_category: int, category_name: str, description: str):
        self.__entry_items = {"id category": id_category, "category name": category_name}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""INSERT INTO CATEGORY (id_category, category_name, description) 
                                    VALUES (%s, %s, %s);""", (id_category, category_name, description))
                self.mysql_connection.commit()
            except Exception as error:
                if "Incorrect integer value" in str(error):
                    messagebox.showerror(title="ID", message=f"Enter an integer value!")
                elif "Duplicate entry" in str(error):
                    messagebox.showerror(title="ID", message=f"ID already exists, try another one.")
                else:
                    messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Category: {category_name}, successfully registered.")
                log().info(f'User: "{self.__username}" created the "{category_name}" category')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close

    def read_category(self) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT * FROM category
                                order by id_category""")
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def update_category(self, new_id, new_categoryname, new_description, old_id):
        self.__entry_items = {"id category": new_id, "category name": new_categoryname}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""UPDATE category
                                    SET id_category = %s, category_name = %s, description = %s
                                    WHERE id_category = %s""", (new_id, new_categoryname, new_description, old_id))
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Category: {new_categoryname}, updated successfully!")
                log().info(f'User: "{self.__username}" updated the "{new_categoryname}" category')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def delete_category(self, id_category: int, category_name: str):
        try:
            self.cursor.execute("DELETE FROM category WHERE id_category = %s", (id_category,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            messagebox.showinfo(title=None, message=f"{category_name.capitalize()} category successfully deleted")
            log().info(f'User: "{self.__username}" deleted the "{category_name}" category')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_category(self, typed: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM category WHERE category_name LIKE %s", ("%" + typed + "%",))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()
