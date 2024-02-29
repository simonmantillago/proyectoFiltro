import modules.coreFiles as cf
from datetime import datetime

def addAsignation(inventario):
    activos=[]
    numero=str(len(inventario['asignaciones'])).zfill(4)
    fecha=str(datetime.now().date())
    isTipo=True
    while isTipo:
        cf.os.system('cls')
        op=cf.rs.checkInput('int','A quien va a realizar la asignacion:\n1. Persona\n2. Zona\n->')
        if op==1:
            tipo='Persona'
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le asignara el o los productos')
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('el id no corresponde a ninguna persona registrada')

        elif op==2:
            tipo='Zona'
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le asignara el o los productos')
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El id no corresponde a ninguna Zona registrada')
        
    isActivo=True
    while isActivo:
        codigo=cf.rs.checkInput('srt','ingrese el codigo del producto a asignar').upper()
        if (codigo in inventario['activos']) and (codigo not in activos):
                if (inventario['activos'][codigo]['estado']=='No asignado'):
                    activos.append(codigo)
                else:
                    cf.rs.showError(f'el producto ya se encuenntra asignado a {inventario["activos"][codigo]["Asignado_A"]}')
        else:
                cf.rs.showError('El id no corresponde a ningun activo registrado')
        isActivo=cf.rs.yesORnot('Desea agregar otro activo a la asignación')

    Asignation={

    'Numero':numero,
    'Fecha':fecha,
    'Tipo':tipo,
    'AsignadoA':id,
    'Activos':activos
    }

    print(Asignation)