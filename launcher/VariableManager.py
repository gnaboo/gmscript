import logging

variable = {}

def log(message, user="root"):
    logging.basicConfig(filename=f'logs.log' , filemode='a', format=f'{user} - %(asctime)s %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.error(message)

def createVariable(name, value):
    try:
        variable[name] = value
        log(f"\"{name}\" was created")
    except:
        print(f"NameError: {name} cannot be created")
        log(f"NameError: {name} cannot be created")

def getVariable(name):
    try:
        log(f"\"{name}\" was asked for")
        return variable[name]
    except:
        log(f"NameError: {name} is not defined")
        return f"NameError: {name} is not defined"


