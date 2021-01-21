#le fichier sera code.mg
from ClassCommand import *

interpret_status = {"isBasicDefined":False}

def splitBetweenCommandAndArgument(line):
    splited_line=line.split("$") #Le premier argument est la commande + un espace ou pas + le préfix
    print(splited_line)
    #print(splited_line)
    for i in splited_line:
        i.replace(" ","") #Pour se débarasser des espaces et avoir préfix + commande
    return splited_line
    
    #Pour le "if", faire en sorte que sa calcule les arguments et que sa répondent True ou False dans le if

def unindentedCommandManager(line):
    splited_line = splitBetweenCommandAndArgument(line)
    command = splited_line[0]

        # /!\ Le programme considère le préfix des boucles comme un argument et bloque donc le vrai argument

    for i in instances:
        #print(command)
        if(i.isCommand(command)):
            i.call()

def fetch_code(file):
    with open(f"{file}.mg", "r") as f:
        script_unsplited = f.read()
        script = script_unsplited.split("\n")
    return script

def interpret_code(script):
    for i in range(len(script)):
        line = script[i]
        if(line.startswith("!")):
            unindentedCommandManager(line)
        
        

if __name__=="__main__":
    interpret_code(fetch_code("code"))