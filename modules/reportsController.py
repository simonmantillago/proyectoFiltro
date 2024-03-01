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
    else:
            print(f"No hay activos aun.")
            cf.pause_screen()
            cf.clear_screen()

def listActivosCategoria(data_inventario):
    while True:
    
        opcion = (""" 
                1. Listar categoria equipos de computo 
                2. Listar categoria juegos
                3. Listar categoria electrodomesticos
                4. Volver al menu de reportes
                """)
        print(opcion)
        #EQUIPOS DE COMPUTO
        op = input(":> ")
        if op == "1":
            listaEquipos = []
            for codigo, activo in data_inventario["activos"].items():
                if activo["categoria"] == "Equipo de computo":
                    nombre = activo["nombre"]
                    categoria = activo["categoria"]
                    numero_serial = activo["numero_serial"]
                    subLista = [codigo, nombre, categoria, numero_serial]
                    listaEquipos.append(subLista)
            if listaEquipos:
                linesPorPage = 30
                totalPag = (len(listaEquipos) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    cf.clear_screen()
                    subset_data = listaEquipos[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    cf.pause_screen()
                    op = input('Si desea volver al menú, presione 0: ')
                    if op == "0":
                        cf.clear_screen()
                        break  
                    print(opcion)

            else:
                print(f"No hay activos en la categoría equipos de computo.")
                cf.pause_screen()
                cf.clear_screen()

            #JUEGOS  
        elif op == "2":
            listaJuegos = []
            for codigo, activo in data_inventario["activos"].items():

                if activo["categoria"] == "Juegos":
                    nombre = activo["nombre"]
                    categoria = activo["categoria"]
                    numero_serial = activo["numero_serial"]
                    subLista = [codigo, nombre,categoria, numero_serial]
                    listaJuegos.append(subLista)
            if listaJuegos:
                linesPorPage = 30
                totalPag = (len(listaJuegos) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    cf.clear_screen()
                    subset_data = listaJuegos[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    cf.pause_screen()
                    op = input('Si desea volver al menú, presione 0: ')
                    if op == "0":
                        cf.clear_screen()  
                        break  
                    print(opcion)
            else:
                print(f"No hay activos en la categoría juegos.")
                cf.pause_screen()
                cf.clear_screen()
    #ELECTRODOMESTICOS
        elif op == "3":
            listaElectrodomesticos = []
            for codigo, activo in data_inventario["activos"].items():

                if activo["categoria"] == "Electrodomesticos":
                    nombre = activo["nombre"]
                    categoria = activo["categoria"]
                    numero_serial = activo["numero_serial"]
                    subLista = [codigo, nombre,categoria, numero_serial]
                    listaElectrodomesticos.append(subLista)
            if listaElectrodomesticos:
                linesPorPage = 30
                totalPag = (len(listaElectrodomesticos) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    cf.clear_screen()
                    subset_data = listaElectrodomesticos[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    cf.pause_screen()
                    op = input('Si desea volver al menú, presione 0: ')
                    if op == "0":
                        cf.clear_screen()  
                        break  
                    print(opcion)
            else:
                print(f"No hay activos en la categoría elesctrodomesticos")
                cf.pause_screen()
                cf.clear_screen()
        elif op == "4":
                cf.clear_screen()  
                cf.reports_menu()
#LISTAR ACTIVOS DADOS DE BAJA POR DAÑO 
def listarActivosDaño(data_inventario):
    lista = []
    for codigo, activo in data_inventario["activos"].items():
        if activo["estado"] == "dado de baja por daño":
            nombre = activo["nombre"]
            estado = activo["estado"]
            numero_serial = activo["numero_serial"]
            subLista = [codigo, nombre, estado, numero_serial]
            lista.append(subLista)
    
    if lista:  # Si la lista no está vacía, imprime los activos no asignados
        linesPorPage = 30
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
        linesPorPage = 30
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
            print(f"No hay activos aun.")
            cf.pause_screen()
            cf.clear_screen()
#LISTAR HISTORIAL DE MOV. DE ACTIVO
def listarHistorial(data_inventario):
    lista = []
    for codigo, activo in data_inventario["activos"].items():
        historial = activo.get("historial", {})  # Obtener el historial de movimientos del activo
        for nro_historial, movimiento in historial.items():
            fecha = movimiento.get("fecha")
            encargado = movimiento.get("encargado")
            tipo_mov = movimiento.get("tipo_mov")
            lista.append([nro_historial, fecha, encargado, tipo_mov])

    if lista:
        linesPorPage = 30
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
        print(f"No hay historial de movimientos disponibles.")
        cf.pause_screen()
        cf.clear_screen()



