import modules.coreFiles as cf

inventario ={
    'activos':{},
    'personas':{},
    'zonas':{}
}


def main():
    cf.checkFile('inventario.json',inventario)

if __name__ == '__main__':
    main()