import modules.coreFiles as cf
import modules.reusable as rs
import modules.fileTranfer as ft
import modules.asignation as a
import modules.activosController as ac
import modules.personalController as pc
import modules.zonasController as zc

from tabulate import tabulate
import sys
data_inventario = {}
def main_menu():
    inventario = cf.readDataFile("inventario.json")
    global data_inventario 
    data_inventario = inventario
    ft.convertExel(data_inventario) #Funcion para subir datos de excel a json
    
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        main_menu()
    
    cf.clear_screen()
    title = """
    +++++++++++++++++++++++++++++
    + SISTEMA G&C DE INVENTARIO +
    +        CAMPUSLANDS        +
    +++++++++++++++++++++++++++++
    """
    print(title)
    menu =[["1.", "Activos"], ["2.", "Personal"], ["3.", "Zonas"], ["4.", "Asignacion de activos"], ["5.", "Reportes"],["6.", "Movimientos de activos"],["7.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(activos_menu)
    elif op == "2":
        wrapper(personal_menu)
    elif op == "3":
        wrapper(zonas_menu)
    elif op == "4":
        wrapper(asignaciones_menu)
    elif op == "5":
        wrapper(reports_menu)
    elif op == "6":
        wrapper(movimientos_menu)
    elif op == "7":
        sys.exit(("\033[92m{}\033[00m" .format('Vuelva pronto!')))
    else:
        main_menu()

def activos_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        activos_menu()

    title = """
    +++++++++++++++
    +   ACTIVOS   +
    +++++++++++++++
    """
    print(title)
    menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(ac.addActivo,data_inventario)
    elif op == "2":
        cf.clear_screen()
        mod = input('Ingrese el codigo del activo a modificar -> ')
        wrapper(ac.modifyActivo,data_inventario.get('activos').get(mod,{}),data_inventario)
    elif op == "3":
        wrapper(cf.delData,'activos',data_inventario)
    elif op == "4":
        wrapper(ac.searchActivo,data_inventario)
    elif op == "5":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        activos_menu()

def personal_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        personal_menu()
        
    title = """
    +++++++++++++++
    +   PERSONAL  +
    +++++++++++++++
    """
    print(title)
    menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(pc.addPersonal,data_inventario)
    elif op == "2":
        cf.clear_screen()
        mod = input('Ingrese la identificacion de la persona a modificar -> ')
        wrapper(pc.modifyPersonal,data_inventario.get('personas').get(mod,{}),data_inventario)
    elif op == "3":
        wrapper(cf.delData,'personas',data_inventario)
    elif op == "4":
        wrapper(pc.searchPersonal,data_inventario)
    elif op == "5":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        personal_menu()

def zonas_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        zonas_menu()

    title = """
    +++++++++++++
    +   Zonas   +
    +++++++++++++
    """
    print(title)
    menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(zc.addZona,data_inventario)
    elif op == "2":
        mod = input('Ingrese el codigo de la zona a modificar -> ')
        wrapper(zc.modifyZona,data_inventario.get('zonas').get(mod,{}),data_inventario)
    elif op == "3":
        wrapper(cf.delData,'zonas',data_inventario)
    elif op == "4":
        wrapper(zc.searchZona,data_inventario)
    elif op == "5":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        zonas_menu()

def asignaciones_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        asignaciones_menu()

    title = """
    ++++++++++++++++++
    +  ASIGNACIONES  +
    ++++++++++++++++++
    """
    print(title)
    menu = [["1.", "Crear"],["2.", "Buscar"],["3.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(a.addAsignation,data_inventario)
    elif op == "2":
        wrapper(a.search_Asignation)
    elif op == "3":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        asignaciones_menu()


def reports_menu(): 
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        reports_menu()

    title = """
    ++++++++++++++
    +  REPORTES  +
    ++++++++++++++
    """
    print(title)
    menu = [["1.", "Listar todos los activos"],["2.", "Listar activos por categoria"],["3.", "Listar activos dados de baja"],["4.", "Listar activos y asignacion"],["5.", "Listar historial de movimiento de activo"],["6.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    elif op == "6":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        reports_menu()

def movimientos_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        movimientos_menu()

    title = """
    +++++++++++++++++
    +  MOVIMIENTOS  +
    +++++++++++++++++
    """
    print(title)
    menu = [["1.", "Retorno activos"],["2.", "Dar de baja activo"],["3.", "Cambiar asignacion del activo"],["4.", "Enviar a garantia activo"],["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        pass
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        movimientos_menu()