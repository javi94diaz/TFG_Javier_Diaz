"""
Delhi Benchmark with KAMKE 88. Attached file pruebaX.txt
"""

from io import BytesIO

from sympy.printing.mathml import mathml
from sympy.core import sympify
from sympy.solvers.ode import allhints
import sympy as sp

import time
import datetime
import multiprocessing

from delhiSymbols import *


class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


# Saves received expression into a PNG image file #NOT USED YET
def savePNG (expr, fileName):
    
    bytesIOfile=BytesIO()
    sp.preview(expr, output='png', viewer='BytesIO', euler=False, outputbuffer=bytesIOfile)
    with open(fileName,"bw") as fPNG:
        fPNG.write(bytesIOfile.getvalue())
    bytesIOfile.close()

# Saves a list of registered times in a file
def saveTimes (timeDef, timeLie, fileName):
        
    with open(fileName, "w") as f:
        f.write("*Default*\t*Lie group*\n")
        for i in range(0, len(timeDef)):
            f.write(str(timeDef[i]) + "\t\t" + str(timeLie[i]) + "\n")
    
    print("Times succesfully saved")

# Replaces the MathML Leibniz notation (dy/dt) for derivatives with Newton notation (y')
def replaceDeriv(transfStr, var):
    preInputDeriv="<mfrac><mrow><mo>&dd;</mo></mrow><mrow><mo>&dd;</mo><mi>x</mi></mrow></mfrac><mrow><mi>"
    postInputDeriv="</mi>"
    preOutputDeriv="<mrow><mi>"
    postOutputDeriv="</mi><mo lspace='0px' form='infix'>'</mo>"
    
    derivLeibniz=preInputDeriv+var+postInputDeriv
    derivNewton=preOutputDeriv+var+postOutputDeriv
    transfStr=transfStr.replace(derivLeibniz,derivNewton)
    
    return transfStr


# Replaces deprecated <mfenced> tags
def decorMML(strMML):
    
    transfStr=strMML
    
    fence="<mi>y</mi><mfenced><mi>x</mi></mfenced>"
    transfFence="<mi>y</mi>"
    transfStr=transfStr.replace(fence,transfFence)
    
    #fencef="<mi>f</mi><mfenced><mi>x</mi></mfenced>"
    #transfFencef="<mi>f</mi>"    
    #transfStr=transfStr.replace(fencef,transfFencef)
    
    transfStr=replaceDeriv(transfStr, "y")
    transfStr=replaceDeriv(transfStr, "f")
    transfStr=replaceDeriv(transfStr, "g")
    
    #transfStr=strMML
    return transfStr


def obtainHints(ODE):
    
    hints = sp.classify_ode(ODE, y)
    print("\nPossible hints:")
    for hint in hints:
        print("\t" + str(hints.index(hint)+1), end=': ')
        print(hint)
    return hints

#Saves the list of hints for each ODE into a text file
def saveHints(fileName, numODE, hints):
    
    with open(fileName, "a") as myfile:
        myfile.write(str(numODE))
        for i in allhints:
            if i in hints:
                myfile.write("\tYes")
            else:
                myfile.write("\tNo")
        myfile.write("\n")


#Obtaining the infinitesimal group xi and eta with all lie heuristics
def obtainInfinitesimals(ODE, hints):
    
    auxvalid = [] #reseting the auxiliary list
    if 'lie_group' in hints:
        for heuristic in lie_heuristics:
            try:
                print("With " + heuristic + ":\n")
                symmetries = sp.ode.infinitesimals(ODE, hint=heuristic, func=y)
                print(symmetries)
                auxvalid.append("Yes")
                
                xilist = [j[fxi] for j in symmetries]
                etalist = [k[feta] for k in symmetries]
                 
                if len(xilist) == len(etalist):
                    for i in range(0, len(xilist)):
                        print("xi" + str(i) + ": " + str(xilist[i]))
                        print("eta" + str(i) + ": " + str(etalist[i]))
                
            except Exception as e:
                print("\n\t" + str(e))
                auxvalid.append("No")
                continue
                
    return auxvalid, xilist, etalist
    
