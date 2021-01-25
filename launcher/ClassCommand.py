from VariableManager import *
instances = []

class _Command:
    def __init__(self, name: str, id: int, alias: list, default: bool = True, caracter: str = "!"):
        self.name=name
        self.alias=alias
        self.default=default
        self.caracter=caracter
        self.id=id
        instances.append(self)

    def setCaracter(self, caracter: str):
        self.caracter=caracter            

    def isCommand(self, input):
        if(input == str(self.caracter+self.name)):
            return True
        else:
            for i in self.alias:
                if(input == self.caracter+i):
                    return True
        return False

    def call(self, moreDetails = None):
        if(self.id == 0):
            stringToPrint = ""
            try: #C'est une liste !
                moreDetails[0]
                for i in moreDetails:
                    stringToPrint = stringToPrint + str(i)

                moreDetails = stringToPrint.split(" ")
                for i in range(len(moreDetails)):
                    if(moreDetails[i].startswith("%")):
                        if(not (getVariable(moreDetails[i][1:]).startswith("NameError"))):
                            moreDetails[i] = getVariable(moreDetails[i][1:])
                        stringToPrint = " ".join(moreDetails)

            except: #C'est une string !
                stringToPrint = "InternalUnknownError. Please contact the developers"
            print(stringToPrint)

        elif(self.id == 1):
            stringToPrint = ""
            try: #C'est une liste !
                moreDetails[0]
                for i in moreDetails:
                    stringToPrint = stringToPrint + str(i)

                moreDetails = stringToPrint.split(" ")
                for i in range(len(moreDetails)):
                    if(moreDetails[i].startswith("%")):
                        if(not (getVariable(moreDetails[i][1:]).startswith("NameError"))):
                            moreDetails[i] = getVariable(moreDetails[i][1:])
                        stringToPrint = " ".join(moreDetails)

            except: #C'est une string !
                stringToPrint = "InternalUnknownError. Please contact the developers"
            print(stringToPrint, end="")

        elif(self.id == 2):
            data1 = "".join(moreDetails)
            data = data1.split(":")
            variableName = data[0]
            valueInAVariable = data[1]
            createVariable(variableName, valueInAVariable)


printCommand = _Command("print", 0, ["PRINT", "Print", "echo"], True)
printfCommand = _Command("printf", 1, ["PRINF", "Printf", "PrintF"], True)
setVariableCommand = _Command("set", 2, ["SET", "Set", "setvar", "SETVAR", "SetVar"], True)