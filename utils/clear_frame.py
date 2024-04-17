import customtkinter

def clear_frame(frame:customtkinter.CTkFrame) -> None: 
    for i in frame.winfo_children():
        i.destroy()
