from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_customer(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username
        
        if self.db_connected():
            try:
                self.cursor.execute("""SELECT id_account FROM account
                                    WHERE username = %s""", (self.__username,))
                self.id_account = self.cursor.fetchone()[0]
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")

    def create_customer(self, name: str, address: str, cellphone: str, email: str | None = None) -> bool:
        self.__entry_items = {"name": name, "address": address, "cellphone": cellphone}
        if not empty_entries(**self.__entry_items):
            try:
                if email is None:
                    self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, account_id_account)
                                        VALUES (%s, %s, %s, %s)""", (name, address, cellphone, self.id_account))
                    self.mysql_connection.commit()
                else:
                    if "@" not in email or ".com" not in email or len(email) < 8:
                        messagebox.showerror(title="Email field", message=f"Please enter a valid email address.")
                        return
                    else:
                        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, email, account_id_account)
                                            VALUES (%s, %s, %s, %s, %s)""", (name, address, cellphone, email, self.id_account))
                        self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Customer: {name}, successfully registered.")
                log().info(f'User "{self.__username}" registered the customer "{name}"')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()
    
    def read_customer(self) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT * FROM customer
                                order by id_customer""")
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()
    
    def update_customer(self, id_customer: str, name: str, address: str, cellphone: str, email: str | None = None) -> True:
        self.__entry_items = {"name": name, "address": address, "cellphone": cellphone}
        if not empty_entries(**self.__entry_items):
            try:
                if email is None:
                    self.cursor.execute("""UPDATE customer
                                        SET name = %s, address = %s, cell_phone = %s, account_id_account = %s, email = NULL
                                        WHERE id_customer = %s""", (name, address, cellphone, self.id_account, id_customer))
                    
                else:
                    if "@" not in email or ".com" not in email or len(email) < 8:
                        messagebox.showerror(title="Email field", message="Please enter a valid email address.")
                        return
                    else:
                        self.cursor.execute("""UPDATE customer
                                            SET name = %s, address = %s, cell_phone = %s, account_id_account = %s, email = %s
                                            WHERE id_customer = %s""", (name, address, cellphone, self.id_account, email, id_customer))
                
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Customer: {name}, updated successfully!")
                log().info(f'User: "{self.__username}" updated the customer "{name}"')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def delete_customer(self, id_customer: int, customer_name: str):
        try:
            self.cursor.execute("DELETE FROM customer WHERE id_customer = %s", (id_customer,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" deleted the customer "{customer_name}"')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_customer(self, typed: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM customer WHERE name LIKE %s", ("%" + typed + "%",))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()
