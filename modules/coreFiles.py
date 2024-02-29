import sys
import os
import json
BASE="data/"
from tabulate import tabulate

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
#funciones de reportes 
def listarActivos(data_inventario):
    lista = []
    for i in data_inventario["activos"]:
        codigo = i
        numero_serial = data_inventario["activos"][i]["numero_serial"]
        nombre = data_inventario["activos"][i]["nombre"]
        marca = data_inventario["activos"][i]["marca"]
        estado = data_inventario["activos"][i]["estado"]
        subLista = [codigo,nombre, numero_serial, marca,estado]
        lista.append(subLista)
    linesPorPage = 20
    for idx,i in enumerate(range(0,len("activos"),linesPorPage)):
        subset_data="activos"[ i: i + linesPorPage]
        totalPag = len("activos")//linesPorPage
        clear_screen()
        print(tabulate(subset_data,headers="keys",tablefmt = "fancy_grid",floatfmt = (".OF")))
        print(f'Pagina {idx + 1} de {totalPag + 1}')
        pause_screen()    
    print(tabulate(lista, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL","MARCA","ESTADO"], tablefmt="fancy_grid"))
    


#cod serial nombre ,arca estado 
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
