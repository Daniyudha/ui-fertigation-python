import sys

if sys.version_info < (3, 10):
    raise ValueError("This program requires Python 3.10 or higher. Your current Python version is not supported.")

import customtkinter

class Ui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # https://pixabay.com/vectors/burgers-bread-food-cheese-1435094/
        # self.iconbitmap("images/global_images/icon.ico")
        self.title("Testing UI For Smart Fertigation System")
        self.geometry("1024x600")
        # self.attributes('-fullscreen', True)
        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")
        self.attributes("-topmost", True)
        self.attributes("-topmost", False)
