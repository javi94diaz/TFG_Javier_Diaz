
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

import sympy as sp
from sympy import sin, cos, tan, sinh, cosh, tanh, exp, log,  atan, atanh, asin, acos, asinh, acosh
from sympy.core import sympify

from PIL import ImageTk, Image
import pygame
import time
import xlrd

from benchmarkv5 import *
from delhiSymbols import *

pygame.init()

def my_exec(code):
    global aux
    exec("global aux; aux= %s" % code)
    return aux

class Content(ttk.Frame):
        
    def __init__(self, *args, **kwargs):
        super(Content, self).__init__()
        
        #COLOR GUAPO PARA FONDO background="#1f2633"
        mycolor="#1f2633"
        
        s = ttk.Style()
        s.configure('lateral.TFrame', background = mycolor)
        s.configure('workarea.TFrame', background = mycolor)
        s.configure('welcome.TFrame', borderwidth = 0, background = mycolor)
        s.configure('solver.TFrame', background = mycolor, relief="groove")
        s.configure('stepbystep.TFrame', background = mycolor, relief="groove")
        s.configure('benchmark.TFrame', background = mycolor, relief="groove")
        s.configure('help.TFrame', background = mycolor, relief="groove")
        s.configure('innerframe.TFrame', background = mycolor, relief="ridge")
        s.configure('subframe.TFrame', background = mycolor)
        
        #estilos para solver mas grandes
        s.configure('title.TLabel', background = mycolor, foreground = "goldenrod", font = "Verdana 18 bold", relief = "flat", padding=15)
        s.configure('subtitle.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 14 bold", relief = "flat", padding=20)
        s.configure('regularlabel.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 12 bold", relief = "flat", padding=20)
        s.configure('smalllabel.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 10", relief = "flat", padding=20)
        s.configure('resultlabel.TLabel', background = mycolor, foreground = "gold", font = "Verdana 12 bold", relief = "flat", padding=20)
        
        #estilos para stepbystep mas pequeños
        s.configure('title2.TLabel', background = mycolor, foreground = "goldenrod", font = "Verdana 14 bold", relief = "flat")
        s.configure('subtitle2.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 13 bold", relief = "flat")
        s.configure('regularlabel2.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 12 bold", relief = "flat")
        s.configure('smalllabel2.TLabel', background = mycolor, foreground = "whitesmoke", font = "Verdana 11", relief = "flat")
        s.configure('resultlabel2.TLabel', background = mycolor, foreground = "gold", font = "Verdana 10 bold", relief = "flat")
        s.configure('resultlabel3.TLabel', background = "lightsalmon", foreground = "black", font = "Verdana 11 bold", relief = "ridge")
        s.configure('resultlabel4.TLabel', background = "plum", foreground = "black", font = "Verdana 11 bold", relief = "ridge")
        s.configure('resultlabel5.TLabel', background = "mediumseagreen", foreground = "black", font = "Verdana 11 bold", relief = "ridge")
        s.configure('tablelabel.TLabel', background = mycolor, foreground = "gold", font = "Verdana 12 bold", relief = "sunken")
        
        #estilos para etiquetas de mensajes de error
        s.configure('okmessage.TLabel', background = mycolor, foreground = "limegreen", font = "Verdana 14 bold", relief = "flat", padding=20)
        s.configure('warningmessage.TLabel', background = mycolor, foreground = "orange", font = "Verdana 14 bold", relief = "flat", padding=20)
        s.configure('errormessage.TLabel', background = mycolor, foreground = "red", font = "Verdana 14 bold", relief = "flat", padding=20)
        s.configure('invisiblemessage.TLabel', background = mycolor, foreground = "#1f263", font = "Verdana 14 bold", relief = "flat", padding=20)
        
        s.configure('okmessage2.TLabel', background = mycolor, foreground = "limegreen", font = "Verdana 10 bold", relief = "flat")
        s.configure('warningmessage2.TLabel', background = mycolor, foreground = "orange", font = "Verdana 10 bold", relief = "flat")
        s.configure('errormessage2.TLabel', background = mycolor, foreground = "red", font = "Verdana 10 bold", relief = "flat")
        s.configure('invisiblemessage2.TLabel', background = mycolor, foreground = mycolor, font = "Verdana 10 bold", relief = "flat")
        s.configure('verifiedmessage.TLabel', background = mycolor, foreground = "deepskyblue", font = "Verdana 10 bold", relief = "flat")
                
        #otros estilos
        s.configure("nb.TNotebook", background=mycolor)
        s.configure("checkbtn.TCheckbutton", background= mycolor, foreground = "whitesmoke", font ="Helvetica 11 bold")

        
    #Content Frame definitions
        self.lateral = ttk.Frame(self, style="lateral.TFrame")
        self.workarea = ttk.Frame(self, width=1000, height=562, style='workarea.TFrame')
        
    # Widgets in LATERAL Frame
        self.etsiidome = PhotoImage (file = "images/etsiidome.png")
        self.etsiilabel = tk.Label(self.lateral, image = self.etsiidome, background="white", relief="groove", borderwidth = 5)#, highlightthickness=10
        self.etsiilabel.grid(row=0, column=0, sticky="nsew", padx = 5, pady = 5)
        buttonfont = font.Font(family = "Helvetica", size = 15, weight = "bold")#, slant = "italic"
        
        self.welcomebtn = tk.Button(self.lateral, text = "Home", command = self.show_welcome, bg = "#2a7b7c", fg = "gold", activebackground = "gold", activeforeground = "#2a7b7c", font = buttonfont, relief = "flat", width = 20)
        self.solverbtn = tk.Button(self.lateral, text = "Solver", command = self.show_solver, bg = "#2a7b7c", fg = "gold", activebackground = "gold", activeforeground = "#2a7b7c", font = buttonfont, relief = "flat", width = 20)
        self.stepsbtn = tk.Button(self.lateral, text = "Step-by-step", command = self.show_stepbystep, bg = "#2a7b7c", fg = "gold", activebackground = "gold", activeforeground = "#2a7b7c", font = buttonfont, relief = "flat", width = 20)
        self.benchmarkbtn = tk.Button(self.lateral, text = "Benchmark", command = self.show_benchmark, bg = "#2a7b7c", fg = "gold", activebackground = "gold", activeforeground = "#2a7b7c", font = buttonfont, relief = "flat", width = 20)
        self.helpbtn = tk.Button(self.lateral, text = "Help", command = self.show_help, bg = "#2a7b7c", fg = "gold", activebackground = "gold", activeforeground = "#2a7b7c", font = buttonfont, relief = "flat", width = 20)
        self.playbutton = tk.Button(self.lateral, text = "Play", command=self.play, bg = mycolor, fg = mycolor, activebackground = mycolor, activeforeground = mycolor, font = buttonfont, relief = "flat", width = 20)
        
        self.welcomebtn.grid(row=1, column=0, padx = 5, pady =10)
        self.solverbtn.grid(row=2, column=0, padx = 5, pady =10)
        self.stepsbtn.grid(row=3, column=0, padx = 5, pady =10)
        self.benchmarkbtn.grid(row=4, column=0, padx = 5, pady =10)
        self.helpbtn.grid(row=5, column=0, padx = 5, pady =10)
        self.playbutton.grid(row=6, column=0, padx = 5, pady =10)
        
    # Frames in WORKAREA Frame
        self.welcome = ttk.Frame(self.workarea, width=1000, height=562, style="welcome.TFrame")
        self.solver = ttk.Frame(self.workarea, width=1000, height=562, style="solver.TFrame")
        self.stepbystep = ttk.Frame(self.workarea, width=1000, height=562, style="stepbystep.TFrame")
        self.benchmark = ttk.Frame(self.workarea, width=1000, height=562, style="benchmark.TFrame")
        self.help = ttk.Frame(self.workarea, width=1000, height=562, style = "help.TFrame")
        
    # Widgets in WELCOME Frame
        #self.cover =  PhotoImage (file = "images/cubitos.png")
        self.cover =  PhotoImage (file = "images/cover2.png")
        self.coverlabel = tk.Label(self.welcome, image=self.cover, relief="flat", borderwidth = 0, highlightthickness=0)
        self.coverlabel.pack()
        #self.coverlabel.photo = self.cover
        #self.coverlabel.place(x=0, y=0, relwidth=1, relheight=1)
        
#         self.backgroundimage = PhotoImage(file="images/fondocover2.png")
#         self.backgroundlabel = Label(self.welcome, image=self.backgroundimage)
#         self.backgroundlabel.photo = self.backgroundimage
#         self.backgroundlabel.image = self.backgroundimage #keep a reference against the garbage collector
#         self.backgroundlabel.place(x=0, y=0, relwidth=1, relheight=1)
        
#         self.ejemplo = ttk.Label(self.welcome, text="EJEMPLO")
#         self.ejemplo.pack(side =LEFT)
        
        
    # Widgets in SOLVER Frame
        self.solvertitle =  ttk.Label(self.solver, text = "ODE LIE SOLVER", style = "title.TLabel")
        self.solvertitle.grid(row=0, column=0, padx=(250,0), pady=(20,30))
        
        self.auxframe = ttk.Frame(self.solver, style="subframe.TFrame")
        self.auxframe.grid(row=1, column=0, padx=(220,0), pady=10)
        
        self.equationlabel = ttk.Label(self.auxframe, text = "Enter your ODE in terms of y, dy and x: ", style = "subtitle.TLabel")
        self.equationlabel.grid(row=0, column=0, columnspan= 2, sticky="nsw")
        
        self.equation = tk.Entry(self.auxframe, bg = "#DAFFDA", font="Verdana 14", foreground="#6a737c", width=30)
        self.equation.insert(0, "3*dy+y^2=0") #Type your equation here
        self.equation.grid(row=1, column=0, padx=(25,10), sticky="ns")
        self.equation.bind("<Button-1>", lambda event: self.delete_text(event, "warnings_solver"))
        
        self.solvebutton = tk.Button(self.auxframe, text = "Solve", relief = "flat", width=12,
                                     bg="mediumseagreen", fg="white", activebackground = "white", activeforeground = "mediumseagreen", 
                                     font="Helvetica 12 bold", command = self.simplesolver)
        self.solvebutton.grid(row=1, column=1, sticky="nw")
        
        self.solutionlabel = ttk.Label(self.auxframe, text = "The solution is:", style  ="subtitle.TLabel")
        self.solutionlabel.grid(row=2, column = 0, columnspan=2, sticky="nsw")
        
        self.solution = tk.Entry(self.auxframe, bg = "lightblue", font="Verdana 14", foreground="#6a737c", relief = "flat", width=30)
        self.solution.insert(0, "Solution appears here...")
        self.solution.grid(row=3, column=0, padx=(25,10), sticky = "ns")
        
        self.clearbutton = tk.Button(self.auxframe, text = "Clear", relief = "flat", width=12,
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 12 bold", command = self.clearsolver)
        self.clearbutton.grid(row=3, column = 1, sticky="nw")
        
        self.warnings = ttk.Label(self.auxframe, text = "Solvable by Lie group", style='invisiblemessage.TLabel')
        self.warnings.grid(row=4, column=0, sticky="nw")
        
        # PARA MOSTRAR LATEX EN TKINTER
        #    https://stackoverflow.com/questions/36636185/is-it-possible-for-python-to-display-latex-in-real-time-in-a-text-box        
        
        
        
    #Widgets in STEP BY STEP Frame
        self.notebook = ttk.Notebook(self.stepbystep, style="nb.TNotebook")
        self.notebook.pressed_index=None
        
        self.step1frame = ttk.Frame(self.notebook, style = "subframe.TFrame")
        self.notebook.add(self.step1frame, text = "\tSTEP 1\t", padding = 0)
        self.step2frame = ttk.Frame(self.notebook, style = "subframe.TFrame")
        self.notebook.add(self.step2frame, text = "\tSTEP 2A\t", padding = 0)
        self.step3frame = ttk.Frame(self.notebook, style = "subframe.TFrame")
        self.notebook.add(self.step3frame, text = "\tSTEP 2B\t", padding = 0)

        self.notebook.pack(fill=BOTH, expand=True)
        
    #STEP 1 FRAME
        self.upperframe = ttk.Frame(self.step1frame, style="innerframe.TFrame")
        self.belowframe = ttk.Frame(self.step1frame, style="innerframe.TFrame")
        self.warnframe1 = ttk.Frame(self.step1frame, style="innerframe.TFrame")
        
        self.upperframe.pack(fill=BOTH, expand=False, padx=8, pady=5)
        self.belowframe.pack(fill=BOTH, expand=True, padx=8, pady=5)
        self.warnframe1.pack(fill=BOTH, expand=False, padx=8, pady=(2,3))
        
        #Upperframe
        self.step1title =  ttk.Label(self.upperframe, text = "STEP 1 - INFINITESIMALS", style="title2.TLabel")
        self.step1title.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=10)

        self.enterlabel = ttk.Label(self.upperframe, text = "dy/dx  = ", style="regularlabel2.TLabel")
        self.enterlabel.grid(row=1, column=0, sticky="w", padx=(40,0), pady=3)
 
        self.equationentry = tk.Entry(self.upperframe, bg = "peachpuff", font="Verdana 11", foreground="#6a737c")
        self.equationentry.insert(0, "-(y^2)/3")
        self.equationentry.grid(row=1, column=1, sticky="nswe", padx=5, pady=3)
        self.equationentry.bind("<Button-1>", lambda event: self.delete_text(event, "warnings_step1"))
        
        self.obtainbutton = tk.Button(self.upperframe, text = "Calculate", relief = "flat", width = 20,
                                bg="lightsalmon", fg="white", activebackground = "white", activeforeground = "lightsalmon", 
                                font="Helvetica 11 bold", command = self.obtinfinitesimals)
        self.obtainbutton.grid(row=1, column=2, sticky="nw", padx=10, pady=3)
        
        self.heurlabel = ttk.Label(self.upperframe, text = "Heuristic:", style="regularlabel2.TLabel")
        self.heurlabel.grid(row=2, column=0, sticky="w", padx=(40,0), pady=(3,10))
        
        self.heur_value = StringVar()
        self.heuroption = ttk.Combobox(self.upperframe, textvariable=self.heur_value, state = "readonly", font="Helvetica 11", width = 31)
        self.heuroption["values"] = lie_heuristics
        self.heuroption['state']  = "readonly"
        self.heuroption.current(0)
        self.heuroption.bind("<<ComboboxSelected>>",lambda e: self.upperframe.focus()) #Removes blue highlighting when combobox is selected
        self.heuroption.bind("<Button-1>", lambda e2: self.step1warnings.configure(text="invisible text", style="invisiblemessage2.TLabel"))
        self.heuroption.grid(row=2, column=1, sticky="ns", padx=5, pady=(3,10))
        
        self.clearstep1button = tk.Button(self.upperframe, text = "Clear", relief = "flat", width=20,
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold", command = self.clearstep1)
        self.clearstep1button.grid(row=2, column=2, sticky="nw", padx=10, pady=(3,10))
        
        self.var1 = IntVar()
        self.clearode = ttk.Checkbutton(self.upperframe, text="Clear ODE", variable=self.var1, style="checkbtn.TCheckbutton",  takefocus=False)
        self.clearode.grid(row=2, column=3)
        
        #Belowframe
        self.conditionframe = ttk.Frame(self.belowframe, style="innerframe.TFrame")
        self.scrollframe = ttk.Frame(self.belowframe, style="subframe.TFrame")
        self.conditionframe.pack(fill=BOTH, expand=False)
        self.scrollframe.pack(fill=BOTH, expand=True)
        
        #Conditionframe
        self.conditionlabel = ttk.Label(self.conditionframe, text = "Linearized symmetry condition", style = "resultlabel2.TLabel")
        self.conditionlabel.grid(row=0, column=0, padx=10, pady=(10,3))
        
        self.conditionimg = PhotoImage(file = "images/condition.png")
        self.condition = ttk.Label(self.conditionframe, image=self.conditionimg)
        self.condition.grid(row=0, column=1, padx= 5, pady=(10,3))
         
        self.substitutedlabel = ttk.Label(self.conditionframe, text = "Substituted symmetry condition", style = "resultlabel2.TLabel")
        self.substitutedlabel.grid(row=1, column=0, padx=10, pady=(3,10))
        
        self.substituted = tk.Entry(self.conditionframe, bg = "peachpuff", font="Verdana 11", foreground="#6a737c", width=33)
        self.substituted.insert(0, "Substituted condition...")
        self.substituted.grid(row=1, column=1, padx=5, pady=(3,10))
        
        #Scrollframe
        self.canvas = tk.Canvas(self.scrollframe, height=250 , background=mycolor)
        myscrollbar = tk.Scrollbar(self.scrollframe, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="right", fill=BOTH, expand=True)
        
        self.window = ttk.Frame(self.canvas, style="subframe.TFrame")
        self.canvas.create_window((0,0), window=self.window, anchor="nw")
        self.window.bind("<Configure>", self._lets_scroll)
        self.window.bind('<Enter>', self._bound_to_mousewheel)
        self.window.bind('<Leave>', self._unbound_to_mousewheel)
        
        ancholbl = 14
        self.nlabel = ttk.Label(self.window, text = "Number", style = "resultlabel3.TLabel", width=int(ancholbl/2))
        self.xilbl  = ttk.Label(self.window, text = "Xi", style = "resultlabel3.TLabel", width=ancholbl)
        self.etalbl  = ttk.Label(self.window, text = "Eta", style = "resultlabel3.TLabel", width=ancholbl)
        
        self.nlabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)
        self.xilbl.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)
        self.etalbl.grid(row=0, column=2, sticky="nsew", padx=10, pady=6)
        
        self.numentrys = []
        self.xientrys = []
        self.etaentrys = []
        
        #Warnframe
        self.step1warnings = ttk.Label(self.warnframe1, text = "invisible text", style='invisiblemessage.TLabel')
        self.step1warnings.pack(side=LEFT, padx=5, pady=3)

        
    #STEP 2A FRAME
        self.upperframe2 = ttk.Frame(self.step2frame, style="innerframe.TFrame")
        self.belowframe2 = ttk.Frame(self.step2frame, style="innerframe.TFrame")
        self.warnframe2 = ttk.Frame(self.step2frame, style="innerframe.TFrame")
        
        #Upperframe2
        self.step2title =  ttk.Label(self.upperframe2, text = "STEP 2A - LIE INTEGRATING FACTOR", style = "title2.TLabel")
        self.step2title.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=10)
        
        self.eqlabel = ttk.Label(self.upperframe2, text = "dy/dx  = ", style = "regularlabel2.TLabel")
        self.eqlabel.grid(row=1, column=0, sticky="w", padx=(40,0), pady=3)
        
        self.equationentry2 = tk.Entry(self.upperframe2, bg = "#DAC0DA", font="Verdana 11", foreground="black", width=28)
        self.equationentry2.insert(0, "-(y^2)/3")
        self.equationentry2.grid(row=1, column=1, sticky="nswe", padx=5, pady=3)
        self.equationentry2.bind("<Button-1>", lambda event: self.delete_text(event, "warnings_step2a"))
        
        self.solvebutton2= tk.Button(self.upperframe2, text = "Solve", relief = "flat", width = 20, 
                                     bg="plum", fg="white", activebackground="white", activeforeground="plum",
                                     font="Helvetica 11 bold", command = self.solvestep2)
        self.solvebutton2.grid(row=1, column=2, sticky="nw", padx=10, pady=3)
        
        self.symmlabel = ttk.Label(self.upperframe2, text = "Symmetry:", style = "regularlabel2.TLabel")
        self.symmlabel.grid(row=2, column=0, sticky="w", padx=(40,0), pady=(3,10))
        
        self.inf_value = StringVar()
        self.infoption = ttk.Combobox(self.upperframe2, textvariable=self.inf_value, state = "readonly", height = 10, width = 31, font="Helvetica 11")
        self.infoption["values"] = inf_list
        self.infoption.current(0)
        self.infoption.bind("<<ComboboxSelected>>",lambda e: self.upperframe2.focus()) #Removes blue highlighting when combobox is selected
        self.infoption.bind("<Button-1>", lambda e3: self.step2warnings.configure(text="invisible text", style="invisiblemessage2.TLabel"))
        self.infoption.grid(row=2, column=1, sticky="nswe", padx=5, pady=(3,10))
        
        self.clearstep2button = tk.Button(self.upperframe2, text = "Clear", relief = "flat", width = 20, 
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold", command = self.clearstep2)
        self.clearstep2button.grid(row=2, column=2, sticky="nw", padx=10, pady=(3,10))
        
        #Belowframe2
        self.integfactorlabel = ttk.Label(self.belowframe2, text = "Method A: Integrating factor transformation", style = "resultlabel.TLabel")
        self.integfactorlabel.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,6), sticky="w")
        
        self.factorlabel = ttk.Label(self.belowframe2, text = "2.  Integrating factor:", style = "resultlabel4.TLabel", width = 25)
        self.factorlabel.grid(row=1, column=0, sticky="w", padx=10, pady=(20,6))
        
        self.factorimg = PhotoImage(file = "images/factor2.png")
        self.factor = ttk.Label(self.belowframe2, image=self.factorimg)
        self.factor.grid(row=1, column=1, padx= 5, pady=(20,6))

        self.subsfactorlabel = ttk.Label(self.belowframe2, text = "3.  Substituted integ. factor:", style = "resultlabel4.TLabel", width = 25)
        self.subsfactorlabel.grid(row=2, column=0, sticky="w", padx=10, pady=6)
        
        self.factorentry = tk.Entry(self.belowframe2, bg = "#DAC0DA", font="Verdana 11", foreground="#6a737c", relief = "flat", width=33)
        self.factorentry.insert(0, "Integrating factor...")
        self.factorentry.grid(row=2, column=1, sticky="nsw", padx=5, pady=6)
        
#         self.yprime = ttk.Label(self.belowframe2, text = "4 -  Exact ODE:", style  ="resultlabel4.TLabel", width = 25)
#         self.yprime.grid(row=3, column=0, sticky="w", padx=10, pady=6)
#         
#         self.exact = tk.Entry(self.belowframe2, bg = "#DAC0DA", font="Verdana 11", foreground="#6a737c", relief = "flat", width=33)
#         self.exact.insert(0, "Exact ODE...")
#         self.exact.grid(row=3, column=1, sticky="w", padx=5, pady=6)
        
        self.solutionlabel2 = ttk.Label(self.belowframe2, text = "4.  The solution is:", style  ="resultlabel4.TLabel", width = 25)
        self.solutionlabel2.grid(row=3, column = 0, sticky="w", padx=10, pady=6)
        
        self.solution2 = tk.Entry(self.belowframe2, bg = "#DAC0DA", font="Helvetica 12", foreground="#6a737c", relief = "flat", width=33)
        self.solution2.insert(0, "Solution appears here...")
        self.solution2.grid(row=3, column=1, sticky="nswe", padx=5, pady=6)
        
        self.checksolution2 = tk.Button(self.belowframe2, text = "Check solution", relief = "flat", width = 15, 
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold", command = self.checksol2)
        self.checksolution2.grid(row=4, column=1, padx=10, pady=(6,10))
        
        #Warnframe2
        self.step2warnings = ttk.Label(self.warnframe2, text = "invisible text", style='invisiblemessage2.TLabel')
        self.step2warnings.pack(side=LEFT, padx=5, pady=3)
        
        self.upperframe2.pack(fill=BOTH, expand=False, padx=8, pady=5)
        self.belowframe2.pack(fill=BOTH, expand=True, padx=8, pady=5)
        self.warnframe2.pack(fill=BOTH, expand=False, padx=8, pady=(2,3))
        
        
    #STEP 2B FRAME
        self.upperframe3 = ttk.Frame(self.step3frame, style="innerframe.TFrame")
        self.belowframe3 = ttk.Frame(self.step3frame, style="innerframe.TFrame")
        self.warnframe3 = ttk.Frame(self.step3frame, style="innerframe.TFrame")
        
        #Upperframe3
        self.step3title =  ttk.Label(self.upperframe3, text = "STEP 2B - CANONICAL COORDINATES", style = "title2.TLabel")
        self.step3title.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=10)
        
        self.eqlabel3 = ttk.Label(self.upperframe3, text = "dy/dx  = ", style = "regularlabel2.TLabel")
        self.eqlabel3.grid(row=1, column=0, sticky="w", padx=(40,0), pady=3)
        
        self.equationentry3 = tk.Entry(self.upperframe3, bg = "#DAFFDA", font="Verdana 11", foreground="black", width=28)
        self.equationentry3.insert(0, "-(y^2)/3")
        self.equationentry3.grid(row=1, column=1, sticky="nswe", padx=5, pady=3)
        self.equationentry3.bind("<Button-1>", lambda event: self.delete_text(event, "warnings_step2b"))
        
        self.solvebutton3= tk.Button(self.upperframe3, text = "Solve", relief = "flat", width = 20, 
                                     bg="mediumseagreen", fg="white", activebackground="white", activeforeground="mediumseagreen",
                                     font="Helvetica 11 bold", command = self.solvestep3)
        self.solvebutton3.grid(row=1, column=2, sticky="nw", padx=10, pady=3)
        
        self.symmlabel = ttk.Label(self.upperframe3, text = "Symmetry:", style = "regularlabel2.TLabel")
        self.symmlabel.grid(row=2, column=0, sticky="w", padx=(40,0), pady=(3,10))
        
        self.inf_value3 = StringVar()
        self.infoption3 = ttk.Combobox(self.upperframe3, textvariable=self.inf_value3, state = "readonly", height = 10, width = 31, font="Helvetica 11")
        self.infoption3["values"] = inf_list
        self.infoption3.current(0)
        self.infoption3.bind("<<ComboboxSelected>>",lambda e: self.upperframe3.focus()) #Removes blue highlighting when combobox is selected
        self.infoption3.bind("<Button-1>", lambda e4: self.step3warnings.configure(text="invisible text", style="invisiblemessage2.TLabel"))
        self.infoption3.grid(row=2, column=1, sticky="nswe", padx=5, pady=(3,10))
        
        self.clearstep3button = tk.Button(self.upperframe3, text = "Clear", relief = "flat", width = 20, 
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold", command = self.clearstep3)
        self.clearstep3button.grid(row=2, column=2, sticky="nw", padx=10, pady=(3,10))
        
        #Belowframe3
        self.varlabel = ttk.Label(self.belowframe3, text = "Method B: Canonical variable change", style = "resultlabel.TLabel")
        self.varlabel.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,6), sticky="w")
        
        self.x1label = ttk.Label(self.belowframe3, text = "2.   Coordinate x1:", style = "resultlabel5.TLabel", width = 25)
        self.x1label.grid(row=1, column=0, sticky="w", padx=10, pady=(20,6))
        
        self.x1 = tk.Entry(self.belowframe3, bg = "#DAFFDA", font="Verdana 11", foreground="#6a737c", relief = "flat", width=33)
        self.x1.insert(0, "x1...")
        self.x1.grid(row=1, column=1, padx= 5, pady=(20,6))
        
        self.y1label = ttk.Label(self.belowframe3, text = "3.   Coordinate y1:", style = "resultlabel5.TLabel", width = 25)
        self.y1label.grid(row=2, column=0, sticky="w", padx=10, pady=6)
        
        self.y1 = tk.Entry(self.belowframe3, bg = "#DAFFDA", font="Verdana 11", foreground="#6a737c", relief = "flat", width=33)
        self.y1.insert(0, "y1...")
        self.y1.grid(row=2, column=1, sticky="nsw", padx=5, pady=6)
        
#         self.yprime3 = ttk.Label(self.belowframe3, text = "4.   Separable ODE:", style  ="resultlabel5.TLabel", width = 25)
#         self.yprime3.grid(row=3, column=0, sticky="w", padx=10, pady=6)
#         
#         self.separable = tk.Entry(self.belowframe3, bg = "#DAFFDA", font="Verdana 11", foreground="#6a737c", relief = "flat", width=33)
#         self.separable.insert(0, "Separable ODE...")
#         self.separable.grid(row=3, column=1, sticky="w", padx=5, pady=6)
        
        self.solutionlabel3 = ttk.Label(self.belowframe3, text = "4.   The solution is:", style  ="resultlabel5.TLabel", width = 25)
        self.solutionlabel3.grid(row=3, column=0, sticky="w", padx=10, pady=(6,10))
          
        self.solution3 = tk.Entry(self.belowframe3, bg = "#DAFFDA", font="Helvetica 12", foreground="#6a737c", relief = "flat", width=33)
        self.solution3.insert(0, "Solution appears here...")
        self.solution3.grid(row=3, column=1, sticky="nswe", padx=5, pady=(6,10))
        
        self.checksolution3 = tk.Button(self.belowframe3, text = "Check solution", relief = "flat", width = 15, 
                                     bg="cornflowerblue", fg="white", activebackground = "white", activeforeground = "cornflowerblue", 
                                     font="Helvetica 11 bold", command = self.checksol3)
        self.checksolution3.grid(row=4, column=1, padx=10, pady=(6,10))
        
        #Warnframe3
        self.step3warnings = ttk.Label(self.warnframe3, text = "invisible text", style='invisiblemessage2.TLabel')
        self.step3warnings.pack(side=LEFT, padx=5, pady=3)
        
        self.upperframe3.pack(fill=BOTH, expand=False, padx=8, pady=5)
        self.belowframe3.pack(fill=BOTH, expand=True, padx=8, pady=5)
        self.warnframe3.pack(fill=BOTH, expand=False, padx=8, pady=(2,3))

        
        
        
        
        
        
        
    # Widgets in BENCHMARK Frame
        self.upframe = ttk.Frame(self.benchmark, style="innerframe.TFrame")
        self.downframe = ttk.Frame(self.benchmark, style="innerframe.TFrame")
        
        self.upframe.pack(fill=BOTH, expand=False, padx=5, pady=5)
        self.downframe.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.test1frame = ttk.Frame(self.downframe, style="innerframe.TFrame")
        self.test2frame = ttk.Frame(self.downframe, style="innerframe.TFrame")
        
        #self.test1frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        #Upframe
        self.benchtitle =  ttk.Label(self.upframe, text = "BENCHMARK KAMKE 88 TEST", style = "title2.TLabel")
        self.benchtitle.grid(row=0, column=0, columnspan=4, sticky="w", padx = (40, 0), pady=10)
                
        self.initiallabel = ttk.Label(self.upframe, text = "Initial ODE:", style = "regularlabel2.TLabel")
        self.initiallabel.grid(row=1, column=0, sticky="w", padx=10, pady=(10,3))
        
        self.initvalue = StringVar()
        self.initode = tk.Spinbox(self.upframe, textvariable=self.initvalue, bg="linen", from_ = 1, to = 87)
        self.initode.delete(0, END)
        self.initode.insert(0, "1")
        self.initode.grid(row=1, column=1, sticky="w", padx=5, pady=(10,3))
        
        self.testlabel = ttk.Label(self.upframe, text = "Test:", style = "regularlabel2.TLabel")
        self.testlabel.grid(row=1, column=2, sticky="w", padx=10, pady=(10,3))
        
        self.test_value= StringVar()
        self.test = ttk.Combobox(self.upframe, textvariable=self.test_value, state = "readonly", font="Helvetica 11", foreground="#6a737c")
        self.test["values"] = test_list
        self.test.current(0)
        self.test.bind("<<ComboboxSelected>>",lambda e: self.upframe.focus()) #Removes blue highlighting when combobox is selected
        self.test.grid(row=1, column=3, sticky="w", padx=5, pady=(10,3))
        
        self.launchbtn = tk.Button(self.upframe, text = "Show Results", relief = "flat", bg="#CE8D4D", fg="white", font="Helvetica 11 bold", command=self.launch_benchmark) #B77E44 #CBB197
        self.launchbtn.grid(row=1, column=4, sticky="ew", padx = 5, pady=(10,3))
        
        self.finallabel = ttk.Label(self.upframe, text = "Final ODE:", style = "regularlabel2.TLabel")
        self.finallabel.grid(row=2, column=0, sticky="w", padx=10, pady=(3,10))
        
        self.finalvalue = StringVar()
        self.finalode = tk.Spinbox(self.upframe, textvariable = self.finalvalue, bg = "linen", from_ = 1, to = 88)
        self.finalode.delete(0, END)
        self.finalode.insert(0, "5") #PONER 1 POR DEFAULT
        self.finalode.grid(row=2, column=1, sticky="w", padx=5, pady=(3,10))
        
        
        #Downframe
        
        #Test1 Frame
        self.canvastest1= tk.Canvas(self.test1frame, background=mycolor)#, height=250
        myscrollbartest1 = tk.Scrollbar(self.test1frame, orient="vertical", command=self.canvastest1.yview)
        self.canvastest1.configure(yscrollcommand=myscrollbartest1.set)
        myscrollbartest1.pack(side="right", fill="y")
        self.canvastest1.pack(side="right", fill=BOTH, expand=True)
        
        self.windowtest1 = ttk.Frame(self.canvastest1, style="subframe.TFrame")
        self.canvastest1.create_window((0,0), window=self.windowtest1, anchor="nw")
        self.windowtest1.bind("<Configure>", self._lets_scroll2)
        self.windowtest1.bind('<Enter>', self._bound_to_mousewheel2)
        self.windowtest1.bind('<Leave>', self._unbound_to_mousewheel2)
        
        self.numlbl = ttk.Label(self.windowtest1, text = "Number", style = "tablelabel.TLabel")
        self.odelbl = ttk.Label(self.windowtest1, text = "ODE", style = "tablelabel.TLabel")
        self.hintlbl = ttk.Label(self.windowtest1, text = "Default Hint", style = "tablelabel.TLabel")
        self.solvablelbl = ttk.Label(self.windowtest1, text="Solvable", style = "tablelabel.TLabel")
        self.liesolvablelbl = ttk.Label(self.windowtest1, text="Lie Solvable", style = "tablelabel.TLabel")
        self.timelbl = ttk.Label(self.windowtest1, text = "Time", style = "tablelabel.TLabel")
        self.num_entrys = []
        self.ode_labels= []
        self.hint_entrys = []
        self.solvable_entrys = []
        self.liesolvable_entrys = []
        self.time_entrys = []
        
        
        
        #Test 2 Frame (HERE WE CREATE ALL THE TABLE FOREVER, only the test2frame is grided or ungrided)
        self.canvastest2= tk.Canvas(self.test2frame, background=mycolor)#, height=250
        myscrollbartest2 = tk.Scrollbar(self.test2frame, orient="vertical", command=self.canvastest2.yview)
        self.canvastest2.configure(yscrollcommand=myscrollbartest2.set)
        myscrollbartest2.pack(side="right", fill="y")
        self.canvastest2.pack(side="right", fill=BOTH, expand=True)
        
        self.windowtest2 = ttk.Frame(self.canvastest2, style="subframe.TFrame")
        self.canvastest2.create_window((0,0), window=self.windowtest2, anchor="nw")
        self.windowtest2.bind("<Configure>", self._lets_scroll3)
        self.windowtest2.bind('<Enter>', self._bound_to_mousewheel3)
        self.windowtest2.bind('<Leave>', self._unbound_to_mousewheel3)
        
        
        self.numlbl2 = ttk.Label(self.windowtest2, text = "Number", style = "tablelabel.TLabel")
        self.abaco1simple = ttk.Label(self.windowtest2, text = "abaco1_simple", style = "tablelabel.TLabel")
        self.abaco1product = ttk.Label(self.windowtest2, text = "abaco1_product", style = "tablelabel.TLabel")
        self.abaco2similar = ttk.Label(self.windowtest2, text = "abaco2_similar", style = "tablelabel.TLabel")
        self.abaco2unique = ttk.Label(self.windowtest2, text = "abaco2_unique", style = "tablelabel.TLabel")
        self.bivariate = ttk.Label(self.windowtest2, text = "bivariate", style = "tablelabel.TLabel")
        self.chi= ttk.Label(self.windowtest2, text = "chi", style = "tablelabel.TLabel")
        
        self.numlbl2.grid(row=0, column=0, sticky="nsew")
        self.abaco1simple.grid(row=0, column=1, sticky="nsew")
        self.abaco1product.grid(row=0, column=2, sticky="nsew")
        self.abaco2similar.grid(row=0, column=3, sticky="nsew")
        self.abaco2unique.grid(row=0, column=4, sticky="nsew")
        self.bivariate.grid(row=0, column=5, sticky="nsew")
        self.chi.grid(row=0, column=6, sticky="nsew")
        
        #Opening the excel table
        excel = xlrd.open_workbook("benchmarktablas.xlsx")
        tabla2 = excel.sheet_by_index(2)
        
        odenums = [1,2,3,4,5,6,7,8,9,15,17,18,19,26,29,31,42,44,60,75,76,84]
        
        self.num_entrys2 =[]
        self.ode_labels2 = []
        self.matrix=[]

        for i in range(0,22):
            
            self.matrix.append(list())
            self.num_entrys2.append(tk.Entry(self.windowtest2, relief="solid"))
            self.num_entrys2[i].insert(0, odenums[i])
            self.num_entrys2[i].grid(row=i+1, column=0, sticky="nsew")
            
            for j in range(0, 6):
                self.matrix[i].append(tk.Entry(self.windowtest2, relief="solid"))
                self.matrix[i][j].insert(0, tabla2.cell_value(2+i, 2+j) )
                self.matrix[i][j].grid(row=i+1, column=j+1, sticky="nsew")
                
                aux = self.matrix[i][j].get()
                
                if (aux == "Yes"):
                    self.matrix[i][j].configure(background="palegreen")
                elif (aux == "No"):
                    self.matrix[i][j].configure(background="#FF5733")
                    

        
        
        
    #Widgets in HELP Frame
        self.upframe3 = ttk.Frame(self.help, style="subframe.TFrame")
        self.downframe3 = ttk.Frame(self.help, style="subframe.TFrame")
        
        self.upframe3.pack(fill=BOTH, expand=False, padx=5, pady=5)
        self.downframe3.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.label25 = ttk.Label(self.upframe3, text = "HELP AREA", style = "title.TLabel")#.grid(row=0, column=0)
        self.label26 = ttk.Label(self.upframe3, text = "Sections Description", style = "subtitle.TLabel")#.grid(row=1, column=0)
        
        self.label25.pack(side=TOP)
        self.label26.pack(side=TOP)
        
        self.description = ScrolledText(self.downframe3, bg = mycolor, fg = "whitesmoke", padx = 20, pady = 10, font = "Verdana 12", height = 20)
        self.description.tag_configure("center", justify='center')
        self.description.tag_add("center", 1.0, "end")
        
        helpfile = open('description.txt', 'r')
        helplines = helpfile.readlines()
        helpfile.close()
        
        for line in helplines:
            self.description.insert(END, line)
        
        self.description.config(state=DISABLED)
        self.description.pack(fill=BOTH, expand = True)
        
        
    # Grids and configuration of all the LAYOUT
        self.grid(column=0, row=0, sticky="nsew")
        self.lateral.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.workarea.grid(row=0, column=1, columnspan=2, rowspan=2, sticky="nsew")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.workarea.grid_columnconfigure(0, weight=1)
        self.workarea.grid_rowconfigure(0, weight=1)
    
    #SHOWING THE MAIN WINDOW
        self.show_welcome()
        
        #ecuaciones de ejemplo
        # 3*dy+y^2 = 0
        # dy = cos(x)*y
        # dy = a*cos(b+y)
        # dy =2*x*y-x*exp(-x^2)
        
    def launch_benchmark(self):
        if self.test.get() == test_list[0]:
            self.launch_test1()
        
        if self.test.get() == test_list[1]:
            self.launch_test2()
    
    
    def launch_test1(self):
        
        #Packing test1, unpacking test2
        self.test2frame.pack_forget()
        self.test1frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        global height
        global prev_height
        
        #Forcing the user input to be number between 1 and 88
        try:
            prev_height = height
            
            final = int(self.finalode.get())
            inicio = int(self.initode.get())
            
            if final > 88:
                final = 88
                self.finalvalue.set("88")
            
            if inicio < 1:
                inicio = 1
                self.initvalue.set("1")
            
            height = final - inicio + 1
            
            if height < 1:
                height = 0
            
            #Very important: CLEANING THE PREVIOUS TEST 1 TABLE
            self.clear_test1(prev_height)
            
        except Exception as exc:
            print(str(exc))
        
        #Reseting all the lists
        self.num_entrys = []
        self.ode_labels= []
        self.hint_entrys = []
        self.solvable_entrys = []
        self.liesolvable_entrys = []
        self.time_entrys = []
        
        odeimages = []
        odepath=""
        
        excel = xlrd.open_workbook("benchmarktablas.xlsx")
        tabla1 = excel.sheet_by_index(0)
        
        #Griding the titles of the table
        self.numlbl.grid(row=0, column=0, sticky="nsew")
        self.odelbl.grid(row=0, column=1, sticky="nsew")
        self.hintlbl.grid(row=0, column=2, sticky="nsew")
        self.solvablelbl.grid(row=0, column=3, sticky="nsew")
        self.liesolvablelbl.grid(row=0, column=4, sticky="nsew")
        self.timelbl.grid(row=0, column=5, sticky="nsew")
        
        #Selecting the corresponding image for each ODE
        for i in range(0, height):
            try: 
                odepath = "images/odes/ode"+ str(inicio+i)+ ".png"
                print(odepath)
                odeimages.append( PhotoImage (file = odepath))
                
            except:
                odepath = "images/odes/ode_not_available.png"
                print(odepath)
                odeimages.append( PhotoImage (file = odepath))
                
            finally: #Appending the numbers and images to their lists
                self.num_entrys.append(tk.Entry(self.windowtest1, relief="solid"))
                self.ode_labels.append(tk.Label(self.windowtest1, background = "white", borderwidth=1, relief="solid", image=odeimages[i]))
                self.ode_labels[i].image = odeimages[i]
            
            #Now appending the rest of the element to each column
            self.hint_entrys.append(tk.Entry(self.windowtest1, relief="solid"))
            self.solvable_entrys.append(tk.Entry(self.windowtest1, relief="solid"))
            self.liesolvable_entrys.append(tk.Entry(self.windowtest1, relief="solid"))
            self.time_entrys.append(tk.Entry(self.windowtest1, relief="solid", background="lightgray"))
            
            #Griding each row and column in the table
            self.num_entrys[i].grid(row=i+1, column=0, sticky="nsew")
            self.ode_labels[i].grid(row=i+1, column=1, sticky="nsew")
            self.hint_entrys[i].grid(row=i+1, column=2, sticky="nsew")
            self.solvable_entrys[i].grid(row=i+1, column=3, sticky="nsew")
            self.liesolvable_entrys[i].grid(row=i+1, column=4, sticky="nsew")
            self.time_entrys[i].grid(row=i+1, column=5, sticky="nsew")
            
            #Setting up the values into the Entry boxes
            self.num_entrys[i].insert(0, int(tabla1.cell_value( int(self.initode.get())+i+1, 1)))
            self.hint_entrys[i].insert(0, tabla1.cell_value( int(self.initode.get())+i+1, 4) )
            self.solvable_entrys[i].insert(0, tabla1.cell_value( int(self.initode.get())+i+1, 2) )
            self.liesolvable_entrys[i].insert(0, tabla1.cell_value( int(self.initode.get())+i+1, 3) )
            self.time_entrys[i].insert(0, tabla1.cell_value( int(self.initode.get())+i+1, 5) )
            
            #Finally setting up the color for each "Yes" or "No"
            solv = self.solvable_entrys[i].get()
            liesolv = self.liesolvable_entrys[i].get()
            
            if (solv == "Yes"):
                self.solvable_entrys[i].configure(background="palegreen")
            elif (solv == "No"):
                self.solvable_entrys[i].configure(background="#FF5733")
                
            if (liesolv == "Yes"):
                self.liesolvable_entrys[i].configure(background="palegreen")
            elif (liesolv == "No"):
                self.liesolvable_entrys[i].configure(background="#FF5733")  
            
    def clear_test1(self, prev_height):
        
        #Ungriding each element of the table including the titles
        self.numlbl.grid_forget()
        self.odelbl.grid_forget()
        self.hintlbl.grid_forget()
        self.solvablelbl.grid_forget()
        self.liesolvablelbl.grid_forget()
        self.timelbl.grid_forget()
        
        for i in range(0, prev_height):
            
            self.num_entrys[i].grid_forget()
            self.ode_labels[i].grid_forget()
            self.hint_entrys[i].grid_forget()
            self.solvable_entrys[i].grid_forget()
            self.liesolvable_entrys[i].grid_forget()
            self.time_entrys[i].grid_forget()
    
        
    def launch_test2(self):
        #Packing the test 2, unpacking test 1
        self.test1frame.pack_forget()
        self.test2frame.pack(fill=BOTH, expand=True, padx=5, pady=5)        
    
            
    # Methods that load one or another Frame in the workarea frame
    def show_welcome(self):
        self.welcomebtn.configure(bg="gold", fg="#2a7b7c")
        self.solverbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.stepsbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.benchmarkbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.helpbtn.configure(bg = "#2a7b7c", fg = "gold")
        
        self.solver.pack_forget()
        self.stepbystep.pack_forget()
        self.benchmark.pack_forget()
        self.help.pack_forget()
        self.welcome.pack(fill = BOTH, expand=True)
        print("altura:"  + str(self.winfo_height()))
        print("ancho:"  + str(self.winfo_width()))
    
    
    def show_solver(self):
        self.welcomebtn.configure(bg = "#2a7b7c", fg = "gold")
        self.solverbtn.configure(bg="gold", fg="#2a7b7c")
        self.stepsbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.benchmarkbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.helpbtn.configure(bg = "#2a7b7c", fg = "gold")
        
        self.welcome.pack_forget()
        self.stepbystep.pack_forget()
        self.benchmark.pack_forget()
        self.help.pack_forget()
        self.solver.pack(fill = BOTH, expand=True, padx=10, pady=10)
        print("altura:"  + str(self.winfo_height()))
        print("ancho:"  + str(self.winfo_width()))
        
        
    def show_stepbystep(self):
        self.welcomebtn.configure(bg = "#2a7b7c", fg = "gold")
        self.solverbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.stepsbtn.configure(bg="gold", fg="#2a7b7c")
        self.benchmarkbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.helpbtn.configure(bg = "#2a7b7c", fg = "gold")
        
        self.solver.pack_forget()
        self.welcome.pack_forget()
        self.benchmark.pack_forget()
        self.help.pack_forget()
        self.stepbystep.pack(fill = BOTH, expand=True, padx=10, pady=10)
        print("altura:"  + str(self.winfo_height()))
        print("ancho:"  + str(self.winfo_width()))
        
        
    def show_benchmark(self):
        self.welcomebtn.configure(bg = "#2a7b7c", fg = "gold")
        self.solverbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.stepsbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.benchmarkbtn.configure(bg="gold", fg="#2a7b7c")
        self.helpbtn.configure(bg = "#2a7b7c", fg = "gold")
        
        self.solver.pack_forget()
        self.welcome.pack_forget()
        self.stepbystep.pack_forget()
        self.help.pack_forget()
        self.benchmark.pack(fill = BOTH, expand=True, padx=10, pady=10)
        print("altura:"  + str(self.winfo_height()))
        print("ancho:"  + str(self.winfo_width()))
    
    
    def show_help(self):
        self.welcomebtn.configure(bg = "#2a7b7c", fg = "gold")
        self.solverbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.stepsbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.benchmarkbtn.configure(bg = "#2a7b7c", fg = "gold")
        self.helpbtn.configure(bg="gold", fg="#2a7b7c")
        
        self.solver.pack_forget()
        self.welcome.pack_forget()
        self.stepbystep.pack_forget()
        self.benchmark.pack_forget()
        self.help.pack(fill = BOTH, expand=True, padx=10, pady=10)
        print("altura:"  + str(self.winfo_height()))
        print("ancho:"  + str(self.winfo_width()))
 
 
    #Restores the widgets in Solver to default texts and colors
    def clearsolver(self):   
        global default_text_solver
        default_text_solver = True
        self.equation.configure(foreground="#6a737c")
        self.equation.delete(0, END)
        self.equation.insert(0, "3*dy+y^2=0") #Type your equation here...
        self.solution.configure(foreground="#6a737c")
        self.solution.delete(0, END)
        self.solution.insert(0, "Solution appears here...")
        self.warnings.configure(style="invisiblemessage.TLabel")
    
    def _lets_scroll(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _lets_scroll2(self, event):
        self.canvastest1.configure(scrollregion=self.canvastest1.bbox("all"))
        
    def _lets_scroll3(self, event):
        self.canvastest2.configure(scrollregion=self.canvastest2.bbox("all"))
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def _on_mousewheel2(self, event):
        self.canvastest1.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _on_mousewheel3(self, event):
        self.canvastest2.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _bound_to_mousewheel2(self, event): 
        self.canvastest1.bind_all("<MouseWheel>", self._on_mousewheel2)
    
    def _bound_to_mousewheel3(self, event):
        self.canvastest2.bind_all("<MouseWheel>", self._on_mousewheel3)
    
    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
    def _unbound_to_mousewheel2(self, event):
        self.canvastest1.unbind_all("<MouseWheel>")
    
    def _unbound_to_mousewheel3(self, event):
        self.canvastest2.unbind_all("<MouseWheel>")    

    #Copies the equation in step1 to other step frames
    def copy_equation(self, event):
        event.widget.delete(0, END)
        event.widget.insert(0, self.equationentry.get())
    
    #Restores the widgets in Step1 to default texts and colors
    def clearstep1(self):
        
        global default_text_step1
        
        if (self.var1.get()):
            default_text_step1 = True
            self.equationentry.delete(0, END)
            self.equationentry.insert(0, "-(y^2)/3")
            self.equationentry.configure(foreground="#6a737c")
            self.var1.set(0)
        else:
            default_text_step1 = False
            
        self.heuroption.current(0)
        self.heuroption.configure(foreground="#6a737c")
        self.substituted.configure(foreground="#6a737c")
        self.substituted.delete(0,END)
        self.substituted.insert(0, "Substituted condition...")
        
        self.step1warnings.configure(text="invisible text", style="invisiblemessage2.TLabel")
        
        inf_list=[None]
        self.infoption["values"] = inf_list
        self.infoption3["values"] = inf_list
        self.infoption.current(0)
        self.infoption3.current(0)
        
        global xilist
        global etalist
        
        for i in range(0, len(xilist)):
            self.numentrys[i].grid_forget()
            self.xientrys[i].grid_forget()
            self.etaentrys[i].grid_forget()
    
    #Restores the widgets in Step2 to default texts and colors
    def clearstep2(self):
        global default_text_step2a
        default_text_step2a = True
        
        self.equationentry2.delete(0, END)
        self.equationentry2.insert(0, self.equationentry.get())
        
        #self.infoption.current(0)
        
        self.factorentry.configure(foreground="#6a737c")
        self.factorentry.delete(0, END)
        self.factorentry.insert(0, "Integrating factor...")
        
        self.exact.configure(foreground="#6a737c")
        self.exact.delete(0, END)
        self.exact.insert(0, "Exact ODE...")
        
        self.solution2.configure(foreground="#6a737c")
        self.solution2.delete(0, END)
        self.solution2.insert(0, "Solution appears here...")
        
        self.step2warnings.configure(text="invisible text", style="invisiblemessage2.TLabel")
        
    
    def clearstep3(self):
        global default_text_step2b
        default_text_step2b = True
        
        self.equationentry3.delete(0, END)
        self.equationentry3.insert(0, self.equationentry.get())
        
        #self.infoption3.current(0)
        
        self.x1.configure(foreground="#6a737c")
        self.x1.delete(0, END)
        self.x1.insert(0, "x1...")
        
        self.y1.configure(foreground="#6a737c")
        self.y1.delete(0, END)
        self.y1.insert(0, "y1...")
        
        self.separable.configure(foreground="#6a737c")
        self.separable.delete(0, END)
        self.separable.insert(0, "Separable ODE...")
        
        self.solution3.configure(foreground="#6a737c")
        self.solution3.delete(0, END)
        self.solution3.insert(0, "Solution appears here...")
        
        self.step3warnings.configure(text="invisible text", style="invisiblemessage2.TLabel")

    
    #When an entry is clicked, restores default text in its default color
    def delete_text(self, event, name):
        
        if (name == "warnings_solver"):
            
            global default_text_solver
            if (default_text_solver):
                event.widget.configure(foreground="black")
                event.widget.delete(0, END)
                self.warnings.configure(style="invisiblemessage.TLabel")
                default_text_solver = False
                
        elif (name == "warnings_step1"):
            
            global default_text_step1
            if (default_text_step1):
                event.widget.configure(foreground="black")
                event.widget.delete(0, END)
                self.step1warnings.configure(style="invisiblemessage2.TLabel")
                default_text_step1 = False
                
        elif (name == "warnings_step2a"):
            
            global default_text_step2a
            if (default_text_step2a):
                #event.widget.configure(foreground="black")
                #event.widget.delete(0, END)
                self.step2warnings.configure(style="invisiblemessage2.TLabel")
                default_text_step2a = False
                
        elif (name == "warnings_step2b"):
            
            global default_text_step2b
            if (default_text_step2b):
                #event.widget.configure(foreground="black")
                #event.widget.delete(0, END)
                self.step3warnings.configure(style="invisiblemessage2.TLabel")
                default_text_step2b = False
        
    def buildcommand(self, userinput):
                
        if '^' in userinput:
            userinput = userinput.replace('^', '**')
            
        members = userinput.split('=', 1)
        firstTerm = members[0]

        if len(members)==1:
            secondTerm="0"
        else:
            secondTerm = members[1]
        
        #The return value is the command which must be go to "my_exec(command)"
        return ("sp.Eq(" + firstTerm + "," + secondTerm + ")") 
    
    
    def simplesolver(self):
        print("Lets solve this equation")
        
        userinput = str(self.equation.get())
        sol = 0
        command = self.buildcommand(userinput)
        print(command)
        
        try:
            eq = my_exec(command)
            
            myhints = sp.classify_ode(eq, y)
            
            if 'lie_group' in myhints:
                self.warnings.configure(style = 'okmessage.TLabel', text = "Solvable by Lie group hint")
                sol = sp.dsolve(eq, func=y, hint='lie_group')
                
            else:
                auxwarn = "Not solvable by Lie. Solving with default hint" + str(myhints[0])
                self.warnings.configure(style='warningmessage.TLabel', text = auxwarn)
                sol = sp.dsolve(eq, func=y, hint='default')
            
            self.solution.configure(foreground="black")
            self.solution.delete(0, END)
            self.solution.insert(0, str(sol))
            
        except NotImplementedError as notimpl:
            print(str(notimpl))
            print("probar con dsolve sin lie_group")
            sol = sp.dsolve(eq, func=y, hint='default')
            
        except Exception as e:
            print(str(e))
            self.warnings.configure(style='errormessage.TLabel', text = "Not solvable")
            
    
    def substitute(self, hache):
        
        x = sp.symbols('x')
        h = sp.symbols('h')
        y= sp.symbols('y')
        hx = sp.symbols('hx')
        hy = sp.symbols('hy')

        hache = sympify(hache)
        hachex = hache.diff(x)
        hachey = hache.diff(y)

        cond = "etax - xiy*h**2 + (etay - xix)*h - (eta*hx + xi*hy)"
        cond = sympify(cond) 
        cond = cond.subs([(h, hache), (hx, hachex), (hy, hachey)])
        strcond = str(cond) + " = 0"
        
        
        self.substituted.configure(foreground="black")
        self.substituted.delete(0, END)
        self.substituted.insert(0, strcond)
        
      
    def obtinfinitesimals(self):
        try:
            userinput = str(self.equationentry.get())
            
            if '^' in userinput:
                userinput = userinput.replace('^', '**')
            
            command= "sp.Eq(" + "dy" + "," + userinput + ")"
            
            eq = my_exec(command)
            
            userheur = self.heuroption.get()
            
            symmetries = sp.ode.infinitesimals(eq, hint=userheur, func=y)
            global xilist
            global etalist
            xilist = [j[fxi] for j in symmetries]
            etalist = [k[feta] for k in symmetries]
            
            self.substitute(userinput)
            
            if len(xilist) == len(etalist):
                
                global inf_list
                inf_list=[]
                desplegable = ""
                
                for i in range(0, len(xilist)):
                    
                    desplegable = "Xi = " + str(xilist[i]) + ", Eta = " + str(etalist[i])
                    
                    inf_list.insert(i, desplegable)
                    inf_index.insert(i, str(i))                    
                    self.infoption["values"] = inf_list
                    self.infoption3["values"] = inf_list
                    
                    self.numentrys.append(tk.Entry(self.window, bg = "lightsalmon", font="Verdana 12", width=8))
                    self.numentrys[i].grid(row=i+1, column=0, sticky="w", padx=10, pady=6)
                
                    self.numentrys[i].delete(0, END)
                    self.numentrys[i].insert(0, str(i+1))
                                 
                    self.xientrys.append(tk.Entry(self.window, bg = "peachpuff", font="Verdana 12", width=16))
                    self.xientrys[i].grid(row=i+1, column=1, sticky="w", padx=10, pady=6)
                    
                    self.xientrys[i].delete(0, END)
                    self.xientrys[i].insert(0, str(xilist[i]))
                    
                    self.etaentrys.append(tk.Entry(self.window, bg = "peachpuff", font="Verdana 12", width=16))
                    self.etaentrys[i].grid(row=i+1, column=2, sticky="w", padx=10, pady=6)
                    
                    self.etaentrys[i].delete(0, END)
                    self.etaentrys[i].insert(0, str(etalist[i]))
                    
                self.step1warnings.configure(text = "Infinitesimals succesfully calculated", style="okmessage2.TLabel")
                
                #The introduced ode is copied to the steps 2A y 2B to work with it after
                self.equationentry2.delete(0, END)
                self.equationentry2.insert(0, self.equationentry.get())
                    
                self.equationentry3.delete(0, END)
                self.equationentry3.insert(0, self.equationentry.get())
                    
                 
        except Exception as e:
            print(str(e))
            self.step1warnings.configure(text = "Error calculating infinitesimals", style="errormessage2.TLabel")
        
    
    def solvestep2(self):   #FALTA CALCULAR Y SUSTITUIR EL FACTOR INTEGRANTE Y LA ODE EXACTA
        sol=0
        try:
            
            userinput = str(self.equationentry2.get())
            
            if '^' in userinput:
                userinput = userinput.replace('^', '**')
            
            command= "sp.Eq(" + "dy" + "," + userinput + ")"
            
            eq = my_exec(command)
            
            #The infinitesimals chosen by the user among previously obtained
            userinfs = int(self.infoption.current())
            xi = xilist[userinfs]
            eta = etalist[userinfs]
            
            sol = sp.dsolve(eq, func=y, hint='lie_group', xi=xi, eta=eta)
            
            self.solution2.configure(foreground="black")
            self.solution2.delete(0, END)
            self.solution2.insert(0, str(sol))
            
            self.step2warnings.configure(text = "Solution succesfully calculated", style="okmessage2.TLabel")
            
        except Exception as e:
            print(str(e))
            self.step2warnings.configure(text = "Error calculating solution", style="errormessage2.TLabel")
            
    def solvestep3(self):   #FALTA CALCULAR Y SUSTITUIR LAS COORDENADAS CANONICAS Y LA ODE SEPARABLE
        sol=0
        try:
            
            userinput = str(self.equationentry3.get())
            
            if '^' in userinput:
                userinput = userinput.replace('^', '**')
            
            command= "sp.Eq(" + "dy" + "," + userinput + ")"
            
            eq = my_exec(command)
            
            #The infinitesimals chosen by the user among previously obtained
            userinfs = int(self.infoption.current())
            xi = xilist[userinfs]
            eta = etalist[userinfs]
            
            sol = sp.dsolve(eq, func=y, hint='lie_group', xi=xi, eta=eta)
            
            self.solution3.configure(foreground="black")
            self.solution3.delete(0, END)
            self.solution3.insert(0, str(sol))
            
            self.step3warnings.configure(text = "Solution succesfully calculated", style="okmessage2.TLabel")
            
        except Exception as e:
            print(str(e))
            self.step3warnings.configure(text = "Error calculating solution", style="errormessage2.TLabel")
    
    def checksol2(self):
        
        try:
            userinput = str(self.equationentry2.get())
            if '^' in userinput:
                userinput = userinput.replace('^', '**')
             
            command= "sp.Eq(" + "dy" + "," + userinput + ")"
            eq = my_exec(command)
            
            output = str(self.solution2.get())
            if 'y(x)' in output:
                output = output.replace('y(x)', 'y')
            
            mysol = my_exec("sp." + output)
            
            print("Funcionando...")
        
            print(sp.checkodesol(eq, mysol))
            print("Yes")
            self.step2warnings.configure(text = "The solution verifies the ODE", style="verifiedmessage.TLabel")
            
        except Exception as e:
            self.step2warnings.configure(text = "This solution does not verify the equation", style="errormessage2.TLabel")
            print("No")
            print(str(e))
            
            
    def checksol3(self):
        try:
            userinput = str(self.equationentry3.get())
            if '^' in userinput:
                userinput = userinput.replace('^', '**')
            
            command= "sp.Eq(" + "dy" + "," + userinput + ")"
            eq = my_exec(command)
            
            output = str(self.solution3.get())
            if 'y(x)' in output:
                output = output.replace('y(x)', 'y')
            
            mysol = my_exec("sp." + output)
            
            print("Funcionando...")
        
            print(sp.checkodesol(eq, mysol))
            print("Yes")
            self.step3warnings.configure(text = "The solution verifies the ODE", style="verifiedmessage.TLabel")
            
        except Exception as e:
            self.step3warnings.configure(text = "This solution does not verify the equation", style="errormessage2.TLabel")
            print("No")
            print(str(e))

    def play(self):
        pygame.mixer.music.load('msound.mp3')
        pygame.mixer.music.play()
#         