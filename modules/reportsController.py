import modules.coreFiles as cf
from tabulate import tabulate

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
        cf.clear_screen()
        subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
        print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        print(f'Pagina {idx + 1} de {totalPag}')
        cf.pause_screen()
        op = input('Si desea volver al menú, presione 0: ')
        if op == "0":
            cf.clear_screen()  
            cf.reports_menu()

def listActivosCategoria(data_inventario, tipo):
    
    op = input("""
               1. Listar categoria Monitor 
               2. Listar categoria CPU
               3. Listar categoria Mouse
               4. Listar categoria Teclado
               
               """)
    if op == "1":
        listaMonitor = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["tipo"] == "Monitor":
                nombre = activo["nombre"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, numero_serial]
                listaMonitor.append(subLista)
        if listaMonitor:
            print(tabulate(listaMonitor, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            cf.pause_screen() 
            cf.clear_screen() 
            cf.reports_menu() 
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
            cf.pause_screen() 
            cf.clear_screen() 
            cf.reports_menu() 
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
            cf.pause_screen() 
            cf.clear_screen() 
            cf.reports_menu() 
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
            cf.pause_screen() 
            cf.clear_screen() 
            cf.reports_menu() 
        else:
            print(f"No hay activos en la categoría '{tipo}'.")

# def listarActivosDaño(activos):
#     for codigo, detalles in activos.items():
#         if detalles["estado"] == "Dado de baja por daño":
#             print(f"Código: {codigo}")
#             for clave, valor in detalles.items():
#                 print(f"{clave.capitalize()}: {valor}")
#             print("-----------------------------")