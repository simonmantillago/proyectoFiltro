import modules.coreFiles as cf
from datetime import datetime

def addAsignation(inventario):
    numero=str(len(inventario['asiganciones'])).zfill(4)
    fecha=str(datetime.now().date())
    isTipo=True
    while isTipo:
        print('1. Persona/n2. Zona')
        op=cf.rs.checkInput('int','->')
        if op==1:
            tipo='Persona'
        elif op==2:
            tipo='Zona'




    Asignation={

    'Numero':numero,
    'Fecha':fecha,
    'Tipo':tipo,
    'AsignadoA':'',
    'Activos':[]
    }