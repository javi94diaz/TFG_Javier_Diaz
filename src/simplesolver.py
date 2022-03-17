# Solver button command method

# dy+7*y=0
# solution:

# dy+y*cos(x)=1/2*sin(2*x)
# solution:  Eq(y(x), C1*exp(-sin(x)) + 1.0*sin(x) - 1.0)


# dy=(sin(log(x))+cos(log(x))+a)*y
# solution: Eq(y(x), C1*exp(x*(a + sin(log(x)))))

import sympy as sp
from sympy import sin, cos, tan, sinh, cosh, tanh, exp, log
from delhiSymbols import *
from sympy.core import sympify

aux = "" #for simple solver, in my_exec function ESTABA EN delhiSymbols

def my_exec(code):
    exec("global aux; aux= %s" % code)
    return aux

def simplesolver():
    
    userinput = input("Type your equation: ")
    
    if '^' in userinput:
        userinput = userinput.replace('^', '**')
        print(userinput)
    
    members = userinput.split('=', 1)
    firstTerm = members[0]
    
    if len(members)==1:
        secondTerm="0"
    else:
        secondTerm = members[1]
    
    command = "sp.Eq(" + firstTerm + "," + secondTerm + ")"
    eq = my_exec(command)
    
    print("Let's solve this equation")
        
    hints = sp.classify_ode(eq, y)
    sol = ''
 
    if 'lie_group' in hints:
        print("Solvable by Lie group hint")
        sol = sp.dsolve(eq, func=y, hint='lie_group')
        print(sol)
        
    else:
        print("Not solved by Lie group hint")
        sol = sp.dsolve(eq, func=y)
        print(sol)

def sustituir():
    
    x = sp.symbols('x')
    h = sp.symbols('h')
    y= sp.symbols('y')
    
    etax =sp.symbols('etax')
    etay =sp.symbols('etay')
    xix =sp.symbols('xix')
    xiy =sp.symbols('xiy')
    
    hx = sp.symbols('hx')
    hy = sp.symbols('hy')
    
    hache = "cos(x)*y"
    hache = sympify(hache)
    print(hache)
    
    hachex = hache.diff(x)
    hachey = hache.diff(y)
    
    print(hachex)
    print(hachey)
    
    cond = "etax - xiy*h**2 + (etay - xix)*h - (eta*hx + xi*hy)"
    cond = sympify(cond)
    
    cond = cond.subs([(h, hache), (hx, hachex), (hy, hachey)])
    print(cond)
    
    strcond = str(cond) + " = 0"
    print(strcond)
    
    

if __name__ == "__main__":
    sustituir()