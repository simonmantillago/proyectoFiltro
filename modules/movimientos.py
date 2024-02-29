# MENU MOVIMIENTO DE ACTIVOS
# 1. RETORNO DE ACTIVO
# 2. DAR DE BAJA ACTIVO
# 3. CAMBIAR ASIGNACION DE ACTIVO
# 4. ENVIAR A GARANTIA ACTIVO
# 5. REGRESAR AL MENU PRINCIPAL
import modules.coreFiles as cf
from datetime import datetime
def Return_Activo(inventario):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('int','Ingrese el nombre del encargado de hacer el retorno')
    cf.clear_screen()
    op=cf.rs.checkInput('int','Quien va a retornar el activo:\n1. Persona\n2. Zona\n->') 
    cf.clear_screen()
    if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona la cual retornara el activo')
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')

    elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona la cual se retornara el activo')
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
    codigo=cf.checkFile('str','Ingrese el código del activo')
    if codigo in inventario['activos']:
        inventario['activos'][codigo]['Asignado_A']=''
        inventario['activos'][codigo]['estado']='No asignado'
        inventario[tipo][id]['activos_asignados'].pop(codigo)
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        historial={
            'nro_historial':nro_historial,
            'encargado':encargado,
            'fecha':fecha,
            'tipo_mov':'Retorno'
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})
    cf.addData('inventario.json',inventario)

def Baja_Activo(inventario):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('int','Ingrese el nombre del encargado de dar de baja el activo')
    cf.clear_screen()
    op=cf.rs.checkInput('int','Quien va a dar de baja el activo:\n1. Persona\n2. Zona\n->') 
    cf.clear_screen()
    if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le dara de baja el activo')
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')

    elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le dara de baja el activo')
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
    codigo=cf.checkFile('str','Ingrese el código del activo')
    if codigo in inventario['activos']:
        inventario['activos'][codigo]['Asignado_A']=''
        inventario['activos'][codigo]['estado']='Dado de baja'
        inventario[tipo][id]['activos_asignados'].pop(codigo)
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        historial={
            'nro_historial':nro_historial,
            'encargado':encargado,
            'fecha':fecha,
            'tipo_mov':'Dado de baja'
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})
    cf.addData('inventario.json',inventario)

    
def cambiar_Asignación(inventario):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('int','Ingrese el nombre del encargado de cambiar la asignacion')
    cf.clear_screen()
    op=cf.rs.checkInput('int','Quien va a retornar el activo:\n1. Persona\n2. Zona\n->') 
    cf.clear_screen()
    if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le quitara el activo')
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')

    elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le quitara el activo')
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
    codigo=cf.checkFile('str','Ingrese el código del activo')
    if codigo in inventario['activos']:
        inventario['activos'][codigo]['Asignado_A']=''
        inventario['activos'][codigo]['estado']='No asignado'
        inventario[tipo][id]['activos_asignados'].pop(codigo)
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        historial={
            'nro_historial':nro_historial,
            'encargado':encargado,
            'fecha':fecha,
            'tipo_mov':'Retorno'
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})
    cf.addData('inventario.json',inventario)

    op=cf.rs.checkInput('int','a quien va a reasignar el activo:\n1. Persona\n2. Zona\n->') 
    cf.clear_screen()
    if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le asignara el o los activos')
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')

    elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le asignara el o los activos')
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
    codigo=cf.checkFile('str','Ingrese el código del activo')
    if codigo in inventario['activos']:
        inventario['activos'][codigo]['Asignado_A']=id
        inventario['activos'][codigo]['estado']='Asignado'
        inventario[tipo][id]['activos_asignados'].append(codigo)
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        historial={
            'nro_historial':nro_historial,
            'encargado':encargado,
            'fecha':fecha,
            'tipo_mov':'Asignacion'
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})
    cf.addData('inventario.json',inventario)


def garantia(inventario):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('int','Ingrese el nombre del encargado de mandar a garantia el activo')
    cf.clear_screen()
    op=cf.rs.checkInput('int','Quien va a retornar el activo:\n1. Persona\n2. Zona\n->') 
    cf.clear_screen()
    if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona que reporta la garantia del activo')
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')

    elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona que reporta la garantia del activo')
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
    codigo=cf.checkFile('str','Ingrese el código del activo')
    if codigo in inventario['activos']:
        inventario['activos'][codigo]['Asignado_A']=''
        inventario['activos'][codigo]['estado']='Garantia'
        inventario[tipo][id]['activos_asignados'].pop(codigo)
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        historial={
            'nro_historial':nro_historial,
            'encargado':encargado,
            'fecha':fecha,
            'tipo_mov':'Garantia'
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})
    cf.addData('inventario.json',inventario)
