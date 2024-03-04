import os 

def checkInput(type, message):
    while (True):
        try:
            data = input(f"{message} :> ")
            if(type == "int"):
                data = int(data)
                if data < 0 :
                    raise ValueError
            elif(type == "float"):
                data = float(data)
                if data < 0 :
                    raise ValueError
            elif(type == "str"):
                data = data.lower()
        except ValueError:
            showError("Error al Ingresa el Dato Intentalo de Nuevo")
        else:
            if(type == "str")and(len(data) < 1):
                showError("Error al Ingresa el Dato Intenta Ingresar Datos Reales")
            else:
                return data
            
def showError(message):
    os.system("cls")
    print("\033[91m{}\033[00m" .format(message))
    os.system("pause")

def yesORnot(message):
    os.system("cls")
    while(True):
        continuar = checkInput("str", f"{message} Si(s) o No(n)").lower()
        if continuar == "s":
            return True
        elif continuar == "n":
            return False
        else:
            showError("Error Opcion no Reconocida Ingresa s para (Si) o n Para (No)")

def showSuccess(message):
    os.system("cls")
    print("\033[92m{}\033[00m" .format(message))
    os.system("pause")