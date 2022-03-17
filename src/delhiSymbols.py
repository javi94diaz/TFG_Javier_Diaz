#Defines necessary symbols and variables to work with
import sympy as sp

# Independent variable
x = sp.symbols('x')

#Functions
y = sp.Function('y')(x)
h = sp.Function('h')(x)
f = sp.Function('f')(x)
g = sp.Function('g')(x)

t = sp.Function('t')(x)



fxi = sp.Function('xi')(x, y)
feta = sp.Function('eta')(x, y)

dy = y.diff(x) # dy/dx


#Symbols
a=sp.symbols("a")
b=sp.symbols("b")
c=sp.symbols("c")
C1=sp.symbols("C1")

A=sp.symbols("A")
B=sp.symbols("B")

n=sp.symbols("n")
m=sp.symbols("m")


a4=sp.symbols("a4")
a3=sp.symbols("a3")
a2=sp.symbols("a2")
a1=sp.symbols("a1")
a0=sp.symbols("a0")

b4=sp.symbols("b4")
b3=sp.symbols("b3")
b2=sp.symbols("b2")
b1=sp.symbols("b1")
b0=sp.symbols("b0")

alpha=sp.symbols("alpha")
beta=sp.symbols("beta")
phi=sp.symbols("phi")

f3=sp.symbols("f3")
f2=sp.symbols("f2")
f1=sp.symbols("f1")
f0=sp.symbols("f0")

# Global variables
timeExec = []           # List of execution times for default hint in dsolve
timeExecLie = []        # List of execution times for lie_group hint in dsolve
hints = []              # List of hints returned by sympy.classify_ode
validheur = []          # This list stores "Yes" or "No" whether an heuristic is valid for an ODE or not
symmetries = []         # Used to store the result of sp.infinitesimals(...) in benchmarkv5.py
xilist = []             # List of obtained Xi functions
etalist = []            # List of obtained Eta functions

#For SOLVER
default_text_solver = True
default_text_step1 = True
default_text_step2a = True
default_text_step2b = True

#For Step-by-step
inf_list = ["None"] #para step 2 y 3
inf_index = ["0"]
test_list = ["1 (Default solution)", "2 (Lie Heuristics)"] #para benchmark

lie_heuristics = [
    "default",
    "abaco1_simple",
    "abaco1_product",
    "abaco2_similar",
    "abaco2_unique_unknown",
    "abaco2_unique_general",
    "linear",
    "function_sum",
    "bivariate",
    "chi"
    ]

#For benchmark
height = 0
prev_height = 0


