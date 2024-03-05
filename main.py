import modules.coreFiles as cf
from ui.menu import main_menu

inventario ={
    'activos':{},
    'personas':{},
    'zonas':{},
    'asignaciones' :{}
}

def main():  
    cf.checkFile('inventario.json',inventario)
    main_menu()

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            cf.rs.showError('Buen intento Jholver')
            cf.clear_screen()
        else:
            main()
            break


    