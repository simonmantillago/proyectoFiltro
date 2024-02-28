import sys
import os
import json
BASE="data/"

def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")

def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")  
        
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)    

def readDataFile(archivo):
    with open(BASE+archivo,"r+") as rf:
        return json.load(rf)

def addData(archivo,data):
    with open(BASE+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)

def listarTodosActivos(activos)
for codigo, detalles in activos.items():
    print(f"Codigo: {codigo}")
    for clave, valor in detalles.items():
        print(f"{clave.capitalize()}: {valor}")
         print("-----------------------------")

def listarActivosCategoria(activos, categoria):
    for codigo, detalles in activos.items():
        if detalles["categoria"] == categoria:
            print(f"Código: {codigo}")
            for clave, valor in detalles.items():
                print(f"{clave.capitalize()}: {valor}")
            print("-----------------------------")

def listarActivosDaño(activos):
    for codigo, detalles in activos.items():
        if detalles["estado"] == "Dado de baja por daño":
            print(f"Código: {codigo}")
            for clave, valor in detalles.items():
                print(f"{clave.capitalize()}: {valor}")
            print("-----------------------------")
