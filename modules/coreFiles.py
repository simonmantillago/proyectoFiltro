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