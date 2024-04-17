import customtkinter
from utils.clear_frame import clear_frame
import tkinter
from database.db_customer import Db_customer
from tkinter import ttk, messagebox

class Ui_customer:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame

        clear_frame(self.square_frame)
        self.ui_widgets()
        self.customer_data()

    def topbar(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame, width=893, height=128, corner_radius=10, fg_color="#ffffff")
        self.topbar_frame.place(x=14, y=0)
        
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("Poppins", 15),
                                                   text_color="#006495", 
                                                   text="Report")
        self.topbar_label.place(x=20, y=5)

        self.searchcustomers_entry = customtkinter.CTkEntry(master=self.topbar_frame,
                                                            width=593, height=50,
                                                            placeholder_text="Cari",
                                                            font=("arial", 12), 
                                                            fg_color="#F3F8FA")
        self.searchcustomers_entry.place(x=174, y=8)

        self.searchcustomers_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                              width=230, height=32,
                                                              corner_radius=4,
                                                              text_color="#ffffff",
                                                              font=("arial", 15), 
                                                              text="Search",
                                                              fg_color="#407ecf", 
                                                              hover_color="#6996d1",
                                                              command=lambda:self.search_person(self.searchcustomers_entry.get()))
        self.searchcustomers_button.place(x=1425, y=9)

        self.root.bind("<Return>", lambda _: self.searchcustomers_button.invoke())

    def ui_widgets(self):
        self.topbar()

        self.delcustomer_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                          width=230, height=32,
                                                          corner_radius=3,
                                                          font=("arial", 15),
                                                          text_color="#ffffff",
                                                          text="Delete Customer",
                                                          fg_color="#d54a49", 
                                                          hover_color="#d1706f",
                                                          command=self.delete_person)
        self.delcustomer_button.place(x=10, y=70)

        self.updatecustomer_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                             width=230, height=32,
                                                             corner_radius=3,
                                                             font=("arial", 15),
                                                             text_color="#ffffff",
                                                             text="Update Customer",
                                                             fg_color="#ec971f", 
                                                             hover_color="#f0b35d",
                                                             command=self.ui_update_person)
        self.updatecustomer_button.place(x=240, y=70)

        self.addcustomer_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                          width=230, height=32,
                                                          corner_radius=3,
                                                          font=("arial", 15),
                                                          text_color="#ffffff",
                                                          text="Add Customer",
                                                          fg_color="#4bb34b", 
                                                          hover_color="#7ebf7e",
                                                          command=self.ui_addcustomer)
        self.addcustomer_button.place(x=470, y=70)

    def customer_data(self):
        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Poppins", 12, "bold"), foreground="#006495")
        self.style.configure("Treeview", font=("Poppins", 12), foreground="#006495", rowheight=28)

        self.customer_treeview = ttk.Treeview(master=self.square_frame,
                                                height=50, 
                                                style="style_treeview.Treeview",
                                                columns=("id customer", "name", "address", 
                                                        "cell phone", "email", "registration date"),
                                                show="headings")
        self.customer_treeview.place(x=14, y=174)

        self.customer_treeview.heading("#1", text="id customer", anchor="center")
        self.customer_treeview.heading("#2", text="name", anchor="center")
        self.customer_treeview.heading("#3", text="address", anchor="center")
        self.customer_treeview.heading("#4", text="cell phone", anchor="center")
        self.customer_treeview.heading("#5", text="email", anchor="center")
        self.customer_treeview.heading("#6", text="registration date", anchor="center")

        self.customer_treeview.column("#1", minwidth=150, width=150, anchor="center")
        self.customer_treeview.column("#2", minwidth=150, width=200, anchor="center")
        self.customer_treeview.column("#3", minwidth=150, width=200, anchor="center")
        self.customer_treeview.column("#4", minwidth=150, width=150, anchor="center")
        self.customer_treeview.column("#5", minwidth=150, width=100, anchor="center")
        self.customer_treeview.column("#6", minwidth=265, width=265, anchor="center")

        self.read_people()

        self.treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=self.customer_treeview.yview)
        self.customer_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=1660, y=50, height=808)

    def ui_addcustomer(self):
        clear_frame(self.square_frame)

        self.topbar()

        self.topbar_label.configure(text="Add Customer")
        self.searchcustomers_entry.destroy()
        self.searchcustomers_button.destroy()

        self.frame_one = customtkinter.CTkFrame(master=self.square_frame,
                                                width=1668, height=440,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=5, y=55)

        self.name_label = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("arial bold", 17),
                                                 text_color="#2e2e2e",
                                                 text="Name:")
        self.name_label.place(x=25, y=25)

        self.name_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                 width=593, height=35,
                                                 corner_radius=3, 
                                                 font=("arial", 17), 
                                                 border_color="#e3e3e3", 
                                                 border_width=1)
        self.name_entry.place(x=25, y=62)

        self.address_label = customtkinter.CTkLabel(master=self.frame_one,
                                                   font=("arial bold", 17),
                                                   text_color="#2e2e2e",
                                                   text="address:")
        self.address_label.place(x=25, y=120)

        self.address_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                   width=593, height=35,
                                                   corner_radius=3, 
                                                   font=("arial", 17), 
                                                   border_color="#e3e3e3", 
                                                   border_width=1)
        self.address_entry.place(x=25, y=160)

        self.cellphone_label = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("arial bold", 17),
                                                      text_color="#2e2e2e",
                                                      text="Cell Phone:")
        self.cellphone_label.place(x=25, y=215)

        self.cellphone_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                      width=593, height=35,
                                                      corner_radius=3, 
                                                      font=("arial", 17),
                                                      border_color="#e3e3e3", 
                                                      border_width=1)
        self.cellphone_entry.place(x=25, y=255)

        self.email_label = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("arial bold", 17),
                                                  text_color="#2e2e2e",
                                                  text="Email:")
        self.email_label.place(x=25, y=310)

        self.email_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                  width=593, height=35,                                                  
                                                  corner_radius=3,
                                                  font=("arial", 17),
                                                  border_color="#e3e3e3", 
                                                  border_width=1)
        self.email_entry.place(x=25, y=350)

        self.divider_frame = tkinter.Frame(master=self.square_frame, 
                                           height=1, width=800, 
                                           bg="#dbdbdb")
        self.divider_frame.place(x=0, y=855)

        self.addcustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                          width=230, height=32,
                                                          corner_radius=3,
                                                          font=("arial", 15),
                                                          text_color="#ffffff",
                                                          text="Add Customer",
                                                          fg_color="#4bb34b", 
                                                          hover_color="#7ebf7e",
                                                          command=self.create_person)
        self.addcustomer_button.place(x=650, y=100)

        self.root.bind("<Return>", lambda _: self.addcustomer_button.invoke())
    
        self.cancel_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.toback)
        self.cancel_button.place(x=650, y=160)

    def ui_update_person(self):
        if self.selected() == False:
            return
        
        clear_frame(self.square_frame)
        
        self.topbar()
        self.topbar_label.configure(text="Update Customer")
        self.searchcustomers_entry.destroy()
        self.searchcustomers_button.destroy()

        self.frame_one = customtkinter.CTkFrame(master=self.square_frame,
                                                width=1668, height=537,
                                                corner_radius=10, 
                                                fg_color="#ffffff")
        self.frame_one.place(x=5, y=55)

        self.id_label = customtkinter.CTkLabel(master=self.frame_one,
                                               font=("arial bold", 17),
                                               text_color="#2e2e2e",
                                               text="ID:")
        self.id_label.place(x=25, y=25)

        self.id_entry = customtkinter.CTkEntry(master=self.frame_one,
                                               width=1618, height=35,
                                               corner_radius=3, 
                                               font=("arial", 17), 
                                               border_color="#e3e3e3", 
                                               border_width=1)
        self.id_entry.place(x=25, y=62)

        self.name_label = customtkinter.CTkLabel(master=self.frame_one,
                                                 font=("arial bold", 17),
                                                 text_color="#2e2e2e",
                                                 text="Name:")
        self.name_label.place(x=25, y=120)

        self.name_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                 width=1618, height=35,
                                                 corner_radius=3, 
                                                 font=("arial", 17), 
                                                 border_color="#e3e3e3", 
                                                 border_width=1)
        self.name_entry.place(x=25, y=160)

        self.address_label = customtkinter.CTkLabel(master=self.frame_one,
                                                    font=("arial bold", 17),
                                                    text_color="#2e2e2e",
                                                    text="Address:")
        self.address_label.place(x=25, y=215)

        self.address_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                    width=1618, height=35,
                                                    corner_radius=3, 
                                                    font=("arial", 17),
                                                    border_color="#e3e3e3",
                                                    border_width=1)
        self.address_entry.place(x=25, y=255)

        self.cellphone_label = customtkinter.CTkLabel(master=self.frame_one,
                                                      font=("arial bold", 17),
                                                      text_color="#2e2e2e",
                                                      text="Cell Phone:")
        self.cellphone_label.place(x=25, y=310)

        self.cellphone_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                      width=1618, height=35,
                                                      corner_radius=3, 
                                                      font=("arial", 17), 
                                                      border_color="#e3e3e3", 
                                                      border_width=1)
        self.cellphone_entry.place(x=25, y=350)

        self.email_label = customtkinter.CTkLabel(master=self.frame_one,
                                                  font=("arial bold", 17),
                                                  text_color="#2e2e2e",
                                                  text="Email:")
        self.email_label.place(x=25, y=405)

        self.email_entry = customtkinter.CTkEntry(master=self.frame_one,
                                                  width=1618, height=35,
                                                  corner_radius=3, 
                                                  font=("arial", 17),
                                                  border_color="#e3e3e3", 
                                                  border_width=1)
        self.email_entry.place(x=25, y=445)

        self.divider_frame = tkinter.Frame(master=self.square_frame, 
                                           height=1, width=1678, 
                                           bg="#dbdbdb")
        self.divider_frame.place(x=0, y=855)

        self.updatecustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                             width=230, height=32,
                                                             corner_radius=3,
                                                             fg_color="#4bb34b", 
                                                             hover_color="#7ebf7e",
                                                             text_color="#ffffff",
                                                             font=("arial", 15), 
                                                             text="Save Changes",
                                                             command=self.update_person)
        self.updatecustomer_button.place(x=1165, y=868)

        self.cancel_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     fg_color="#5c5c5c",
                                                     hover_color="#6e6e6e", 
                                                     text_color="#ffffff",
                                                     font=("arial", 15), 
                                                     text="Cancel",
                                                     command=self.toback)
        self.cancel_button.place(x=1425, y=868)

        self.bring_customerdata()

        self.root.bind("<Return>", lambda _: self.updatecustomer_button.invoke())

    def create_person(self):
        __email = self.email_entry.get()

        if __email in ["None", ""]:
            __email = None

        __add_result = Db_customer(username=self.__username).create_customer(name=self.name_entry.get(),
                                                                             address=self.address_entry.get(),
                                                                             cellphone=self.cellphone_entry.get(),
                                                                             email=__email)
        
        if __add_result:
            self.toback()
    
    def read_people(self):
        self.customer_treeview.delete(*self.customer_treeview.get_children())

        __all_customers = Db_customer(username=self.__username).read_customer()

        self.customer_treeview.tag_configure("hexgray", background="#ededed")
        self.customer_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for i in __all_customers:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.customer_treeview.insert("", "end", values=i, tags=tag)
    
    def update_person(self):
        __email = self.email_entry.get()

        if __email in ["None", ""]:
            __email = None

        __update_data = Db_customer(username=self.__username).update_customer(id_customer=self.id_entry.get(),
                                                                              name=self.name_entry.get(),
                                                                              address=self.address_entry.get(),
                                                                              cellphone=self.cellphone_entry.get(),
                                                                              email=__email)
        
        if __update_data:
            self.toback()

    def delete_person(self):
        if self.selected() == False:
            return
        
        message = f"Are you sure you want to delete\nthe customer: {self.selected_customer[1]}."
        modal = messagebox.askyesno(title=f"id customer: {self.selected_customer[0]}", message=message)
        
        if modal == True:
            Db_customer(self.__username).delete_customer(id_customer=self.selected_customer[0], customer_name= self.selected_customer[1])
            self.customer_treeview.delete(self.customer_treeview.selection()[0])

    def search_person(self, typed: str):
        self.customer_treeview.delete(*self.customer_treeview.get_children())

        customer = Db_customer(self.__username).search_customer(typed=typed)

        tag = "hexwhite"
        for i in customer:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.customer_treeview.insert("", "end", values=i, tags=tag)
            
    def bring_customerdata(self):
        list_entries = [self.id_entry, self.name_entry, self.address_entry, self.cellphone_entry, self.email_entry]
        for k, v in enumerate(list_entries):
            v.insert(0, self.selected_customer[k])

        self.id_entry.configure(state="disabled", fg_color="#e3e3e3", border_color="#ffffff")

    def selected(self) -> bool:
        try:
            self.selected_customer = self.customer_treeview.item(self.customer_treeview.selection()[0], "values")
        except IndexError:
            messagebox.showerror(title=None, message="Please select a customer")
            return False
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
            return False

    def toback(self):
        clear_frame(self.square_frame)
        self.ui_widgets()
        self.customer_data()
