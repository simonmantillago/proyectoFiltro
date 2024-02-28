import sys
import os
import json
import modules.reusable as rs
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
        
        
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)
        
def delData(*params):
    op = params[0]
    data = params[1]
    delVal = input(f"Ingrese el codigo de {op} que desea borrar -> ")
    if delVal in data[op]:
        data[op].pop(delVal)
        UpdateFile('inventario.json',data)
        rs.showSuccess('Se ha eliminado correctamente')
        clear_screen()
        
    else:
        rs.showError('Ese codigo no se encuentra en la base de datos')
        clear_screen()

def addActivo():
    pass