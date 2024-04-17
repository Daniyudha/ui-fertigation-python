import customtkinter
from utils.clear_frame import clear_frame
from utils.validate_input import validate_input
import tkinter
from tkinter import ttk, messagebox
from database.db_product import Db_product
from database.db_category import Db_category
from database.connection.db_connection import Db_connection

class Ui_product:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        self.root.unbind("<Return>")

        clear_frame(self.square_frame)
        self.ui_widgets()
        self.product_data()

    def topbar(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Product")
        self.topbar_label.place(x=20, y=5)

        self.searchproducts_entry = customtkinter.CTkEntry(master=self.topbar_frame,
                                                           width=1227, height=35,
                                                           placeholder_text="Search by product name",
                                                           font=("arial", 17), 
                                                           fg_color="#EEEEEE", 
                                                           border_color="#e3e3e3", 
                                                           border_width=1)
        self.searchproducts_entry.place(x=174, y=8)

        self.searchproducts_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                             width=230, height=32,
                                                             corner_radius=4,
                                                             text_color="#ffffff",
                                                             font=("arial", 15), 
                                                             text="Search",
                                                             fg_color="#407ecf", 
                                                             hover_color="#6996d1",
                                                             command=lambda:self.search_product(self.searchproducts_entry.get()))
        self.searchproducts_button.place(x=1425, y=9)

        self.root.bind("<Return>", lambda _: self.searchproducts_button.invoke())
    
    def info_widgets(self):
        self.enabledproducts_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                            width=285, height=170,
                                                            corner_radius=8,
                                                            fg_color="#4bb34b")
        self.enabledproducts_frame.place(x=20, y=70)
        self.enabledproducts_label = customtkinter.CTkLabel(master=self.enabledproducts_frame,
                                                            font=("Arial", 21, "italic"),
                                                            text_color="#ffffff", 
                                                            text="Total Enabled Products")
        self.enabledproducts_label.place(x=20, y=15)
        self.totalenabled_label = customtkinter.CTkLabel(master=self.enabledproducts_frame,
                                                         font=("arial black", 25),
                                                         text_color="#ffffff", 
                                                         text=f"{Db_product(self.__username).totalproduct_rowstable('Enabled'):^26}")
        self.totalenabled_label.place(x=30, y=72)

        self.disabledproducts_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                             width=285, height=170,
                                                             corner_radius=8,
                                                             fg_color="#d64b4b")
        self.disabledproducts_frame.place(x=20, y=260)
        self.disabledproducts_label = customtkinter.CTkLabel(master=self.disabledproducts_frame,
                                                             font=("Arial", 21, "italic"),
                                                             text_color="#ffffff", 
                                                             text="Total Disabled Products")
        self.disabledproducts_label.place(x=20, y=15)
        self.totaldisabled_label = customtkinter.CTkLabel(master=self.disabledproducts_frame,
                                                          font=("arial black", 25),
                                                          text_color="#ffffff", 
                                                          text=f"{Db_product(self.__username).totalproduct_rowstable('Disabled'):^26}")
        self.totaldisabled_label.place(x=30, y=72)

        self.totalproducts_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                          width=285, height=170,
                                                          corner_radius=8,
                                                          fg_color="#407ecf")
        self.totalproducts_frame.place(x=20, y=450)
        self.totalproducts_label = customtkinter.CTkLabel(master=self.totalproducts_frame,
                                                          font=("Arial", 21, "italic"),
                                                          text_color="#ffffff", 
                                                          text="Total Products")
        self.totalproducts_label.place(x=20, y=15)
        self.total_label = customtkinter.CTkLabel(master=self.totalproducts_frame,
                                                  font=("arial black", 25),
                                                  text_color="#ffffff", 
                                                  text=f"{Db_connection().total_rowstable('product'):^26}")
        self.total_label.place(x=30, y=72)

    def ui_widgets(self):
        self.topbar()
        self.info_widgets()

        self.delproduct_button = customtkinter.CTkButton(master=self.square_frame,
                                                         width=230, height=32,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text_color="#ffffff",
                                                         text="Delete Product",
                                                         fg_color="#d54a49", 
                                                         hover_color="#d1706f",
                                                         command=self.delete_producttree)
        self.delproduct_button.place(x=905, y=868)

        self.updateproduct_button = customtkinter.CTkButton(master=self.square_frame,
                                                            width=230, height=32,
                                                            corner_radius=3,
                                                            font=("arial", 15),
                                                            text_color="#ffffff",
                                                            text="Update Product",
                                                            fg_color="#ec971f", 
                                                            hover_color="#f0b35d",
                                                            command=self.ui_updateproduct)
        self.updateproduct_button.place(x=1165, y=868)

        self.addproduct_button = customtkinter.CTkButton(master=self.square_frame,
                                                         width=230, height=32,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text_color="#ffffff",
                                                         text="Add Product",
                                                         fg_color="#4bb34b", 
                                                         hover_color="#7ebf7e",
                                                         command=self.ui_createproduct)
        self.addproduct_button.place(x=1425, y=868)

    def product_data(self):
        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        self.style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.product_treeview = ttk.Treeview(master=self.square_frame,
                                             height=28,
                                             style="style_treeview.Treeview",
                                             columns=("ID", "name", "sale price", 
                                                     "category", "status"),
                                             show="headings")
        self.product_treeview.place(x=325, y=50)

        self.product_treeview.heading("#1", text="ID", anchor="center")
        self.product_treeview.heading("#2", text="name", anchor="center")
        self.product_treeview.heading("#3", text="sale price", anchor="center")
        self.product_treeview.heading("#4", text="category", anchor="center")
        self.product_treeview.heading("#5", text="status", anchor="center")

        self.product_treeview.column("#1", minwidth=150, width=200, anchor="center")
        self.product_treeview.column("#2", minwidth=200, width=350, anchor="center")
        self.product_treeview.column("#3", minwidth=100, width=250, anchor="center")
        self.product_treeview.column("#4", minwidth=240, width=290, anchor="center")
        self.product_treeview.column("#5", minwidth=100, width=250, anchor="center")

        self.treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=self.product_treeview.yview)
        self.product_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=1660, y=50, height=808)

        self.read_products()

    def ui_createproduct(self):
        clear_frame(self.square_frame)

        self.topbar()
        self.topbar_label.configure(text="Add Product")
        self.searchproducts_entry.destroy()
        self.searchproducts_button.destroy()

        self.frame_one = customtkinter.CTkFrame(master=self.square_frame,
                                                width=1668, height=540,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=5, y=55)

        self.id_label = customtkinter.CTkLabel(master=self.frame_one,
                                               font=("arial bold", 17),
                                               text_color="#2e2e2e",
                                               text="ID:")
        self.id_label.place(x=25, y=25)
        
        validation = self.root.register(validate_input)

        self.id_entry = customtkinter.CTkEntry(master=self.frame_one,
                                               width=1618, height=35,
                                               validate="key", 
                                               validatecommand=(validation, "%P"),
                                               corner_radius=3, 
                                               font=("arial", 17), 
                                               border_color="#e3e3e3", 
                                               border_width=1)
        self.id_entry.place(x=25, y=62)

        self.productname_label = customtkinter.CTkLabel(master=self.frame_one,
                                                        font=("arial bold", 17),
                                                        text_color="#2e2e2e",
                                                        text="Product name:")
        self.productname_label.place(x=25, y=120)

        self.productname_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                        width=1618, height=35,
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        self.productname_entry.place(x=25, y=160)

        self.saleprice_label = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("arial bold", 17),
                                                      text_color="#2e2e2e",
                                                      text="Sale price:")
        self.saleprice_label.place(x=25, y=215)

        self.saleprice_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                      width=1618, height=35,
                                                      corner_radius=3, 
                                                      font=("arial", 17),
                                                      border_color="#e3e3e3", 
                                                      border_width=1)
        self.saleprice_entry.place(x=25, y=255)

        self.status_label = customtkinter.CTkLabel(master=self.frame_one,
                                                   font=("arial bold", 17),
                                                   text_color="#2e2e2e",
                                                   text="Status:")
        self.status_label.place(x=25, y=405)

        self.status_optionmenu = customtkinter.CTkOptionMenu(master=self.frame_one,
                                                             width=1618, height=35,
                                                             corner_radius=4,
                                                             fg_color="#f2f2f2",
                                                             text_color="#2e2e2e",
                                                             font=("arial", 17),
                                                             dropdown_font=("arial", 15),
                                                             button_color="#818285",
                                                             button_hover_color="#636466",
                                                             values=["Enabled", "Disabled"])
        self.status_optionmenu.place(x=25, y=445)
        self.status_optionmenu.set("Enabled")

        self.category_label = customtkinter.CTkLabel(master=self.frame_one,
                                                     font=("arial bold", 17),
                                                     text_color="#2e2e2e",
                                                     text="Category:")
        self.category_label.place(x=25, y=310)

        self.category_optionmenu = customtkinter.CTkOptionMenu(master=self.frame_one,
                                                               width=1618, height=35,
                                                               corner_radius=4,
                                                               fg_color="#f2f2f2",
                                                               text_color="#2e2e2e",
                                                               font=("arial", 17),
                                                               dropdown_font=("arial", 15),
                                                               button_color="#818285",
                                                               button_hover_color="#636466",
                                                               values=self.read_categories())
        self.category_optionmenu.place(x=25, y=350)

        self.divider_frame = tkinter.Frame(master=self.square_frame, 
                                           height=1, width=1678, 
                                           bg="#dbdbdb")
        self.divider_frame.place(x=0, y=855)

        self.addproduct_button = customtkinter.CTkButton(master=self.square_frame,
                                                         width=230, height=32,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text_color="#ffffff",
                                                         text="Add Product",
                                                         fg_color="#4bb34b", 
                                                         hover_color="#7ebf7e",
                                                         command=self.create_producttree)
        self.addproduct_button.place(x=1165, y=868)

        self.root.bind("<Return>", lambda _: self.addproduct_button.invoke())

        self.cancel_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.toback)
        self.cancel_button.place(x=1425, y=868)

    def ui_updateproduct(self):
        if self.selected() == False:
            return

        clear_frame(self.square_frame)

        self.topbar()
        self.topbar_label.configure(text="Update Product")
        self.searchproducts_entry.destroy()
        self.searchproducts_button.destroy()

        self.frame_one = customtkinter.CTkFrame(master=self.square_frame,
                                                width=1668, height=540,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=5, y=55)

        self.id_label = customtkinter.CTkLabel(master=self.frame_one,
                                               font=("arial bold", 17),
                                               text_color="#2e2e2e",
                                               text="ID:")
        self.id_label.place(x=25, y=25)

        validation = self.root.register(validate_input)

        self.id_entry = customtkinter.CTkEntry(master=self.frame_one,
                                               width=1618, height=35,
                                               validate="key", 
                                               validatecommand=(validation, "%P"),
                                               corner_radius=3, 
                                               font=("arial", 17), 
                                               border_color="#e3e3e3", 
                                               border_width=1)
        self.id_entry.place(x=25, y=62)

        self.productname_label = customtkinter.CTkLabel(master=self.frame_one,
                                                        font=("arial bold", 17),
                                                        text_color="#2e2e2e",
                                                        text="Product name:")
        self.productname_label.place(x=25, y=120)

        self.productname_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                        width=1618, height=35,
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        self.productname_entry.place(x=25, y=160)

        self.saleprice_label = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("arial bold", 17),
                                                      text_color="#2e2e2e",
                                                      text="Sale price:")
        self.saleprice_label.place(x=25, y=215)

        self.saleprice_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                      width=1618, height=35,
                                                      corner_radius=3, 
                                                      font=("arial", 17),
                                                      border_color="#e3e3e3", 
                                                      border_width=1)
        self.saleprice_entry.place(x=25, y=255)

        self.status_label = customtkinter.CTkLabel(master=self.frame_one,
                                                   font=("arial bold", 17),
                                                   text_color="#2e2e2e",
                                                   text="Status:")
        self.status_label.place(x=25, y=405)

        self.status_optionmenu = customtkinter.CTkOptionMenu(master=self.frame_one,
                                                             width=1618, height=35,
                                                             corner_radius=4,
                                                             fg_color="#f2f2f2",
                                                             text_color="#2e2e2e",
                                                             font=("arial", 17),
                                                             dropdown_font=("arial", 15),
                                                             button_color="#818285",
                                                             button_hover_color="#636466",
                                                             values=["Enabled", "Disabled"])
        self.status_optionmenu.place(x=25, y=445)
        self.status_optionmenu.set("Enabled")

        self.category_label = customtkinter.CTkLabel(master=self.frame_one,
                                                     font=("arial bold", 17),
                                                     text_color="#2e2e2e",
                                                     text="Category:")
        self.category_label.place(x=25, y=310)

        self.category_optionmenu = customtkinter.CTkOptionMenu(master=self.frame_one,
                                                               width=1618, height=35,
                                                               corner_radius=4,
                                                               fg_color="#f2f2f2",
                                                               text_color="#2e2e2e",
                                                               font=("arial", 17),
                                                               dropdown_font=("arial", 15),
                                                               button_color="#818285",
                                                               button_hover_color="#636466",
                                                               values=self.read_categories())
        self.category_optionmenu.place(x=25, y=350)

        self.divider_frame = tkinter.Frame(master=self.square_frame, 
                                           height=1, width=1678, 
                                           bg="#dbdbdb")
        self.divider_frame.place(x=0, y=855)

        self.updateproduct_button = customtkinter.CTkButton(master=self.square_frame,
                                                            width=230, height=32,
                                                            corner_radius=3,
                                                            font=("arial", 15),
                                                            text_color="#ffffff",
                                                            text="Save Changes",
                                                            fg_color="#4bb34b", 
                                                            hover_color="#7ebf7e",
                                                            command=self.update_producttree)
        self.updateproduct_button.place(x=1165, y=868)
    
        self.cancel_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.toback)
        self.cancel_button.place(x=1425, y=868)

        self.bring_productdata()

        self.root.bind("<Return>", lambda _: self.updateproduct_button.invoke())
    
    def create_producttree(self):
        categories = Db_category(self.__username).read_category()
        id_category = int()

        for i in categories:
            if i[1] == self.category_optionmenu.get():
                id_category = i[0]

        action = Db_product(self.__username).create_product(id_product=self.id_entry.get(),
                                                            product_name=self.productname_entry.get(),
                                                            sale_price=self.saleprice_entry.get(),
                                                            id_category=id_category,
                                                            status=self.status_optionmenu.get())
        if action:
            self.toback()

    def read_products(self):
        self.product_treeview.delete(*self.product_treeview.get_children())

        __all_product = Db_product(self.__username).read_product(show_disabled=True)
        
        self.product_treeview.tag_configure("hexgray", background="#ededed")
        self.product_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for p in __all_product:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.product_treeview.insert("", "end", values=p, tags=tag)

    def update_producttree(self):
        categories = Db_category(self.__username).read_category()
        id_category = int()

        for i in categories:
            if i[1] == self.category_optionmenu.get():
                id_category = i[0]

        update_productnow = Db_product(self.__username).update_product(new_id=self.id_entry.get(),
                                                                       new_productname=self.productname_entry.get(),
                                                                       new_saleprice=self.saleprice_entry.get(),
                                                                       new_idcategory=id_category,
                                                                       new_status=self.status_optionmenu.get(),
                                                                       old_id= self.selected_product[0])

        if update_productnow:
            self.toback()

    def delete_producttree(self):
        if self.selected() == False:
            return
        
        message = f"Are you sure you want to delete\nthe product: {self.selected_product[1]}."
        modal = messagebox.askyesno(title=f"id product: {self.selected_product[0]}", message=message)
        
        if modal == True:
            Db_product(self.__username).delete_product(id_product=self.selected_product[0], product_name=self.selected_product[1])
            self.product_treeview.delete(self.product_treeview.selection()[0])

            frames = [self.enabledproducts_frame, self.totalproducts_frame, self.disabledproducts_frame]
            for fr in frames:
                fr.destroy()
  
            self.info_widgets()

    def search_product(self, typed: str):
        self.product_treeview.delete(*self.product_treeview.get_children())
  
        product = Db_product(self.__username).search_products_likename(typed=typed)

        tag = "hexwhite"
        for p in product:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.product_treeview.insert("", "end", values=p, tags=tag)

    def selected(self) -> bool:
        try:
            self.selected_product = self.product_treeview.item(self.product_treeview.selection()[0], "values")
        except IndexError:
            messagebox.showerror(title=None, message="Please select a product")
            return False
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
            return False
        
    def read_categories(self) -> list:
        categories = Db_category(self.__username).read_category()
        aux = []

        for i in categories:
            aux.append(i[1])
        return aux
    
    def bring_productdata(self):
        list_entries = [self.id_entry, self.productname_entry, self.saleprice_entry]
        for k, v in enumerate(list_entries):
            v.insert(0, self.selected_product[k])
        
        self.category_optionmenu.set(self.selected_product[3])
        self.status_optionmenu.set(self.selected_product[4])

    def toback(self):
        clear_frame(self.square_frame)
        self.ui_widgets()
        self.product_data()