#Saves the list of valid and invalid heuristics for a given ODE
def saveHeuristics(fileName, numODE, auxvalid):
    
    with open(fileName, "a") as myfile:
        myfile.write(str(numODE))
        for i in auxvalid:
            myfile.write("\t" + i)
        myfile.write("\n")

#Generating an output MathML file (.mml) with the solution of the ODE
def saveMathML (expr, fileName):
    
    strMML=mathml(expr,printer='presentation')
    strMML=decorMML(strMML)
    with open(fileName,"w") as fMML:
        fMML.write(strMML)

#Attempts to solve an ode with all possible hints proposed by sympy's classify_ode method
def solveAll(ODE, y, numODE, hint):
    
    solution = sp.dsolve(ODE, func=y, hint=hint)
    print("Solution of ODE " + str(numODE) + " with " + hint + " hint: ", end = '')
    print(solution)

#Attempts to solve an ode with 'lie_group' hint and returns the solution and the execution time
def solveODELie(ODE, y, numODE, hints):
    
    solutionLie = 0     
    if 'lie_group' in hints:
        try:
            print("Solving with Lie group hint...")
            timeLie0= time.perf_counter()
            solutionLie=sp.dsolve(ODE, func=y, hint='lie_group')
            print("Solution of ODE " + str(numODE) + " with Lie group hint: ", end = '')
            print(solutionLie)
            #sp.pprint(solutionLie) # Pretty printing the solution
              
        except Exception as e:
            print("NOPE: ", end = '')
            print(str(e))
              
        finally:
            timeLie1 = time.perf_counter() - timeLie0
            print("Time elapsed Lie: {:.2f} seconds".format(timeLie1))
            timeExecLie.append("{:.2f}".format(timeLie1))
              
            #Adding a line to the times file
            with open("times.txt", "a") as myfile:
                myfile.write("\t\t{:.2f}\n".format(timeLie1))
    else:
        print("Not solvable by the Lie group hint")
    
    return solutionLie, timeExecLie


#Solves an ode with 'dsolve' and returns the solution and the execution time
def solveODE(ODE, y, numODE):
    
    solution=""
    print("Solving with default hint...")
    t0 = time.perf_counter()
    try:
        solution = sp.dsolve(ODE, func=y)
        print("Solution of ODE " + str(numODE) + " with default hint: ", end = '')
        print(solution)
        
    except Exception as e:
        print(str(e))
        solution=sp.Eq(1,1, evaluate=False)
     
    timeExecODE = time.perf_counter() - t0
    
    return solution, timeExecODE


#Returns an ODE as a sympy Eq with simplified members
def createODE(strODE):
    
    members=strODE.split('=')
    lhs=sympify(members[0])
    rhs=sympify(members[1])
    ODE=sp.Eq(lhs,rhs)
    print(ODE)
    return ODE


# Receives a line from a text file and outputs the ODE and its number
def analyzeLine(line):
   
    blankLine=False
    numLine=-1
    strODE=""
    
    lineComponents=line.split()

    if len(lineComponents)>0:
            linecode = lineComponents[0]              # The first "word" of the split line: it can be a number or a line like /*****
    else:
            blankLine=True
            
    isComment = blankLine or (linecode[0:2]=='/*')    # A line is considered as a comment if it starts with /* or it is empty
    if not isComment:
        numLine=int(lineComponents[0])                #Saves the number of the ODE
        strODE=lineComponents[1].rstrip("\n")         #Saves the ODE removing the final \n character
        
    return isComment, numLine, strODE


#Asks the user for a number and returns it as an int
def inputNum(prompt="Introduzca numero:"):
    
    userInput = input(prompt)
    if userInput !="":
        return int(userInput)
    else:
        return 0
 

