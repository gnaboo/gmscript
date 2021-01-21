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

    def call(self):
        if(self.id == 0):
            print("OUI !")


printCommand = _Command("print", 0, ["PRINT", "Print", "echo"], True)

"""class CustomCommand(_Command):
    def __init__(self, name: str, alias: list, caracter: str = "!"):
        super().__init__(name, alias, False, caracter)"""