# MENU MOVIMIENTO DE ACTIVOS
# 1. RETORNO DE ACTIVO
# 2. DAR DE BAJA ACTIVO
# 3. CAMBIAR ASIGNACION DE ACTIVO
# 4. ENVIAR A GARANTIA ACTIVO
# 5. REGRESAR AL MENU PRINCIPAL
import modules.coreFiles as cf
from datetime import datetime

##################################################################################################################
def movimiento(inventario,msg,estado,tipo_mov):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('str','Ingrese el nombre del encargado del movimiento')
    ismovimiento=True
    while ismovimiento:
        cf.clear_screen()
        op=cf.rs.checkInput('int',f'Quien va a {msg}:\n1. Persona\n2. Zona\n->') 
        cf.clear_screen()
        if op==1:
                tipo='personas'## evalua en personas si existe o no
                id_persona=cf.rs.checkInput('str',f'Ingrese el ID de la Persona que {msg}')
                cf.clear_screen()
                if id_persona in inventario['personas']:
                    id=id_persona
                    ismovimiento=False
                else:
                    cf.rs.showError('El ID no corresponde a ninguna persona registrada')
                    cf.clear_screen()

        elif op==2:
                tipo='zonas' ## evalua en zonas si existe o no
                id_zona=cf.rs.checkInput('str',f'Ingrese el ID de la Zona que {msg}')
                cf.clear_screen()
                if id_zona in inventario['zonas']:
                    id=id_zona
                    ismovimiento=False
                else:
                    cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
                    cf.clear_screen()
    isCodigo=True
    while isCodigo:
        codigo=cf.rs.checkInput('str','Ingrese el código del activo').upper()
        if codigo in inventario['activos']:
            if codigo in inventario[tipo][id]['activos_asignados']:
                inventario['activos'][codigo]['Asignado_A']=''
                inventario['activos'][codigo]['estado']=estado
                inventario[tipo][id]['activos_asignados'].remove(codigo)
                nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
                historial={
                    'nro_historial':nro_historial,
                    'encargado':encargado,
                    'fecha':fecha,
                    'tipo_mov':tipo_mov
            }
                inventario['activos'][codigo]['historial'].update({nro_historial:historial})
                cf.clear_screen()
                isCodigo=False
            else:
                cf.rs.showError(f'El codigo del activo no corresponde a ningun activo asignado a {id}')
                cf.clear_screen()
                isCodigo=cf.rs.yesORnot('¿Desea intentar con otro codigo?')
        else:
            cf.rs.showError('El codigo del activo no corresponde a ningun activo registrado')
            cf.clear_screen()
            isCodigo=cf.rs.yesORnot('¿Desea intentar con otro codigo?')
            cf.clear_screen()
        
    cf.addData('inventario.json',inventario)
    cf.rs.showSuccess('Movimiento realizado con exito')


##################################################################################################################

def cambiar_Asignación(inventario,msg):
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('str','Ingrese el nombre del encargado del movimiento')
    ismovimiento=True
    while ismovimiento:
        cf.clear_screen()
        op=cf.rs.checkInput('int',f'Quien va a {msg}:\n1. Persona\n2. Zona\n->') 
        cf.clear_screen()
        if op==1:
                tipo_a='personas'## evalua en personas si existe o no
                id_persona=cf.rs.checkInput('str',f'Ingrese el ID de la Persona la cual {msg}')
                cf.clear_screen()
                if id_persona in inventario['personas']:
                    id_a=id_persona
                    ismovimiento=False
                else:
                    cf.rs.showError('El ID no corresponde a ninguna persona registrada')
                    cf.clear_screen()

        elif op==2:
                tipo_a='zonas' ## evalua en zonas si existe o no
                id_zona=cf.rs.checkInput('str',f'Ingrese el ID de la Zona la cual {msg}')
                cf.clear_screen()
                if id_zona in inventario['zonas']:
                    id_a=id_zona
                    ismovimiento=False
                else:
                    cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
                    cf.clear_screen()


    ischange=True
    while ischange:
        op=cf.rs.checkInput('int','a quien va a reasignar el activo:\n1. Persona\n2. Zona\n->') 
        cf.clear_screen()
        if op==1:
                tipo='personas'## evalua en personas si existe o no
                id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le asignara el o los activos')
                cf.clear_screen()
                if id_persona in inventario['personas']:
                    id=id_persona
                    ischange=False
                else:
                    cf.rs.showError('El ID no corresponde a ninguna persona registrada')
                    cf.clear_screen()

        elif op==2:
                tipo='zonas' ## evalua en zonas si existe o no
                id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le asignara el o los activos')
                cf.clear_screen()
                if id_zona  in inventario['zonas']:
                    id=id_zona
                    ischange=False
                else:
                    

                    cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
                    cf.clear_screen()

        isCodigo=True
        while isCodigo:
            codigo=cf.rs.checkInput('str','Ingrese el código del activo').upper()
            if codigo in inventario['activos']:
                if codigo in inventario[tipo_a][id_a]['activos_asignados']:
                    inventario[tipo_a][id_a]['activos_asignados'].remove(codigo)
                    inventario['activos'][codigo]['Asignado_A']=id
                    inventario['activos'][codigo]['estado']='Asignado'
                    inventario[tipo][id]['activos_asignados'].append(codigo)
                    nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
                    historial={
                        'nro_historial':nro_historial,
                        'encargado':encargado,
                        'fecha':fecha,
                        'tipo_mov':'Re Asignacion'}
                    inventario['activos'][codigo]['historial'].update({nro_historial:historial})


                    numero=str(len(inventario['asignaciones'])+1).zfill(4)
                    Asignation={
                        'Numero':numero,
                        'Fecha':fecha,
                        'Tipo':tipo,
                        'AsignadoA':id,
                        'Activo':[codigo]
                        }
                    inventario['asignaciones'].update({numero:Asignation})

                    isCodigo=False
                else:
                    cf.rs.showError(f'El codigo del activo no corresponde a ningun activo asignado a {id_a}')
                    cf.clear_screen()
                    isCodigo=cf.rs.yesORnot('¿Desea intentar con otro codigo?')
            else:
                cf.rs.showError('El codigo del activo no corresponde a ningun activo registrado')
                cf.clear_screen()
                isCodigo=cf.rs.yesORnot('¿Desea intentar con otro codigo?')
                cf.clear_screen()

    cf.addData('inventario.json',inventario)
    cf.rs.showSuccess(f'El activo {codigo} ya fue reasignado')

