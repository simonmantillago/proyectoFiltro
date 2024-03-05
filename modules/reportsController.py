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
    if lista:
        linesPorPage = 15
        totalPag = (len(lista) - 1) // linesPorPage + 1
        for idx in range(totalPag):
            cf.clear_screen()
            subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
            print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            cf.pause_screen()
            cf.clear_screen()
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                cf.clear_screen()  
                cf.reports_menu()
    else:
            print(f"No hay activos aun.")
            cf.pause_screen()
            cf.clear_screen()

def listActivosCategoria(data_inventario):
        cf.clear_screen()
        categoria_buscar = cf.rs.checkInput('str','Ingrese la categoria a buscar').upper()
        
        listaEquipos = []
        for codigo, activo in data_inventario["activos"].items():
            if activo["categoria"].upper()== categoria_buscar:
                nombre = activo["nombre"]
                categoria = activo["categoria"]
                numero_serial = activo["numero_serial"]
                subLista = [codigo, nombre, categoria, numero_serial]
                listaEquipos.append(subLista)
            else: 
                cf.rs.showError(f'No hay ningun activo registrado en la categoria {categoria_buscar}')
                iscategoria=(cf.rs.yesORnot('Desea intentarlo nuevamente'))
                if iscategoria==False:
                    cf.clear_screen()
                    cf.reports_menu()
                    return
                else:
                    listActivosCategoria(data_inventario)

        if listaEquipos:
            linesPorPage = 15
            totalPag = (len(listaEquipos) - 1) // linesPorPage + 1
            for idx in range(totalPag):
                cf.clear_screen()
                subset_data = listaEquipos[idx * linesPorPage: (idx + 1) * linesPorPage]
                print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                print(f'Pagina {idx + 1} de {totalPag}')
                cf.pause_screen()
                op = input('Si desea volver al menú, presione 0: ')
                cf.clear_screen()
                if op == "0":
                    cf.clear_screen()
                    break  
        

            else:
                print(f"No hay activos en la categoría {categoria_buscar}.")
                cf.pause_screen()
                cf.clear_screen()

    
#LISTAR ACTIVOS DADOS DE BAJA POR DAÑO 
def listarActivosDaño(data_inventario):
    lista = []
    for codigo, activo in data_inventario["activos"].items():
        if activo["estado"] == "Dado de baja":
            nombre = activo["nombre"]
            estado = activo["estado"]
            numero_serial = activo["numero_serial"]
            subLista = [codigo, nombre, estado, numero_serial]
            lista.append(subLista)
    
    if lista:  # Si la lista no está vacía, imprime los activos no asignados
        linesPorPage = 15
        totalPag = (len(lista) - 1) // linesPorPage + 1
        for idx in range(totalPag):
            cf.clear_screen()
            subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
            print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "ESTADO", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            cf.pause_screen()
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                cf.clear_screen()
                cf.reports_menu()

    else:
        print("No hay activos con estado 'No asignado'")
        cf.pause_screen()
        cf.clear_screen()
#LISTAR ACTIVOS Y ASIGNACION 
def listarActivosAsignacion (data_inventario):
    
    lista = []
    for i in data_inventario["activos"]:
    
        codigo = i
        numero_serial = data_inventario["activos"][i]["numero_serial"]
        nombre = data_inventario["activos"][i]["nombre"]
        asignacion = data_inventario["activos"][i]["Asignado_A"]
        subLista = [codigo, nombre,asignacion, numero_serial]
        lista.append(subLista)
    if lista:
        linesPorPage = 15
        totalPag = (len(lista) - 1) // linesPorPage + 1
        for idx in range(totalPag):
            cf.clear_screen()
            subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
            print(tabulate(subset_data, headers=["CODIGO", "NOMBRE",  "ASIGNADO A","NUMERO SERIAL"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            cf.pause_screen()
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                cf.clear_screen()  
                cf.reports_menu()
            else: 
                cf.clear_screen()
    else:
        print(f"No hay activos aun.")
        cf.pause_screen()
        cf.clear_screen()
#LISTAR HISTORIAL DE MOV. DE ACTIVO
def listarHistorial(data_inventario):
    activosrc = cf.rs.checkInput('str','Ingrese el activo del que desea ver el historial')
    lista = []
    for codigo, activo in data_inventario["activos"].items():
        if codigo == activosrc.upper():    
            historial = activo.get("historial", {})  # Obtener el historial de movimientos del activo
            for nro_historial, movimiento in historial.items():
                fecha = movimiento.get("fecha")
                encargado = movimiento.get("encargado")
                tipo_mov = movimiento.get("tipo_mov")
                lista.append([nro_historial, fecha, encargado, tipo_mov])

    if lista:
        linesPorPage = 15
        totalPag = (len(lista) - 1) // linesPorPage + 1
        for idx in range(totalPag):
            cf.clear_screen()
            subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
            print(tabulate(subset_data, headers=["Nro. HISTORIAL", "FECHA", "ENCARGADO", "TIPO DE MOVIMIENTO"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            cf.pause_screen()
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                cf.clear_screen()  
                cf.reports_menu()
            else:
                cf.clear_screen()
    else:
        print(f"No hay historial de movimientos disponibles.")
        cf.pause_screen()
        cf.clear_screen()