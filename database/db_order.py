from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_order(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()
    
    def create_order(self, id_waiter: int, id_customer: int=None, *id_products):
        self.__entry_items = {"waiter": id_waiter}
        if not empty_entries(**self.__entry_items):
            try:
                if id_customer:
                    self.cursor.execute("""INSERT INTO `order` (waiter_id_waiter, customer_id_customer)
                                        VALUES (%s, %s);""", (id_waiter, id_customer))
                else:
                    self.cursor.execute("""INSERT INTO `order` (waiter_id_waiter) 
                                        VALUES (%s);""", (id_waiter,))
                self.mysql_connection.commit()
                
                id_order = self.cursor.lastrowid
                
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                log().info(f'User: "{self.__username}" created order {id_order}')
                self.add_productto_order(id_order, *id_products)
                return id_order
            finally:
                self.cursor.close()
                self.mysql_connection.close

    def add_productto_order(self, id_order, *id_products):
        try:
            count = {}
            for id_product in id_products:
                if id_product in count:
                    count[id_product] += 1
                else:
                    count[id_product] = 1
            
            duplicates = {}
            for id_product, quantity in count.items():
                if quantity > 1:
                    duplicates[id_product] = quantity
                else:
                    duplicates[id_product] = 1
            
            for id_product, quantity in duplicates.items():
                self.cursor.execute("""INSERT INTO order_has_product (order_id_order, product_id_product, quantity)
                                    VALUES (%s, %s, %s);""", (id_order, id_product, quantity))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            if id_products:
                log().info(f'User: "{self.__username}" added the products: {id_products} in order {id_order}')
            else:
                log().info(f'User: "{self.__username}" started the order {id_order} without product')
        finally:
            self.cursor.close()
            self.mysql_connection.close
    
    def update_order_has_product(self, id_order, *product_quantity):
        try:
            for pr_qt in product_quantity:
                self.cursor.execute("""UPDATE order_has_product
                                    SET quantity = %s
                                    WHERE order_id_order = %s
                                    AND product_id_product = %s;""", (pr_qt[1], id_order, pr_qt[0]))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" updated the products {product_quantity} in order {id_order}')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def delete_order_has_product(self, id_order, *id_product):
        try:
            for prod in id_product:
                self.cursor.execute("""DELETE FROM order_has_product 
                                    WHERE order_id_order = %s
                                    AND product_id_product = %s""", (id_order, prod))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            log().info(f'User: "{self.__username}" deleted the products {id_product}')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def order_has_product(self, id_order) -> list:
        try:
            self.cursor.execute("""SELECT product_id_product, quantity FROM order_has_product
                                WHERE order_id_order = %s;""", (id_order,))
            return self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()