# Main function
def main():
    
    sp.init_printing()

    startODE = inputNum("Initial ODE:")
    finalODE = inputNum("Final ODE:")
    
    while startODE > finalODE:
        startODE = inputNum("Initial ODE:")
        finalODE = inputNum("Final ODE:")
    
    #Parsing the file containing the ODEs
    file = open('kamke88.txt', 'r')
    Lines = file.readlines()
    file.close()
    
    #Creating the file to save solving times
    with open("times.txt", "w") as f:
        f.write("*Default*\t*Lie group*\n")
        
    #Creating file to save hints of each ODE
    with open("odehints.txt", "w") as f:
        f.write("Number")
        for elem in allhints:
            f.write("\t" + elem)
        f.write("\n")
    
    #Creating file to save Lie heuristics
    with open("heuristics.txt", "w") as f:
        f.write("Number")
        for heuristic in lie_heuristics:
            f.write("\t" + heuristic)
        f.write("\n")
    
    timeTotal0 = time.perf_counter()    #Registers the total execution time for the ODEs indicated by the user
    currentLine = 0                     #Used to parse the whole file line by line
    numODE = 0                          #Indicates the number of the current analyzed and solved ODE
    
    
    lista = []
    
    while numODE < finalODE:
        
    #Analyzing current line. If it is empty or a comment, it is ignored. If not, an ODE is saved in strODE
        isComment,numODE,strODE=analyzeLine(Lines[currentLine])
        currentLine+=1
        
    #Ignoring current line if it is empty, a comment, or a previous ODE than starter one (startODE)
        passLine = isComment or (numODE<startODE)
        if passLine:
            continue
        
    #Creating an ODE object from previously read strODE 
        ODE=createODE(strODE)
        print("\nODE {}: {}".format(numODE, strODE))
        #saveMathML(ODE, "mmlODE/ODE{}.mml".format(numODE)) 
        
        #hints = obtainHints(ODE)  
        #saveHints("odehints.txt", numODE, hints)
        
        try:
            result = sp.ode.infinitesimals(ODE, func=y, hint='default')
            lista.append(result)
        except Exception as e:
            print(str(e))
            lista.append(numODE)
            print("No puede")
        
        #auxvalid, xilist, etalist = obtainInfinitesimals(ODE, hints)
        #saveHeuristics("heuristics.txt", numODE, auxvalid)
         
        #solution,timeExecODE = solveODE(ODE,y, numODE)
        #saveMathML(solution, "mmlSOLUTION/SOL{}.mml".format(numODE))
        
    #Saving time measurements
        #timeExec.append("{:.2f}".format(timeExecODE))
        #print("Time elapsed dsolve: {:.2f} seconds".format(timeExecODE))
           
        #with open("times.txt", "a") as myfile:
        #    myfile.write("{:.2f}".format(timeExecODE))
        
#         solutionLie, timeExecLie = solveODELie(ODE, y, numODE, hints)
#         saveMathML(solutionLie, "mmlSOLUTIONLIE/SOL{}.mml".format(numODE))
           
        #solving all     
#         print("Solving with ALL hints...")
#      
#         for hint in hints:
#             try:
#                 p = multiprocessing.Process(target = solveAll(ODE, y, numODE, "lie_group"))
#                 p.start()
#                 #print("Multiprocessing started")
#                  
#                 #Waiting 5 seconds while process is running
#                 p.join(5)
#                   
#                 if p.is_alive():
#                     print ("Current hint still running... let's skip it...")
#                      
#                 p.terminate()
#                 p.join()
#                  
#             except Exception as e:
#                 print(str(e))
    #END OF WHILE LOOP
    
    #Showing total execution time and saving each ODE execution time in a file
    #timeTotal1 = time.perf_counter() - timeTotal0
    #print("\nTOTAL Time elapsed: {:.2f}".format(timeTotal1))
    

if __name__ == "__main__":
    main()