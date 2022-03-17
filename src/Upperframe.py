from tkinter import *
from tkinter import ttk
import tkinter as tk
from delhiSymbols import *

class Upperframe(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Upperframe, self).__init__()
        
        mycolor="#1f2633"
        
        s = ttk.Style()
        
        print(args)
        
        titletext = args[1] 
        combotext = args[2]
        button1text = args[3]
        button2text = args[4]
        
        s.configure('title2.TLabel', background = mycolor, foreground = "goldenrod", font = "Verdana 14 bold", relief = "flat")
        s.configure('subtitle2.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 13 bold", relief = "flat")
        s.configure('regularlabel2.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 12 bold", relief = "flat")
        s.configure('innerframe.TFrame', background = mycolor, relief="ridge")
        
        self.configure(style="innerframe.TFrame")
        
        self.step2title =  ttk.Label(self, text = titletext, style = "title2.TLabel")
        self.step2title.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=10)
        
        self.eqlabel = ttk.Label(self, text = "dy/dx  = ", style = "regularlabel2.TLabel")
        self.eqlabel.grid(row=1, column=0, sticky="w", padx=(40,0), pady=3)
        
        self.equationentry2 = tk.Entry(self, bg = "whitesmoke", font="Verdana 11", foreground="black", width=28)
        self.equationentry2.insert(0, "-(y^2)/3")# self.equationentry.get() asi copia la ode del step1
        self.equationentry2.grid(row=1, column=1, sticky="nswe", padx=5, pady=3)
        #self.equationentry2.bind("<Button-1>", lambda event: self.delete_text(event, "warnings_step2"))
        
        self.solvebutton2= tk.Button(self, text = button1text, relief = "flat", width = 20, 
                                     bg="mediumseagreen", fg="white", activebackground="white", activeforeground="mediumseagreen",
                                     font="Helvetica 11 bold")#, command = self.solvestep2)
        self.solvebutton2.grid(row=1, column=2, sticky="nw", padx=10, pady=3)
        
        self.combolabel = ttk.Label(self, text = combotext, style = "regularlabel2.TLabel")
        self.combolabel.grid(row=2, column=0, sticky="w", padx=(40,0), pady=(3,10))
        
        self.inf_value = StringVar()
        self.infoption = ttk.Combobox(self, textvariable=self.inf_value, state = "readonly", height = 10, width = 31, font="Helvetica 11", foreground="#6a737c")
        self.infoption["values"] = inf_list
        self.infoption.current(0)
        self.infoption.bind("<<ComboboxSelected>>",lambda e: self.upperframe2.focus()) #Removes blue highlighting when combobox is selected
        self.infoption.grid(row=2, column=1, sticky="nswe", padx=5, pady=(3,10))
        
        self.clearstep2button = tk.Button(self, text = button2text, relief = "flat", width = 20, 
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold")#, command = self.clearstep2)
        self.clearstep2button.grid(row=2, column=2, sticky="nw", padx=10, pady=(3,10))

#     def solvestep2(self):
#         pass
    
#     def clearstep2(self):
#         pass

if __name__ == "__main__":
    
    root= tk.Tk()
    frame = Upperframe(root, "STEP 3A - CANONICAL COORDINATES", "sYMMETRY:", "SolveNow", "ClearNow")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    ancho = int(root.winfo_width()/8)
    
    frame.pack(fill=BOTH, expand=True)
    root.mainloop()