import modules.coreFiles as cf
import modules.reusable as rs
from tabulate import tabulate
import sys

inventario = None
inventario = cf.checkFile("inventario.json", inventario)

def main_menu():
    def wrapper(func):
        cf.clear_screen()
        func()
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
        pass
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
    def wrapper(func):
        cf.clear_screen()
        func()
        activos_menu()

    title = """
    +++++++++++++++
    +   ACTIVOS   +
    +++++++++++++++
    """
    print(title)
    menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        pass
    elif op == "2":
        pass
    elif op == "4":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        activos_menu()

def personal_menu():
    def wrapper(func):
        cf.clear_screen()
        func()
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
        personal_menu()

def asignaciones_menu():
    def wrapper(func):
        cf.clear_screen()
        func()
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
        pass
    elif op == "2":
        pass
    elif op == "3":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        asignaciones_menu()


def reports_menu(): 
    def wrapper(func):
        cf.clear_screen()
        func()
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
    def wrapper(func):
        cf.clear_screen()
        func()
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