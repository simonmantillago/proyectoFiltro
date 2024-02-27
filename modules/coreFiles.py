import sys
import os
import json
BASE="data/"

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")  
        
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)    