from database.connection.db_connection import Db_connection
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.log import log

class Db_product(Db_connection):
    def __init__(self, username):
        super().__init__()
        self.__username = username

        self.db_connected()

    def create_product(self, id_product, product_name, sale_price, id_category, status):
        self.__entry_items = {"id product": id_product, 
                              "product name": product_name, 
                              "sale price": sale_price,
                              "id category": id_category,
                              "status": status}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""INSERT INTO product (id_product, product_name, sale_price, category_id_category, status) 
                                    VALUES (%s, %s, %s, %s, %s);""", (id_product, product_name, sale_price, id_category, status))
                self.mysql_connection.commit()
            except Exception as error:
                if "Incorrect integer value" in str(error):
                    messagebox.showerror(title="ID", message=f"Enter an integer value!")
                elif "Duplicate entry" in str(error):
                    messagebox.showerror(title="ID", message=f"ID already exists, try another one.")
                else:
                    messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Product: {product_name}, successfully registered.")
                log().info(f'User: "{self.__username}" created the "{product_name}" product')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close

    def read_product(self, show_disabled:bool=False) -> list[tuple]:
        try:
            self.cursor.execute("""SELECT PRODUCT.id_product, 
                                PRODUCT.product_name, 
                                PRODUCT.sale_price, 
                                CATEGORY.category_name, 
                                PRODUCT.`status`
                                FROM PRODUCT
                                JOIN CATEGORY ON PRODUCT.category_id_category = CATEGORY.id_category
                                WHERE `status` != %s
                                ORDER BY id_product""", (f'{"Disabled" if show_disabled == False else None}',))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def update_product(self, new_id, new_productname, new_saleprice, new_idcategory, new_status, old_id):
        self.__entry_items = {"id product": new_id, 
                              "product name": new_productname, 
                              "sale price": new_saleprice,
                              "id category": new_idcategory,
                              "status": new_status}
        if not empty_entries(**self.__entry_items):
            try:
                self.cursor.execute("""UPDATE product
                                    SET id_product = %s, product_name = %s, sale_price = %s, category_id_category = %s, status = %s
                                    WHERE id_product = %s""", (new_id, new_productname, new_saleprice, new_idcategory, new_status, old_id))
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                messagebox.showinfo(title=None, message=f"Product: {new_productname}, updated successfully!")
                log().info(f'User: "{self.__username}" updated the "{new_productname}" product')
                return True
            finally:
                self.cursor.close()
                self.mysql_connection.close()

    def delete_product(self, id_product: int, product_name: str):
        try:
            self.cursor.execute("DELETE FROM product WHERE id_product = %s", (id_product,))
            self.mysql_connection.commit()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            messagebox.showinfo(title=None, message=f"{product_name.capitalize()} Product successfully deleted")
            log().info(f'User: "{self.__username}" deleted the "{product_name}" product')
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_products_likename(self, typed: str) -> str:
        try:
            self.cursor.execute("""SELECT PRODUCT.id_product, 
                                PRODUCT.product_name, 
                                PRODUCT.sale_price, 
                                CATEGORY.category_name, 
                                PRODUCT.`status`
                                FROM PRODUCT
                                JOIN CATEGORY ON PRODUCT.category_id_category = CATEGORY.id_category
                                WHERE product_name LIKE %s
                                ORDER BY id_product;""", ('%' + typed + '%',))
            self.result = self.cursor.fetchall()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_product_tableid(self, id_product: int) -> list:
        try:
            self.cursor.execute("""SELECT * from product
                                WHERE id_product = %s""", (id_product,))
            self.result = self.cursor.fetchall()[0]
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def search_product_tablename(self, product_name):
        try:
            self.cursor.execute("""SELECT PRODUCT.id_product, 
                                PRODUCT.product_name, 
                                PRODUCT.sale_price, 
                                CATEGORY.category_name, 
                                PRODUCT.`status`
                                FROM PRODUCT
                                JOIN CATEGORY ON PRODUCT.category_id_category = CATEGORY.id_category
                                WHERE product_name = %s
                                ORDER BY id_product;""", (product_name,))
            self.result = self.cursor.fetchone()
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
        else:
            return self.result
        finally:
            self.cursor.close()
            self.mysql_connection.close()

    def totalproduct_rowstable(self, status:str) -> int:
        try:
            self.cursor.execute("""SELECT COUNT(*) FROM product
                                WHERE status = %s""", (status,))
            result = self.cursor.fetchall()[0][0]
            return result
        except Exception as error:
            messagebox.showerror("Error", f"Error: {error}")
        finally:
            self.cursor.close()
            self.mysql_connection.close()
