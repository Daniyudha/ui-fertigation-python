import customtkinter
from utils.clear_frame import clear_frame
from utils.validate_input import validate_input
import tkinter
from database.db_category import Db_category
from tkinter import ttk, messagebox

class Ui_category:
    def __init__(self, username: str, root: customtkinter.CTk, square_frame: customtkinter.CTk):
        self.__username = username
        self.root = root
        self.square_frame = square_frame

        clear_frame(self.square_frame)
        self.root.after(40, lambda:self.ui_widgets())

    def ui_widgets(self):
        self.topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        self.topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Category")
        self.topbar_label.place(x=20, y=5)

        self.searchcategory_entry = customtkinter.CTkEntry(master=self.topbar_frame,
                                                           width=1227, height=35,
                                                           placeholder_text="Search by category name",
                                                           font=("arial", 17), 
                                                           fg_color="#EEEEEE", 
                                                           border_color="#e3e3e3", 
                                                           border_width=1)
        self.searchcategory_entry.place(x=174, y=8)

        self.searchcategory_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                             width=230, height=32,
                                                             corner_radius=4,
                                                             text_color="#ffffff",
                                                             font=("arial", 15), 
                                                             text="Search",
                                                             fg_color="#407ecf", 
                                                             hover_color="#6996d1",
                                                             command=lambda:self.search_person(self.searchcategory_entry.get()))
        self.searchcategory_button.place(x=1425, y=9)

        self.root.bind("<Return>", lambda _: self.searchcategory_button.invoke())

        self.createcategory_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                           width=350, height=390,
                                                           corner_radius=10,
                                                           fg_color="#ffffff")
        self.createcategory_frame.place(x=10, y=58)

        self.categoryid_label = customtkinter.CTkLabel(master=self.createcategory_frame, 
                                               font=("arial", 17), 
                                               text_color="#383838", 
                                               text="ID:")
        self.categoryid_label.place(x=10, y=10)

        validation = self.root.register(validate_input)

        self.categoryid_entry = customtkinter.CTkEntry(master=self.createcategory_frame,
                                                       width=330, height=35,
                                                       validate="key",
                                                       validatecommand=(validation, "%P"),
                                                       corner_radius=3, 
                                                       font=("arial", 17), 
                                                       border_color="#e3e3e3", 
                                                       border_width=1)
        self.categoryid_entry.place(x=10, y=45)

        self.categoryname_label = customtkinter.CTkLabel(master=self.createcategory_frame, 
                                                         font=("arial", 17), 
                                                         text_color="#383838", 
                                                         text="Category Name:")
        self.categoryname_label.place(x=10, y=90)

        self.categoryname_entry = customtkinter.CTkEntry(master=self.createcategory_frame,
                                                         width=330, height=35,
                                                         corner_radius=3, 
                                                         font=("arial", 17), 
                                                         border_color="#e3e3e3", 
                                                         border_width=1)
        self.categoryname_entry.place(x=10, y=125)

        self.description_label = customtkinter.CTkLabel(master=self.createcategory_frame, 
                                                        font=("arial", 17), 
                                                        text_color="#383838", 
                                                        text="Description:")
        self.description_label.place(x=10, y=170)

        self.description_textbox = customtkinter.CTkTextbox(master=self.createcategory_frame,
                                                            width=330, height=110,
                                                            corner_radius=3, 
                                                            font=("arial", 17), 
                                                            border_color="#e3e3e3", 
                                                            border_width=1)
        self.description_textbox.place(x=10, y=205)

        self.createcategory_button = customtkinter.CTkButton(master=self.createcategory_frame,
                                                             width=330, height=35,
                                                             corner_radius=3,
                                                             font=("arial", 15),
                                                             text_color="#ffffff",
                                                             text="Add Category",
                                                             fg_color="#4bb34b", 
                                                             hover_color="#7ebf7e",
                                                             command=self.create_categorytree)
        self.createcategory_button.place(x=10, y=335)

        self.updatecategory_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                           width=350, height=100,
                                                           corner_radius=10,
                                                           fg_color="#ffffff")
        self.updatecategory_frame.place(x=10, y=680)

        self.updatecategory_label = customtkinter.CTkLabel(master=self.updatecategory_frame, 
                                                           font=("arial", 17), 
                                                           text_color="#383838", 
                                                           text="Update selected category:")
        self.updatecategory_label.place(x=10, y=10)

        self.updatecategory_button = customtkinter.CTkButton(master=self.updatecategory_frame,
                                                             width=330, height=35,
                                                             corner_radius=3,
                                                             font=("arial", 15),
                                                             text_color="#ffffff",
                                                             text="Update Category",
                                                             fg_color="#ec971f", 
                                                             hover_color="#f0b35d",
                                                             command=self.ui_updatecategory)
        self.updatecategory_button.place(x=10, y=45)

        self.deletecategory_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                           width=350, height=100,
                                                           corner_radius=10,
                                                           fg_color="#ffffff")
        self.deletecategory_frame.place(x=10, y=795)

        self.deletecategory_label = customtkinter.CTkLabel(master=self.deletecategory_frame, 
                                                           font=("arial", 17), 
                                                           text_color="#383838", 
                                                           text="Delete selected category:")
        self.deletecategory_label.place(x=10, y=10)

        self.deletecategory_button = customtkinter.CTkButton(master=self.deletecategory_frame,
                                                             width=330, height=35,
                                                             corner_radius=3,
                                                             font=("arial", 15),
                                                             text_color="#ffffff",
                                                             text="Delete Category",
                                                             fg_color="#d54a49", 
                                                             hover_color="#d1706f",
                                                             command=self.delete_categorytree)
        self.deletecategory_button.place(x=10, y=45)

        self.style = ttk.Style()
        self.style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        self.style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        self.style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.category_treeview = ttk.Treeview(master=self.square_frame,
                                              height=29,
                                              style="style_treeview.Treeview",
                                              columns=("ID", "Category", "Description"),
                                              show="headings")
        self.category_treeview.place(x=370, y=58)

        self.category_treeview.heading("#1", text=" ID", anchor="w")
        self.category_treeview.heading("#2", text=" Category", anchor="w")
        self.category_treeview.heading("#3", text=" Description", anchor="w")

        self.category_treeview.column("#1", minwidth=150, width=200, anchor="center")
        self.category_treeview.column("#2", minwidth=150, width=300, anchor="w")
        self.category_treeview.column("#3", minwidth=150, width=800, anchor="w")

        self.treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=self.category_treeview.yview)
        self.category_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=1660, y=58, height=837)

        self.read_categories()

    def ui_updatecategory(self):
        if self.selected() == False:
            return
        
        self.topbar_label.configure(text="Update Category")
        self.searchcategory_entry.destroy()
        self.searchcategory_button.destroy()
        
        self.deletecategory_frame.destroy()
        self.updatecategory_frame.destroy()

        self.categoryid_entry.delete(0, "end")
        self.categoryname_entry.delete(0, "end")
        self.description_textbox.delete("1.0","end")

        self.createcategory_frame.configure(height=440)
        self.createcategory_button.configure(text="Save Changes", 
                                             command=self.update_categorytree)

        self.cancel_button = customtkinter.CTkButton(master=self.createcategory_frame,
                                                     width=330, height=35,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.toback)
        self.cancel_button.place(x=10, y=385)

        self.categoryid_entry.insert(0, self.selected_category[0])
        self.categoryname_entry.insert(0, self.selected_category[1])
        self.description_textbox.insert("1.0", self.selected_category[2])

    def create_categorytree(self):
        action = Db_category(self.__username).create_category(id_category=self.categoryid_entry.get(),
                                                              category_name=self.categoryname_entry.get(),
                                                              description=self.description_textbox.get("1.0","end"))
        if action:
            self.categoryid_entry.delete(0, "end")
            self.categoryname_entry.delete(0, "end")
            self.description_textbox.delete("1.0","end")
            self.toback()

    def read_categories(self):
        self.category_treeview.delete(*self.category_treeview.get_children())

        __all_category = Db_category(self.__username).read_category()
        
        self.category_treeview.tag_configure("hexgray", background="#ededed")
        self.category_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for i in __all_category:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.category_treeview.insert("", "end", values=i, tags=tag)

    def update_categorytree(self):
        update_categorynow = Db_category(self.__username).update_category(new_id = self.categoryid_entry.get(),
                                                                          new_categoryname= self.categoryname_entry.get(),
                                                                          new_description= self.description_textbox.get("1.0", "end"),
                                                                          old_id= self.selected_category[0])

        if update_categorynow:
            self.toback()

    def delete_categorytree(self):
        if self.selected() == False:
            return
        
        message = f"Are you sure you want to delete\nthe category: {self.selected_category[1]}."
        modal = messagebox.askyesno(title=f"id category: {self.selected_category[0]}", message=message)
        
        if modal == True:
            Db_category(self.__username).delete_category(id_category=self.selected_category[0], category_name=self.selected_category[1])
            self.category_treeview.delete(self.category_treeview.selection()[0])

    def search_person(self, typed: str):
        self.category_treeview.delete(*self.category_treeview.get_children())
  
        category = Db_category(self.__username).search_category(typed=typed)

        tag = "hexwhite"
        for i in category:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.category_treeview.insert("", "end", values=i, tags=tag)

    def selected(self) -> bool:
        try:
            self.selected_category = self.category_treeview.item(self.category_treeview.selection()[0], "values")
        except IndexError:
            messagebox.showerror(title=None, message="Please select a category")
            return False
        except Exception as error:
            messagebox.showerror(title=None, message=f"Error: {error}")
            return False      

    def toback(self):
        clear_frame(self.square_frame)
        self.root.after(40, lambda:self.ui_widgets())
