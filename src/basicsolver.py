
import sympy as sp
from sympy.printing.mathml import print_mathml
from sympy.printing.mathml import mathml
from math import *
import math
from sympy import sin, cos, tan, sinh, cosh, tanh, exp, log, atan

from sympy.core import sympify

from delhiSymbols import *

# x, a0, a1, a2, a3, a4, a, b, c= sp.symbols('x a0 a1 a2 a3 a4 a b c')
# 
# y = sp.Function('y')(x)
# f = sp.Function('f')(x)


# odes = []
# odes.append( sp.Eq(y.diff(x)-(a4*x**4+a3*x**3+a2*x**2+a1*x+a0)**(-1/2), 0) )
# odes.append( sp.Eq(y.diff(x)+ a*y - c*(sp.exp(b*x)) , 0) )

# lie_heuristics = (
#     "abaco1_simple",
#     "abaco1_product",
#     "abaco2_similar",
#     "abaco2_unique_unknown",
#     "abaco2_unique_general",
#     "linear",
#     "function_sum",
#     "bivariate",
#     "chi"
#     )
# 
# 
# infinits = {}
# lista = []
# 
# print("Without given hint:\n")
# print( sp.ode.infinitesimals(odes[1]))
# 
# for heuristic in lie_heuristics:
#     try:
#         print("With " + heuristic + ":\n")
#         lista = sp.ode.infinitesimals(odes[0], hint=heuristic)
#         print("La lista: ")
#         print(lista)
#         infinits = lista[0]
#         xi = infinits[0]
#         eta = infinits[1]
#         print(xi)
#         print(eta)
#  
#     except Exception as e:
#         print("\t" + str(e))
#         continue


# ode3 = sp.Eq(y.diff(x)+ a*y - b*(sp.sin(c*x)), 0)
# ode4 = sp.Eq(y.diff(x)+ 2*x*y - x*(sp.exp(-x**2)), 0) 
# ode5 = sp.Eq(y.diff(x)+ y*sp.cos(x)-sp.exp(2*x), 0)
# ode6 = sp.Eq(y.diff(x)+ y*sp.cos(x)-1/2*sp.sin(2*x) ,0) 
# ode7 = sp.Eq(y.diff(x)+ y*sp.cos(x)-sp.exp(-sp.sin(x)) , 0)
# ode8 = sp.Eq(y.diff(x)+ y*sp.tan(x)-sp.sin(2*x), 0)
# ode9 = sp.Eq(y.diff(x)- y*( sp.sin(sp.log(x)) + sp.cos(sp.log(x)) + a ), 0)
# ode10 = sp.Eq(y.diff(x) + y+ f.diff(x) - f*f.diff(x), 0)
# 
# ode16 = sp.Eq(y.diff(x)+y**2+(x*y-1)*y, 0)
# 
# for i in range(0, len(odes)):
#      
#     hints = sp.classify_ode(odes[i], y)
#     print("\nPossible hints for the " + str(i+1) + " equation: ") 
#     for hint in hints:
#         print("\t" + str(hints.index(hint)+1), end=': ')
#         print(hint)
#  
#     for current_hint in hints:
#         print("Solving with hint: " + current_hint)
#         try:
#             print(sp.dsolve(odes[i], y, hint = current_hint))
#         except:
#             print("Not valid hint for this equation")
#      
#     print("\nBenchmark finished succesfully")

myode = sp.Eq(y.diff(x)-a*cos(y+b), 0)
mysol = sp.Eq(y, -b - 2*atan((C1 + exp(a*x))/(C1 - exp(a*x))))

print("Funcionando...")

try:
    print(sp.checkodesol(myode, mysol))
    print("Yes")
except Exception as e:
    print(str(e))