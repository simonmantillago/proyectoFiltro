import modules.coreFiles as cf
from ui.menu import main_menu
inventario ={
    'activos':{},
    'personas':{},
    'zonas':{}
}


def main():
    
    cf.checkFile('inventario.json',inventario)
    main_menu()

if __name__ == '__main__':
    main()