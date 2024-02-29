import sys
import os
import json
from ui.menu import reports_menu
from tabulate import tabulate
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
#funciones de reportes 
def listarActivos(data_inventario):
    
    lista = []
    for i in data_inventario["activos"]:
        codigo = i
        numero_serial = data_inventario["activos"][i]["numero_serial"]
        nombre = data_inventario["activos"][i]["nombre"]
        subLista = [codigo, nombre, numero_serial]
        lista.append(subLista)
    linesPorPage = 30
    totalPag = (len(lista) - 1) // linesPorPage + 1
    for idx in range(totalPag):
        clear_screen()
        subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
        print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        print(f'Pagina {idx + 1} de {totalPag}')
        pause_screen()
        op = input('Si desea volver al menú, presione 0: ')
        if op == "0":
            clear_screen()  
            reports_menu()  


def listActivosCategoria(data_inventario, tipo):
    
    op = input("""
               1. Listar categoria Monitor 
               2. Listar categoria CPU
               3. Listar categoria Mouse
               4. Listar categoria Teclado
               
               """)
    if op == "0":
            clear_screen()  
            reports_menu() 
    elif op == "1":
        listaMonitor = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["tipo"] == "Monitor":
                nombre = activo["nombre"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, numero_serial]
                listaMonitor.append(subLista)
        if listaMonitor:
            print(tabulate(listaMonitor, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            pause_screen() 
            clear_screen() 
            reports_menu() 
        else:
            print(f"No hay activos en la categoría '{tipo}'.")
            
    elif op == "2":
        listaCPU = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["tipo"] == "CPU":
                nombre = activo["nombre"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, numero_serial]
                listaCPU.append(subLista)
        if listaCPU:
            print(tabulate(listaCPU, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            pause_screen() 
            clear_screen() 
            reports_menu() 
        else:
            print(f"No hay activos en la categoría '{tipo}'.")
    elif op == "3":
        listaMouse = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["tipo"] == "Mouse":
                nombre = activo["nombre"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, numero_serial]
                listaMouse.append(subLista)
        if listaMouse:
            print(tabulate(listaMouse, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            pause_screen() 
            clear_screen() 
            reports_menu() 
        else:
            print(f"No hay activos en la categoría '{tipo}'.")
    elif op == "4":
        listaTeclado = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["tipo"] == "Teclado":
                nombre = activo["nombre"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, numero_serial]
                listaTeclado.append(subLista)
        if listaTeclado:
            print(tabulate(listaTeclado, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            pause_screen() 
            clear_screen() 
            reports_menu() 
        else:
            print(f"No hay activos en la categoría '{tipo}'.")
        
                


# def listarActivosDaño(activos):
#     for codigo, detalles in activos.items():
#         if detalles["estado"] == "Dado de baja por daño":
#             print(f"Código: {codigo}")
#             for clave, valor in detalles.items():
#                 print(f"{clave.capitalize()}: {valor}")
#             print("-----------------------------")
