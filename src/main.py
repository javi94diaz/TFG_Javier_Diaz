
import tkinter as tk
from tkinter import ttk
import Content

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title("DELHI App - Escuela Tecnica Superior de Ingenieros Industriales UPM")
    root.iconbitmap("images/python_ico.ico")
    root.geometry("1250x562")
    root.resizable(False, False)
    content = Content.Content(root)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.grid(column=0, row=0)
    root.mainloop()