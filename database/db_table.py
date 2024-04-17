from database.connection.db_connection import Db_connection
from tkinter import messagebox
from utils.log import log

class Db_table(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()
    
    def create_table(self, id_table:int=None) -> True:
        try:
            if id_table:
                self.cursor.execute("INSERT INTO `table` (id_table) VALUES (%s);", (id_table,))
            else:
                self.cursor.execute("INSERT INTO `table` (id_table) VALUES (NULL);")
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" created a table')
            return True
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def read_table(self) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT * FROM `table`
                                order by id_table""")
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def read_id_order_table(self, id_table) -> int:
        try:
            self.cursor.execute("""SELECT order_id_order FROM `table`
                                WHERE id_table = %s""", (id_table,))
            return self.cursor.fetchone()[0]
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def update_order_table(self, id_table, id_order):
        try:
            self.cursor.execute("""UPDATE `table`
                                SET order_id_order = %s
                                WHERE id_table = %s;""", (id_order, id_table))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def delete_table(self, id_table):
        try:
            self.cursor.execute("""DELETE FROM `table`
                                WHERE id_table = %s""", (id_table,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" deleted table {id_table}')
            messagebox.showinfo(title=None, message=f"Table deleted successfully!")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def sum_values_table(self) -> list:
        try:
            self.cursor.execute(f"""SELECT `table`.id_table, `table`.order_id_order, SUM(product.sale_price * order_has_product.quantity) AS total_price
                                FROM `table`
                                LEFT JOIN `order` ON `table`.order_id_order = `order`.id_order
                                LEFT JOIN order_has_product ON `order`.id_order = order_has_product.order_id_order
                                LEFT JOIN product ON order_has_product.product_id_product = product.id_product
                                GROUP BY `table`.id_table, `table`.order_id_order
                                ORDER BY `table`.id_table;""")
            return self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def table_waiter(self, id_table: int):
        try:
            self.cursor.execute("""SELECT waiter.`name`
                                FROM `table`
                                JOIN `order` ON `table`.order_id_order = `order`.id_order
                                JOIN waiter ON `order`.waiter_id_waiter = waiter.id_waiter
                                WHERE `table`.id_table = %s;""", (id_table,))
            return self.cursor.fetchone()[0]
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def table_customer(self, id_table) -> True:
        try:
            self.cursor.execute("""SELECT customer.name
                                FROM `table`
                                JOIN `order` ON `table`.order_id_order = `order`.id_order
                                JOIN customer ON `order`.customer_id_customer = customer.id_customer
                                WHERE `table`.id_table = %s;""", (id_table,))
            return self.cursor.fetchone()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def remove_customer_table(self, id_table: int, id_order: int, payment: float):
        try:
            self.cursor.execute("""UPDATE `table`
                                SET order_id_order = %s
                                WHERE id_table = %s""", (None, id_table))
            
            self.cursor.execute("""UPDATE `order`
                                SET end_time = NOW(), payment = %s
                                WHERE id_order = %s;""", (payment, id_order))

            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" finished the table {id_table}')
            return True
        finally:
            self.cursor.close()
            self.mysql_connection.close()
