#le fichier sera code.mg
from ClassCommand import *
variables = {}

def splitBetweenCommandAndArgument(line):
    splited_line=line.split("$") #Le premier argument est la commande + un espace ou pas + le préfix
    return splited_line
    
    #Pour le "if", faire en sorte que sa calcule les arguments et que sa répondent True ou False dans le if

def unindentedCommandManager(line):
    splited_line = splitBetweenCommandAndArgument(line)
    command = splited_line[0].replace(" ","")
    arguments = []
    for i in range(len(splited_line)-1):
        arguments.append(splited_line[i+1])

    for i in instances:
        if(i.isCommand(command)):
            i.call(arguments)

def fetch_code(file):
    with open(f"{file}.mg", "r") as f:
        script_unsplited = f.read()
        script = script_unsplited.split("\n")
    return script

def interpret_code(script):
    for i in range(len(script)):
        line = script[i]
        if(line.startswith("!")): #ATTENTION DU COUP A CAUSE DE SA LES PREFIXS CUSTOMS DE MARCHENT PAS !
            unindentedCommandManager(line)
        
        

if __name__=="__main__":
    interpret_code(fetch_code("script"))