import customtkinter
from utils.validate_input import validate_input
from utils.clear_frame import clear_frame
import tkinter
from database.db_table import Db_table
from database.db_waiter import Db_waiter
from database.db_customer import Db_customer
from database.db_product import Db_product
from database.db_order import Db_order
from tkinter import ttk, messagebox, filedialog
from PIL import Image
import copy
import os

class Ui_table:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame
        self.root.unbind("<Return>")

        clear_frame(self.square_frame)
        self.ui_images()
        self.ui_widgets()

    def ui_images(self):
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.productpil_image = Image.open("images/tables_images/product.png")
        self.product_image = customtkinter.CTkImage(dark_image=self.productpil_image,
                                                    light_image=self.productpil_image,
                                                    size=(47,47))
        
        self.pricepil_image = Image.open("images/tables_images/price.png")
        self.price_image = customtkinter.CTkImage(dark_image=self.pricepil_image,
                                                  light_image=self.pricepil_image,
                                                  size=(47,47))
        
        self.paymentpil_image = Image.open("images/tables_images/payment.png")
        self.payment_image = customtkinter.CTkImage(dark_image=self.paymentpil_image,
                                                    light_image=self.paymentpil_image,
                                                    size=(47,47))
        
        self.changepil_image = Image.open("images/tables_images/change.png")
        self.change_image = customtkinter.CTkImage(dark_image=self.changepil_image,
                                                   light_image=self.changepil_image,
                                                   size=(47,47))

    def topbar(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Tables")
        self.topbar_label.place(x=20, y=5)

        self.redstatus_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                      width=30, height=30,
                                                      corner_radius=100,
                                                      fg_color="#d54a49",
                                                      bg_color="#dcdcdc",
                                                      border_color="#dcdcdc")
        self.redstatus_frame.place(x=245, y=9)
        self.redstatus_label = customtkinter.CTkLabel(master=self.square_frame,
                                                      text_color="#404040",
                                                      text="Occupied",
                                                      bg_color="#dcdcdc",
                                                      font=("arial", 17))
        self.redstatus_label.place(x=285, y=9)

        self.greenstatus_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                        width=30, height=30,
                                                        corner_radius=100,
                                                        fg_color="#4bb34b",
                                                        bg_color="#dcdcdc",
                                                        border_color="#dcdcdc")
        self.greenstatus_frame.place(x=445, y=9)
        self.greenstatus_label = customtkinter.CTkLabel(master=self.square_frame,
                                                        text_color="#404040",
                                                        text="Unoccupied",
                                                        bg_color="#dcdcdc",
                                                        font=("arial", 17))
        self.greenstatus_label.place(x=485, y=9)

        self.deletetable_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                          width=197, height=32,
                                                          corner_radius=4,
                                                          text_color="#ffffff",
                                                          font=("arial", 15), 
                                                          text="Delete Table",
                                                          fg_color="#d54a49", 
                                                          hover_color="#d1706f",
                                                          command=self.ui_delete_table)
        self.deletetable_button.place(x=1250, y=9)

        self.addtable_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                       width=197, height=32,
                                                       corner_radius=4,
                                                       text_color="#ffffff",
                                                       font=("arial", 15), 
                                                       text="Add Table",
                                                       fg_color="#4bb34b", 
                                                       hover_color="#7ebf7e",
                                                       command=self.ui_add_table)
        self.addtable_button.place(x=1455, y=9)

    def ui_widgets(self):
        self.topbar()

        self.subsquare_frame = customtkinter.CTkFrame(master=self.square_frame, width=1678, height=962)
        self.subsquare_frame.place(x=0, y=50)

        self.tables_canvas = tkinter.Canvas(master=self.subsquare_frame, width=1678, height=858)
        self.tables_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        self.tables_scrollbar = tkinter.Scrollbar(master=self.subsquare_frame, 
                                                  orient=tkinter.VERTICAL, 
                                                  command=self.tables_canvas.yview)
        self.tables_scrollbar.place(x=1660, y=0, height=858)

        self.tables_canvas.configure(yscrollcommand=self.tables_scrollbar.set)
        self.tables_canvas.bind("<Configure>", lambda _: self.tables_canvas.configure(scrollregion=self.tables_canvas.bbox("all")))

        self.window_frame = tkinter.Frame(master=self.tables_canvas)
        self.tables_canvas.create_window((0,0), window=self.window_frame, anchor="nw")

        tables_values = Db_table(self.__username).sum_values_table()
        table_row = table_column = 0

        for tab_va in tables_values:
            table_button = customtkinter.CTkButton(master=self.window_frame,
                                                   width=197, height=140,
                                                   font=("arial bold", 20),
                                                   fg_color= "#d64b4b" if tab_va[1] else "#4bb34b", 
                                                   hover_color= "#ab3c3c" if tab_va[1] else "#3f993f",
                                                   text=f"{tab_va[0]}\n\n{tab_va[2]}" if tab_va[2] else tab_va[0],
                                                   command=lambda _= tab_va[0]:self.ui_table_data(id_table=_)
                                                   )
            table_button.grid(row=table_row, column=table_column, padx=5, pady=5)

            if table_button.cget("fg_color") == "#d64b4b":
                table_button.configure(command=lambda _= tab_va[0]: self.ui_orders(id_table=_))
            
            table_column += 1
            if table_column == 8:
                table_row += 1
                table_column = 0

    def ui_add_table(self):
        try:
            self.table_toplevel.destroy()
        except:
            pass

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Add Total Tables")
        self.table_toplevel.geometry("390x80+760+25")
        self.table_toplevel.resizable(False, False)
        
        tabview = customtkinter.CTkTabview(master=self.table_toplevel,
                                           width=390, height=90,
                                           corner_radius=0,
                                           bg_color="#ffffff")
        tabview.place(x=0, y=-10)
        tabview.add("ID")
        tabview.add("Quantity")
        tabview.tab("ID")
        tabview.tab("Quantity")

        validation = self.root.register(validate_input)

        idtable_entry = customtkinter.CTkEntry(master=tabview.tab("ID"),
                                               width=225, height=30,
                                               validate="key",
                                               validatecommand=(validation, "%P"),
                                               corner_radius=0,
                                               font=("arial", 17), 
                                               fg_color="#ffffff", 
                                               border_color="#b5b3b3", 
                                               border_width=1)
        idtable_entry.place(x=5, y=7)

        customtkinter.CTkButton(master=tabview.tab("ID"),
                                width=150, height=30,
                                corner_radius=4,
                                text_color="#ffffff",
                                font=("arial", 15), 
                                text="Add Table",
                                fg_color="#4bb34b", 
                                hover_color="#7ebf7e",
                                command=lambda:self.add_id_table(id_table=int(idtable_entry.get()))).place(x=235, y=7)
        
        addtable_spinbox = tkinter.Spinbox(master=tabview.tab("Quantity"),
                                           width=17,
                                           validate="key",
                                           validatecommand=(validation, "%P"),
                                           font=("arial bold", 16),
                                           from_=0, to=100)
        addtable_spinbox.place(x=5, y=7)

        customtkinter.CTkButton(master=tabview.tab("Quantity"),
                                width=150, height=30,
                                corner_radius=4,
                                text_color="#ffffff",
                                font=("arial", 15), 
                                text="Add Table",
                                fg_color="#4bb34b", 
                                hover_color="#7ebf7e",
                                command=lambda:self.add_table(int(addtable_spinbox.get()))).place(x=235, y=7)

    def ui_delete_table(self):
        try:
            self.table_toplevel.destroy()
        except:
            pass

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Delete Table")
        self.table_toplevel.geometry("395x55+760+35")
        self.table_toplevel.resizable(False, False)
        
        deletetable_optionmenu = customtkinter.CTkOptionMenu(master=self.table_toplevel,
                                                             width=230, height=30,
                                                             corner_radius=4,
                                                             fg_color="#fafafa",
                                                             bg_color="#d9d9d9",
                                                             text_color="#2e2e2e",
                                                             font=("arial", 17),
                                                             dropdown_font=("arial", 15),
                                                             button_color="#818285",
                                                             button_hover_color="#636466",
                                                             values=self.read_data("table"))
        deletetable_optionmenu.grid(row=0, column=0, padx=5, pady=12)
        
        customtkinter.CTkButton(master=self.table_toplevel,
                                width=150, height=30,
                                corner_radius=4,
                                text_color="#ffffff",
                                font=("arial", 15), 
                                text="Delete Table",
                                fg_color="#d54a49", 
                                hover_color="#d1706f",
                                command=lambda:self.remove_table(id_table=deletetable_optionmenu.get())).grid(row=0, column=1)

    def ui_table_data(self, id_table: int):
        try:
            self.table_toplevel.destroy()
        except:
            pass

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Table Data")
        self.table_toplevel.geometry("300x250+815+390")
        self.table_toplevel.resizable(False, False)

        number_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                              font=("arial bold", 17),
                                              text_color="#2e2e2e",
                                              text="Number:")
        number_label.place(x=25, y=10)

        number_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                              width=250, height=35,
                                              corner_radius=3,
                                              border_width=1, 
                                              font=("arial", 17),
                                              fg_color="#e3e3e3", 
                                              border_color="#ffffff")
        number_entry.place(x=25, y=47)
        number_entry.insert(0, id_table)
        number_entry.configure(state="disabled")

        waiter_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                              font=("arial bold", 17),
                                              text_color="#2e2e2e",
                                              text="Waiter:")
        waiter_label.place(x=25, y=95)

        waiter_optionmenu = customtkinter.CTkOptionMenu(master=self.table_toplevel,
                                                        width=250, height=35,
                                                        corner_radius=4,
                                                        fg_color="#fafafa",
                                                        bg_color="#d9d9d9",
                                                        text_color="#2e2e2e",
                                                        font=("arial", 17),
                                                        dropdown_font=("arial", 15),
                                                        button_color="#818285",
                                                        button_hover_color="#636466",
                                                        values=self.read_data("waiters"))
        waiter_optionmenu.place(x=25, y=132)

        order_button = customtkinter.CTkButton(master=self.table_toplevel,
                                               width=250, height=32,
                                               corner_radius=4,
                                               text_color="#ffffff",
                                               font=("arial", 15), 
                                               text="Order",
                                               fg_color="#4bb34b", 
                                               hover_color="#7ebf7e",
                                               command=lambda:self.ui_initial_order(id_table=id_table, waiter=waiter_optionmenu.get()))
        order_button.place(x=25, y=195)
    
    def ui_initial_order(self, id_table:int, waiter:str):
        self.table_toplevel.destroy()

        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Order")
        self.table_toplevel.geometry("669x669+625+225")
        self.table_toplevel.resizable(False, False)

        id_table_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                font=("arial bold", 17),
                                                text_color="#2e2e2e",
                                                text="Table:")
        id_table_label.place(x=25, y=10)

        id_table_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                width=150, height=35,
                                                corner_radius=3,
                                                border_width=1, 
                                                font=("arial", 17),
                                                fg_color="#e3e3e3", 
                                                border_color="#ffffff")
        id_table_entry.place(x=25, y=47)
        id_table_entry.insert(0, id_table)
        id_table_entry.configure(state="disabled")

        waiter_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                              font=("arial bold", 17),
                                              text_color="#2e2e2e",
                                              text="Waiter:")
        waiter_label.place(x=194, y=10)

        waiter_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                              width=450, height=35,
                                              corner_radius=3,
                                              border_width=1, 
                                              font=("arial", 17),
                                              fg_color="#e3e3e3", 
                                              border_color="#ffffff")
        waiter_entry.place(x=194, y=47)
        waiter_entry.insert(0, waiter)
        waiter_entry.configure(state="disabled")

        customer_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                font=("arial bold", 17),
                                                text_color="#2e2e2e",
                                                text="Customer:")
        customer_label.place(x=25, y=95)

        customer_optionmenu = customtkinter.CTkOptionMenu(master=self.table_toplevel,
                                                          width=619, height=35,
                                                          corner_radius=4,
                                                          fg_color="#fafafa",
                                                          bg_color="#d9d9d9",
                                                          text_color="#2e2e2e",
                                                          font=("arial", 17),
                                                          dropdown_font=("arial", 15),
                                                          button_color="#818285",
                                                          button_hover_color="#636466",
                                                          values=self.read_data("customers"))
        customer_optionmenu.place(x=25, y=132)

        products_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                font=("arial bold", 17),
                                                text_color="#2e2e2e",
                                                text="Products:")
        products_label.place(x=25, y=180)

        self.product_optionmenu = customtkinter.CTkOptionMenu(master=self.table_toplevel,
                                                              width=300, height=35,
                                                              corner_radius=4,
                                                              fg_color="#fafafa",
                                                              bg_color="#d9d9d9",
                                                              text_color="#2e2e2e",
                                                              font=("arial", 17),
                                                              dropdown_font=("arial", 15),
                                                              button_color="#818285",
                                                              button_hover_color="#636466",
                                                              values=self.read_data("products"))
        self.product_optionmenu.place(x=25, y=214)

        self.total_spinbox = tkinter.Spinbox(master=self.table_toplevel,
                                             width=3,
                                             font=("arial", 19),
                                             from_=1, to=100)
        self.total_spinbox.place(x=336, y=215)

        add_button = customtkinter.CTkButton(master=self.table_toplevel,
                                             width=100, height=35,
                                             corner_radius=4,
                                             text_color="#ffffff",
                                             font=("arial", 15), 
                                             text="Add to list",
                                             fg_color="#4bb34b", 
                                             hover_color="#7ebf7e",
                                             command=self.add_tolist)
        add_button.place(x=410, y=214)

        remove_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                width=100, height=35,
                                                corner_radius=4,
                                                text_color="#ffffff",
                                                font=("arial", 15), 
                                                text="Remove selected",
                                                fg_color="#d54a49", 
                                                hover_color="#d1706f",
                                                command=self.remove_selected)
        remove_button.place(x=520, y=214)

        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        self.style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.products_treeview = ttk.Treeview(master=self.table_toplevel,
                                              height=8,
                                              style="style_treeview.Treeview",
                                              columns=("ID", "product", "sale price", "category"),
                                              show="headings")
        self.products_treeview.place(x=25, y=260)

        self.products_treeview.heading("#1", text="ID", anchor="center")
        self.products_treeview.heading("#2", text="product", anchor="center")
        self.products_treeview.heading("#3", text="sale price", anchor="center")
        self.products_treeview.heading("#4", text="category", anchor="center")

        self.products_treeview.column("#1", minwidth=50, width=70, anchor="center")
        self.products_treeview.column("#2", minwidth=100, width=260, anchor="center")
        self.products_treeview.column("#3", minwidth=100, width=130, anchor="w")
        self.products_treeview.column("#4", minwidth=100, width=150, anchor="w")

        self.treeview_scrollbar = tkinter.Scrollbar(master=self.table_toplevel, orient=tkinter.VERTICAL, command=self.products_treeview.yview)
        self.products_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=627, y=260, height=248)


        squarestatus_frame = customtkinter.CTkFrame(master=self.table_toplevel,
                                                    width=619,
                                                    height=90,
                                                    fg_color="#ffffff")
        squarestatus_frame.place(x=25, y=520)

        self.total_products = self.sale_price = 0
        
        productimage_label = customtkinter.CTkLabel(master=squarestatus_frame,text="", image=self.product_image)
        productimage_label.place(x=25, y=22)
        totalproduct_label = customtkinter.CTkLabel(master=squarestatus_frame, font=("arial", 17), text_color="#383838", text="Total products:")
        totalproduct_label.place(x=95, y=10)
        self.totalproduct_stringvar = customtkinter.StringVar()
        totalproductstringvar_label = customtkinter.CTkLabel(master=squarestatus_frame, font=("arial", 19), text_color="#383838", textvariable=self.totalproduct_stringvar)
        totalproductstringvar_label.place(x=140, y=36)


        divider_frame = tkinter.Frame(master=squarestatus_frame, height=70, width=1)
        divider_frame.place(x=309, y=10)


        salepriceimage_label = customtkinter.CTkLabel(master=squarestatus_frame,text="", image=self.price_image)
        salepriceimage_label.place(x=334, y=22)
        saleprice_label = customtkinter.CTkLabel(master=squarestatus_frame, font=("arial", 17), text_color="#383838", text="Total price:")
        saleprice_label.place(x=404, y=10)
        self.saleprice_stringvar = customtkinter.StringVar()
        salepricestringvar_label = customtkinter.CTkLabel(master=squarestatus_frame, font=("arial", 19), text_color="#383838", textvariable=self.saleprice_stringvar)
        salepricestringvar_label.place(x=449, y=36)


        start_order_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                     width=230, height=32,
                                                     corner_radius=4,
                                                     text_color="#ffffff",
                                                     font=("arial", 15), 
                                                     text="Start order",
                                                     fg_color="#4bb34b", 
                                                     hover_color="#7ebf7e",
                                                     command=lambda:self.start_order(id_table=id_table,
                                                                                     waiter=waiter, 
                                                                                     customer=customer_optionmenu.get()))
        start_order_button.place(x=412, y=623)

        back_button = customtkinter.CTkButton(master=self.table_toplevel,
                                              width=230, height=32,
                                              corner_radius=3,
                                              font=("arial", 15),
                                              text_color="#ffffff",
                                              text="Back",
                                              fg_color="#5c5c5c", 
                                              hover_color="#6e6e6e",
                                              command=lambda:self.back_uiorder(id_table=id_table))
        back_button.place(x=170, y=623)
        
        self.tag = "hexwhite"

    def ui_orders(self, id_table):
        try:
            self.table_toplevel.destroy()
        except:
            pass

        self.waiter = Db_table(self.__username).table_waiter(id_table=id_table)
        self.customer = Db_table(self.__username).table_customer(id_table=id_table)
        self.order_id_order = Db_table(self.__username).read_id_order_table(id_table=id_table)
        self.products_order = Db_order(self.__username).order_has_product(id_order=self.order_id_order)
        self.products = Db_product(self.__username).read_product(show_disabled=True)
    
        self.table_toplevel = tkinter.Toplevel(master=self.root)
        self.table_toplevel.after(200, lambda: self.table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        self.table_toplevel.title("Orders")
        self.table_toplevel.geometry("669x895+625+50")
        self.table_toplevel.resizable(False, False)

        self.id_table_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial bold", 17),
                                                     text_color="#2e2e2e",
                                                     text="Table:")
        self.id_table_label.place(x=25, y=10)

        self.id_table_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                     width=150, height=35,
                                                     corner_radius=3,
                                                     border_width=1, 
                                                     font=("arial", 17),
                                                     fg_color="#e3e3e3", 
                                                     border_color="#ffffff")
        self.id_table_entry.place(x=25, y=47)
        self.id_table_entry.insert(0, id_table)
        self.id_table_entry.configure(state="disabled")

        self.waiter_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                   font=("arial bold", 17),
                                                   text_color="#2e2e2e",
                                                   text="Waiter:")
        self.waiter_label.place(x=194, y=10)

        self.waiter_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                   width=450, height=35,
                                                   corner_radius=3,
                                                   border_width=1, 
                                                   font=("arial", 17),
                                                   fg_color="#e3e3e3", 
                                                   border_color="#ffffff")
        self.waiter_entry.place(x=194, y=47)
        self.waiter_entry.insert(0, self.waiter)
        self.waiter_entry.configure(state="disabled")

        self.customer_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial bold", 17),
                                                     text_color="#2e2e2e",
                                                     text="Customer:")
        self.customer_label.place(x=25, y=95)

        self.customer_entry = customtkinter.CTkEntry(master=self.table_toplevel,
                                                     width=620, height=35,
                                                     corner_radius=3,
                                                     border_width=1, 
                                                     font=("arial", 17),
                                                     fg_color="#e3e3e3", 
                                                     border_color="#ffffff")
        self.customer_entry.place(x=25, y=132)
        self.customer_entry.insert(0, self.customer if self.customer != None else "Unregistered")
        self.customer_entry.configure(state="disabled")

        self.products_label = customtkinter.CTkLabel(master=self.table_toplevel,
                                                     font=("arial bold", 17),
                                                     text_color="#2e2e2e",
                                                     text="Products:")
        self.products_label.place(x=25, y=180)

        self.product_optionmenu = customtkinter.CTkOptionMenu(master=self.table_toplevel,
                                                              width=300, height=35,
                                                              corner_radius=4,
                                                              fg_color="#fafafa",
                                                              bg_color="#d9d9d9",
                                                              text_color="#2e2e2e",
                                                              font=("arial", 17),
                                                              dropdown_font=("arial", 15),
                                                              button_color="#818285",
                                                              button_hover_color="#636466",
                                                              values=self.read_data("products"))
        self.product_optionmenu.place(x=25, y=214)

        self.total_spinbox = tkinter.Spinbox(master=self.table_toplevel,
                                             width=3,
                                             font=("arial", 19),
                                             from_=1, to=100)
        self.total_spinbox.place(x=336, y=215)     

        self.add_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                  width=100, height=35,
                                                  corner_radius=4,
                                                  text_color="#ffffff",
                                                  font=("arial", 15), 
                                                  text="Add to list",
                                                  fg_color="#4bb34b", 
                                                  hover_color="#7ebf7e",
                                                  command=self.add_new_selected_orders)
        self.add_button.place(x=410, y=214)

        self.remove_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                     width=100, height=35,
                                                     corner_radius=4,
                                                     text_color="#ffffff",
                                                     font=("arial", 15), 
                                                     text="Remove selected",
                                                     fg_color="#d54a49", 
                                                     hover_color="#d1706f",
                                                     command=self.remove_selected_orders)
        self.remove_button.place(x=520, y=214)

        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        self.style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.products_treeview = ttk.Treeview(master=self.table_toplevel,
                                              height=16,
                                              style="style_treeview.Treeview",
                                              columns=("ID", "product", "sale price", "category"),
                                              show="headings")
        self.products_treeview.place(x=25, y=260)

        self.products_treeview.heading("#1", text="ID", anchor="center")
        self.products_treeview.heading("#2", text="product", anchor="center")
        self.products_treeview.heading("#3", text="sale price", anchor="center")
        self.products_treeview.heading("#4", text="category", anchor="center")

        self.products_treeview.column("#1", minwidth=50, width=70, anchor="center")
        self.products_treeview.column("#2", minwidth=100, width=260, anchor="center")
        self.products_treeview.column("#3", minwidth=100, width=130, anchor="w")
        self.products_treeview.column("#4", minwidth=100, width=150, anchor="w")

        self.treeview_scrollbar = tkinter.Scrollbar(master=self.table_toplevel,
                                                    orient=tkinter.VERTICAL, 
                                                    command=self.products_treeview.yview)
        self.products_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=627, y=260, height=472)

        self.squarestatus_frame = customtkinter.CTkFrame(master=self.table_toplevel,
                                                         width=619,
                                                         height=90,
                                                         fg_color="#ffffff")
        self.squarestatus_frame.place(x=25, y=742)

        self.total_products = self.sale_price = 0
        
        self.productimage_label = customtkinter.CTkLabel(master=self.squarestatus_frame,text="", image=self.product_image)
        self.productimage_label.place(x=25, y=22)
        self.totalproduct_label = customtkinter.CTkLabel(master=self.squarestatus_frame, font=("arial", 17), text_color="#383838", text="Total products:")
        self.totalproduct_label.place(x=95, y=10)
        self.totalproduct_stringvar = customtkinter.StringVar()
        self.totalproductstringvar_label = customtkinter.CTkLabel(master=self.squarestatus_frame, font=("arial", 19), text_color="#383838", textvariable=self.totalproduct_stringvar)
        self.totalproductstringvar_label.place(x=140, y=36)


        self.divider_frame = tkinter.Frame(master=self.squarestatus_frame, height=70, width=1)
        self.divider_frame.place(x=309, y=10)


        self.salepriceimage_label = customtkinter.CTkLabel(master=self.squarestatus_frame,text="", image=self.price_image)
        self.salepriceimage_label.place(x=334, y=22)
        self.saleprice_label = customtkinter.CTkLabel(master=self.squarestatus_frame, font=("arial", 17), text_color="#383838", text="Total price:")
        self.saleprice_label.place(x=404, y=10)
        self.saleprice_stringvar = customtkinter.StringVar()
        self.salepricestringvar_label = customtkinter.CTkLabel(master=self.squarestatus_frame, font=("arial", 19), text_color="#383838", textvariable=self.saleprice_stringvar)
        self.salepricestringvar_label.place(x=449, y=36)

        self.products_treeview.tag_configure("hexyellow", background="#fffd75")
        self.products_treeview.tag_configure("hexweakyellow", background="#fcfbbd")

        self.tag = "hexweakyellow"

        for p in self.products_order:
            for _ in range(p[1]):
                for product_info in self.products:
                    if product_info[0] == p[0]:
                        self.tag = "hexyellow" if self.tag == "hexweakyellow" else "hexweakyellow"
                        self.products_treeview.insert("", "end", values=product_info, tags=self.tag)
                        
                        self.sale_price += float(product_info[2])
                        self.saleprice_stringvar.set(f"{self.sale_price:.2f}")
                        
                        self.total_products += 1
                        self.totalproduct_stringvar.set(self.total_products)

        self.apply_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                    width=230, height=32,
                                                    corner_radius=4,
                                                    text_color="#ffffff",
                                                    font=("arial", 15), 
                                                    text="Apply",
                                                    fg_color="#4bb34b", 
                                                    hover_color="#7ebf7e",
                                                    command=self.apply_order)
        self.apply_button.place(x=412, y=847)

        self.finish_button = customtkinter.CTkButton(master=self.table_toplevel,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="finish",
                                                     fg_color="#fab914", 
                                                     hover_color="#fcc947",
                                                     command=lambda:self.finalize_order(id_table=id_table, 
                                                                                        id_order=self.order_id_order,
                                                                                        waiter=self.waiter, 
                                                                                        customer=self.customer, 
                                                                                        total_products=self.total_products,
                                                                                        total_price=f"{self.sale_price:.2f}"))
        self.finish_button.place(x=170, y=847)
        
        self.products_order = [list(product) for product in self.products_order]
        self.products_order_copy = copy.deepcopy(self.products_order)

    def apply_order(self):
        insert_statement = list()
        update_statement = list()
        delete_statement = list()

        for p_new in self.products_order:
            found = False
            for p_old in self.products_order_copy:
                if p_new[0] == p_old[0]:
                    found = True
                    if p_new[1] != p_old[1] and p_new[1] > 0:
                        update_statement.append(p_new)
                    elif p_new[1] == 0:
                        delete_statement.append(p_new)  
                    break
            if not found:
                insert_statement.append(p_new)

        if insert_statement:
            insert_products = list()
            for insert_p in insert_statement:
                for _ in range(insert_p[1]):
                    insert_products.append(insert_p[0])
            Db_order(self.__username).add_productto_order(self.order_id_order, *insert_products)

        if update_statement:
            Db_order(self.__username).update_order_has_product(self.order_id_order, *update_statement)

        if delete_statement:
            delete_products = list()
            for delete_p in delete_statement:
                delete_products.append(delete_p[0])
            Db_order(self.__username).delete_order_has_product(self.order_id_order, *delete_products)

        if insert_statement or update_statement or delete_statement:
            messagebox.showinfo(title=None, message="Table order updated successfully")

        self.table_toplevel.destroy()
        self.toback()
            
    def add_tolist(self):
        self.products_treeview.tag_configure("hexgray", background="#ededed")
        self.products_treeview.tag_configure("hexwhite", background="#fafbfc")

        product = self.product_optionmenu.get()
        product = Db_product(self.__username).search_product_tablename(product)

        for _ in range(int(self.total_spinbox.get())):
            self.tag = "hexgray" if self.tag == "hexwhite" else "hexwhite"
            self.products_treeview.insert("", "end", values=product, tags=self.tag)
            
            self.sale_price += float(product[2])
            self.saleprice_stringvar.set(f"{self.sale_price:.2f}")
            
            self.total_products += 1
            self.totalproduct_stringvar.set(self.total_products)

    def add_table(self, total: int):
        if total > 0:
            for _ in range(total):
                Db_table(self.__username).create_table()
        
            messagebox.showinfo(title=None, message="Table created successfully")
            self.table_toplevel.destroy()
            self.toback()

    def add_id_table(self, id_table:int):
        if id_table > 0:
            add_table = Db_table(self.__username).create_table(id_table=id_table)
        
        if add_table:
            messagebox.showinfo(title=None, message="Table created successfully")
            self.table_toplevel.destroy()
            self.toback()

    def read_data(self, table: str) -> list:
        data = []

        match table:
            case "products":
                table_rows = Db_product(self.__username).read_product()
            case "waiters":
                table_rows = Db_waiter(self.__username).read_waiter()
            case "customers":
                table_rows = Db_customer(self.__username).read_customer()
                data.append("Unregistered")
            case "table":
                table_rows = Db_table(self.__username).read_table()
                table_rows = list(tuple(map(str, i[::-1])) for i in table_rows)

        for i in table_rows:
            data.append(i[1])
        return data
    
    def add_new_selected_orders(self):
        self.products_treeview.tag_configure("hexgray", background="#ededed")
        self.products_treeview.tag_configure("hexwhite", background="#fafbfc")

        product = self.product_optionmenu.get()
        product = Db_product(self.__username).search_product_tablename(product)

        for _ in range(int(self.total_spinbox.get())):
            self.tag = "hexgray" if self.tag == "hexwhite" else "hexwhite"
            self.products_treeview.insert("", "end", values=product, tags=self.tag)
            
            self.sale_price += float(product[2])
            self.saleprice_stringvar.set(f"{self.sale_price:.2f}")
            
            self.total_products += 1
            self.totalproduct_stringvar.set(self.total_products)

            list_id = False
            slicing = 0
            for id in self.products_order:
                if product[0] == id[0]:
                    self.products_order[slicing][1] += 1
                    list_id = True
                slicing += 1

            if not list_id:
                self.products_order.append([product[0], 1])

    def remove_selected_orders(self):
        if self.selected() == False:
            return 
        
        self.products_treeview.delete(self.products_treeview.selection()[0])
        
        self.sale_price -= float(self.selected_product[2])
        self.sale_price = round(self.sale_price, 2)
        self.saleprice_stringvar.set(f"{self.sale_price:.2f}")

        self.total_products -= 1
        self.totalproduct_stringvar.set(self.total_products)

        slicing = 0
        for id in self.products_order:
            if int(self.selected_product[0]) == id[0]:
                self.products_order[slicing][1] -= 1
            slicing += 1
        
    def remove_selected(self):
        if self.selected() == False:
            return 
        
        self.products_treeview.delete(self.products_treeview.selection()[0])
        
        self.sale_price -= float(self.selected_product[2])
        self.sale_price = round(self.sale_price, 2)
        self.saleprice_stringvar.set(f"{self.sale_price:.2f}")

        self.total_products -= 1
        self.totalproduct_stringvar.set(self.total_products)

    def start_order(self, id_table:int, waiter:str, customer:str):
        waiter_rows = Db_waiter(self.__username).read_waiter()
        for w in waiter_rows:
            if w[1] == waiter:
                waiter = w[0]

        customer_rows = Db_customer(self.__username).read_customer()
        for c in customer_rows:
            if c[1] == customer:
                customer = c[0]
        
        if customer == "Unregistered":
            customer = None

        id_productlist = []
        for item in self.products_treeview.get_children():
            id_productlist.append(self.products_treeview.item(item, "values")[0])

        self.table_toplevel.destroy() 
        id_order = Db_order(self.__username).create_order(waiter, customer, *id_productlist)
        Db_table(self.__username).update_order_table(id_table=id_table, id_order=id_order)

        messagebox.showinfo(title=None, message="Order created successfully")
        self.toback()

    def remove_table(self, id_table: int):
        Db_table(self.__username).delete_table(id_table=id_table)
        self.toback()

    def selected(self) -> bool:
        try:
            self.selected_product = self.products_treeview.item(self.products_treeview.selection()[0], "values")
        except IndexError:
            messagebox.showerror(title=None, message="Please select a product", parent=self.table_toplevel)
            return False
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
            return False
    
    def finalize_order(self, id_table, id_order, waiter, customer, total_products, total_price):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            text = (
                f"TABLE: {id_table}\nWAITER: {waiter}\n\n"
                f"ID ORDER: {id_order}\n"
                f"CUSTOMER: {customer}\n\n"
                "ID, PRODUCT NAME,  SALE PRICE,  CATEGORY,  STATUS:\n\n"
            )
            for item in self.products_treeview.get_children():
                text += str(self.products_treeview.item(item, "values")) + "\n"
            text += f"\nTOTAL PRODUCTS: {total_products}\nTOTAL PRICE: {total_price}"

            with open(file_path, "w") as file:
                file.write(text)
            
            os.system(f"start {file_path}")

        destroy_widgets = [self.products_label, 
                           self.product_optionmenu, 
                           self.total_spinbox,
                           self.add_button,
                           self.remove_button,
                           self.apply_button]
        
        for i in destroy_widgets:
            i.destroy()

        self.table_toplevel.geometry("669x920+625+50")
        self.products_treeview.place(x=25, y=185)
        self.treeview_scrollbar.place(x=627, y=185, height=472)
        self.squarestatus_frame.place(x=25  ,y=667)
        
        self.table_toplevel.attributes("-topmost", True)

        payment_frame = customtkinter.CTkFrame(master=self.table_toplevel,
                                               width=619,
                                               height=90,
                                               fg_color="#ffffff")
        payment_frame.place(x=25, y=770)

        self.change_stringvar = customtkinter.StringVar()
        self.change_stringvar.trace_add("write", self.update_change_stringvar)

        paymentimage_label = customtkinter.CTkLabel(master=payment_frame,text="", image=self.payment_image)
        paymentimage_label.place(x=25, y=22)
        payment_label = customtkinter.CTkLabel(master=payment_frame, font=("arial", 17), text_color="#383838", text="Payment:")
        payment_label.place(x=95, y=10)
        
        validation = self.root.register(validate_input)

        payment_entry = customtkinter.CTkEntry(master=payment_frame,
                                               width=180, height=30,
                                               validate="key",
                                               validatecommand=(validation, "%P"),
                                               textvariable=self.change_stringvar,
                                               corner_radius=3, 
                                               font=("arial", 19), 
                                               text_color="#383838",
                                               border_color="#e3e3e3", 
                                               border_width=1)
        payment_entry.place(x=110, y=39)

        divider_frametwo = tkinter.Frame(master=payment_frame, height=70, width=1)
        divider_frametwo.place(x=309, y=10)

        changeimage_label = customtkinter.CTkLabel(master=payment_frame, text="", image=self.change_image)
        changeimage_label.place(x=334, y=22)
        change_label = customtkinter.CTkLabel(master=payment_frame, 
                                              font=("arial", 17), 
                                              text_color="#383838", 
                                              text="Change:")
        change_label.place(x=404, y=10)
        self.change_stringvar_label = customtkinter.CTkLabel(master=payment_frame, 
                                                             font=("arial", 19), 
                                                             text_color="#e34f4f")
        self.change_stringvar_label.place(x=443, y=36)

        if self.saleprice_stringvar.get() == "":
            self.change_stringvar_label.configure(text="")
            payment_entry.destroy()
        else:
            self.change_stringvar_label.configure(text=f"-{self.saleprice_stringvar.get()}")

        back_button = customtkinter.CTkButton(master=self.table_toplevel,
                                              width=230, height=32,
                                              corner_radius=3,
                                              font=("arial", 15),
                                              text_color="#ffffff",
                                              text="Back",
                                              fg_color="#5c5c5c", 
                                              hover_color="#6e6e6e",
                                              command=lambda:self.back_uiorders(id_table=id_table))
        back_button.place(x=170, y=872)

        self.finish_button.place(x=412, y=872)
        self.finish_button.configure(command=lambda:self.finalize_table(id_table=id_table, id_order=id_order, payment=payment_entry.get()))

        payment_entry.insert(0, 0)

    def back_uiorders(self, id_table):
        self.table_toplevel.destroy()
        self.ui_orders(id_table=id_table)

    def back_uiorder(self, id_table):
        self.table_toplevel.destroy()
        self.ui_table_data(id_table=id_table)
    
    def update_change_stringvar(self, *args):
        try:
            self.change = float(self.change_stringvar.get()) - float(self.saleprice_stringvar.get())
            self.change_stringvar_label.configure(text=f"{self.change:.2f}")
            if self.change < 0:
                self.change_stringvar_label.configure(text_color="#e34f4f")
            else:
                self.change_stringvar_label.configure(text_color="#383838")
        except:
            self.change_stringvar_label.configure(text=f"-{self.saleprice_stringvar.get()}")

    def finalize_table(self, id_table: int, id_order: int, payment: float):
        if self.saleprice_stringvar.get() == "" or self.change >= 0:
            remove_customer = Db_table(self.__username).remove_customer_table(id_table=id_table, id_order=id_order, payment=payment)
            if remove_customer:
                self.table_toplevel.destroy()
                messagebox.showinfo(title=None, message="Table closed successfully.")
            self.toback()

    def toback(self):
        clear_frame(self.square_frame)
        self.ui_widgets()
