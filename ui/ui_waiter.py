import customtkinter
from utils.clear_frame import clear_frame
from tkinter import ttk, messagebox
import tkinter
from database.db_waiter import Db_waiter

class Ui_waiter:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame

        clear_frame(self.square_frame)
        self.ui_widgets()

    def ui_widgets(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Waiter")
        self.topbar_label.place(x=20, y=5)

        self.searchwaiter_entry = customtkinter.CTkEntry(master=self.topbar_frame,
                                                         width=1227, height=35,
                                                         placeholder_text="Search by waiter name",
                                                         font=("arial", 17), 
                                                         fg_color="#EEEEEE", 
                                                         border_color="#e3e3e3", 
                                                         border_width=1)
        self.searchwaiter_entry.place(x=174, y=8)

        self.searchwaiter_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                           width=230, height=32,
                                                           corner_radius=4,
                                                           text_color="#ffffff",
                                                           font=("arial", 15), 
                                                           text="Search",
                                                           fg_color="#407ecf", 
                                                           hover_color="#6996d1",
                                                           command=lambda:self.search_person(self.searchwaiter_entry.get()))
        self.searchwaiter_button.place(x=1425, y=9)

        self.root.bind("<Return>", lambda _: self.searchwaiter_button.invoke())

        self.operations_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                       width=350, height=260,
                                                       corner_radius=10,
                                                       fg_color="#ffffff")
        self.operations_frame.place(x=10, y=58)

        self.waitername_label = customtkinter.CTkLabel(master=self.operations_frame, 
                                                       font=("arial", 17), 
                                                       text_color="#383838", 
                                                       text="Name:")
        self.waitername_label.place(x=10, y=10)

        self.waitername_entry = customtkinter.CTkEntry(master=self.operations_frame,
                                                       width=330, height=35,
                                                       corner_radius=3, 
                                                       font=("arial", 17), 
                                                       border_color="#e3e3e3", 
                                                       border_width=1)
        self.waitername_entry.place(x=10, y=45)

        self.waitercellphone_label = customtkinter.CTkLabel(master=self.operations_frame, 
                                                            font=("arial", 17), 
                                                            text_color="#383838", 
                                                            text="Cell Phone:")
        self.waitercellphone_label.place(x=10, y=90)

        self.waitercellphone_entry = customtkinter.CTkEntry(master=self.operations_frame,
                                                            width=330, height=35,
                                                            corner_radius=3, 
                                                            font=("arial", 17), 
                                                            border_color="#e3e3e3", 
                                                            border_width=1)
        self.waitercellphone_entry.place(x=10, y=135)

        self.createwaiter_button = customtkinter.CTkButton(master=self.operations_frame,
                                                           width=330, height=35,
                                                           corner_radius=3,
                                                           font=("arial", 15),
                                                           text_color="#ffffff",
                                                           text="Add Waiter",
                                                           fg_color="#4bb34b", 
                                                           hover_color="#7ebf7e",
                                                           command=self.create_waitertree)
        self.createwaiter_button.place(x=10, y=200)

        self.updatewaiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                         width=350, height=100,
                                                         corner_radius=10,
                                                         fg_color="#ffffff")
        self.updatewaiter_frame.place(x=10, y=680)

        self.updatewaiter_label = customtkinter.CTkLabel(master=self.updatewaiter_frame, 
                                                         font=("arial", 17), 
                                                         text_color="#383838", 
                                                         text="Update selected waiter:")
        self.updatewaiter_label.place(x=10, y=10)

        self.updatewaiter_button = customtkinter.CTkButton(master=self.updatewaiter_frame,
                                                           width=330, height=35,
                                                           corner_radius=3,
                                                           font=("arial", 15),
                                                           text_color="#ffffff",
                                                           text="Update Waiter",
                                                           fg_color="#ec971f", 
                                                           hover_color="#f0b35d",
                                                           command=self.ui_updatewaiter)
        self.updatewaiter_button.place(x=10, y=45)

        self.deletewaiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                         width=350, height=100,
                                                         corner_radius=10,
                                                         fg_color="#ffffff")
        self.deletewaiter_frame.place(x=10, y=795)

        self.deletewaiter_label = customtkinter.CTkLabel(master=self.deletewaiter_frame, 
                                                         font=("arial", 17), 
                                                         text_color="#383838", 
                                                         text="Delete selected waiter:")
        self.deletewaiter_label.place(x=10, y=10)

        self.deletewaiter_button = customtkinter.CTkButton(master=self.deletewaiter_frame,
                                                           width=330, height=35,
                                                           corner_radius=3,
                                                           font=("arial", 15),
                                                           text_color="#ffffff",
                                                           text="Delete Waiter",
                                                           fg_color="#d54a49", 
                                                           hover_color="#d1706f",
                                                           command=self.delete_waitertree)
        self.deletewaiter_button.place(x=10, y=45)

        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        self.style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.waiter_treeview = ttk.Treeview(master=self.square_frame,
                                            height=29,
                                            style="style_treeview.Treeview",
                                            columns=("ID", "name", "cell phone"),
                                            show="headings")
        self.waiter_treeview.place(x=370, y=58)

        self.waiter_treeview.heading("#1", text="  ID", anchor="w")
        self.waiter_treeview.heading("#2", text=" name", anchor="w")
        self.waiter_treeview.heading("#3", text=" cell phone", anchor="w")

        self.waiter_treeview.column("#1", minwidth=100, width=150, anchor="center")
        self.waiter_treeview.column("#2", minwidth=250, width=400, anchor="w")
        self.waiter_treeview.column("#3", minwidth=500, width=750, anchor="w")

        self.treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=self.waiter_treeview.yview)
        self.waiter_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=1660, y=58, height=837)

        self.read_waiters()

    def ui_updatewaiter(self):
        if self.selected() == False:
            return
        
        self.topbar_label.configure(text="Update Waiter")
        self.searchwaiter_entry.destroy()
        self.searchwaiter_button.destroy()
        
        self.updatewaiter_frame.destroy()
        self.deletewaiter_frame.destroy()

        self.waitername_entry.delete(0, "end")
        self.waitercellphone_entry.delete(0, "end")

        self.operations_frame.configure(height=320)
        self.createwaiter_button.configure(text="Save Changes", 
                                           command=self.update_waitertree)

        self.cancel_button = customtkinter.CTkButton(master=self.operations_frame,
                                                     width=330, height=35,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.toback)
        self.cancel_button.place(x=10, y=255)

        self.waitername_entry.insert(0, self.selected_waiter[1])
        self.waitercellphone_entry.insert(0, self.selected_waiter[2])

    def create_waitertree(self):
        action = Db_waiter(self.__username).create_waiter(name=self.waitername_entry.get(),
                                                          cell_phone=self.waitercellphone_entry.get())
        
        if action:
            self.waitername_entry.delete(0, "end")
            self.waitercellphone_entry.delete(0, "end")
            self.toback()

    def read_waiters(self):
        self.waiter_treeview.delete(*self.waiter_treeview.get_children())

        __all_waiter = Db_waiter(self.__username).read_waiter()
        
        self.waiter_treeview.tag_configure("hexgray", background="#ededed")
        self.waiter_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for i in __all_waiter:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.waiter_treeview.insert("", "end", values=i, tags=tag)

    def update_waitertree(self):
        update_waiternow = Db_waiter(self.__username).update_waiter(new_name=self.waitername_entry.get(),
                                                                    new_cell_phone=self.waitercellphone_entry.get(),
                                                                    id_water=self.selected_waiter[0])

        if update_waiternow:
            self.toback()

    def delete_waitertree(self):
        if self.selected() == False:
            return
        
        message = f"Are you sure you want to delete\nthe waiter: {self.selected_waiter[1]}."
        modal = messagebox.askyesno(title=f"id waiter: {self.selected_waiter[0]}", message=message)
        
        if modal == True:
            Db_waiter(self.__username).delete_waiter(id_waiter=self.selected_waiter[0], waiter_name=self.selected_waiter[1])
            self.waiter_treeview.delete(self.waiter_treeview.selection()[0])

    def search_person(self, typed: str):
        self.waiter_treeview.delete(*self.waiter_treeview.get_children())
  
        waiter = Db_waiter(self.__username).search_waiter(typed=typed)

        tag = "hexwhite"
        for i in waiter:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.waiter_treeview.insert("", "end", values=i, tags=tag)

    def selected(self) -> bool:
        try:
            self.selected_waiter = self.waiter_treeview.item(self.waiter_treeview.selection()[0], "values")
        except IndexError:
            messagebox.showerror(title=None, message="Please select a waiter")
            return False
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
            return False

    def toback(self):
        clear_frame(self.square_frame)
        self.ui_widgets()
