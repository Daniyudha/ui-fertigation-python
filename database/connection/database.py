from database.connection.db_connection import Db_connection
from tkinter import messagebox

class Database(Db_connection):
    def __init__(self):
        super().__init__()
        if self.db_connected(database=None):
            try:
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS fertigation;")
                self.cursor.execute("USE fertigation;")
        
            except Exception as error:
                messagebox.showerror(title=None, message=f"Error: {error}")

    def login_tables(self):
        self.mysql_connection.commit()
