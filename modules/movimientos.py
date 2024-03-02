import modules.coreFiles as cf
import modules.asignation as a
from datetime import datetime
def mov(inventario,estado,tipo_mov,encargado):
    codigo=cf.rs.checkInput('str','Ingrese el codigo del activo').upper()
    if codigo in inventario['activos']:
        if tipo_mov=='Retorno':
            if inventario['activos'][codigo]['estado']=='Asignado':
                modificar_data(inventario,estado,tipo_mov,encargado,codigo)
            else:
                cf.rs.showError(f'El activo se encuentra en estado de {inventario["activos"][codigo]["estado"]}')
                return
        else:
            if inventario['activos'][codigo]['estado']=='Dado de baja':
                cf.rs.showError(f'El activo ya se encuentra Dado de Baja')
                return
            else:
                modificar_data(inventario,estado,tipo_mov,encargado,codigo)
    else:
        cf.rs.showError('El codigo no coincide con ningun activo registrado')
        return
    
    return codigo
def modificar_data(inventario,estado,tipo_mov,encargado,codigo):
    fecha=str(datetime.now().date())
    nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
    id=inventario['activos'][codigo]['Asignado_A']
    inventario['activos'][codigo]['Asignado_A']='N/A'
    inventario['activos'][codigo]['estado']=estado
    if id!='N/A':
        inventario['asignaciones'][id]['Activos'].remove(codigo)
        tipo=inventario['asignaciones'][id]['Tipo']
        if tipo=='zonas':
            inventario[tipo][id]['cantidad_activos']-=1
        inventario[tipo][id]['activos_asignados'].remove(codigo)
    historial={
    'nro_historial':nro_historial,
    'encargado':encargado,
    'fecha':fecha,
    'tipo_mov':tipo_mov}
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})

    cf.addData('inventario.json',inventario)
    if tipo_mov!='Retorno':
        cf.rs.showSuccess('El movimiento se realizó con exito')


def cam(inventario,encargado):
    codigo=mov(inventario,'No asignado','Retorno',encargado)
    if codigo==None:
        return
    addAsignation(inventario,'Re-asignacion',encargado,codigo)

def addAsignation(inventario,tipo,encargado,codigo):
#constantes
    activos=[]
    fecha=str(datetime.now().date())

    cf.clear_screen()

    isTipo=True
    while isTipo:
        cf.clear_screen()
        op=cf.rs.checkInput('int','A quien va a realizar la asignacion:\n1. Persona\n2. Zona\n->') 
        cf.clear_screen()
        if op==1:
            tipo='personas'## evalua en personas si existe o no
            id_persona=cf.rs.checkInput('str','Ingrese el ID de la Persona a la cual se le asignara el o los activos').upper()
            cf.clear_screen()
            if id_persona in inventario['personas']:
                id=id_persona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna persona registrada')
                isworking=(cf.rs.yesORnot('¿Desea intentarlo nuevamente?'))
                if isworking==False:
                    cf.rs.showError(f'El activo {codigo} quedó en estado No asignado')
                    cf.rs.showError(f'Si desea reasignarlo debe realizarlo desde el apartado de asignaciones')
                    return

        elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le asignara el o los activos').upper()
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')
                isworking=(cf.rs.yesORnot('¿Desea intentarlo nuevamente?'))
                if isworking==False:
                    cf.rs.showError(f'El activo {codigo} quedó en estado No asignado')
                    cf.rs.showError(f'Si desea reasignarlo debe realizarlo desde el apartado de asignaciones')
                    return

    cf.clear_screen() 
    if tipo=='zonas':  ## evalua en la zona si tiene capacidad para realizar la asignacion
        if inventario[tipo][id]['cantidad_activos']<inventario[tipo][id]['total_capacidad']:
            inventario[tipo][id]['cantidad_activos']+=1
            add_codigo(activos,inventario,codigo,tipo,fecha,id,encargado) ## asigna, cambia estados e ingresa info al json
            
        else:
            cf.rs.showError(f'Esta zona ya cuenta con la maxima capacidad de activos \n Por tal motivo no se le pueden asignar mas activos, sin embargo el activo {codigo} quedó en estado No asignado')
            cf.rs.showError(f'Si desea reasignarlo debe realizarlo desde el apartado de asignaciones')
            return
    else:
        add_codigo(activos,inventario,codigo,tipo,fecha,id,encargado)# asigna, cambia estados e ingresa info al json
                
        
    if tipo=='zonas':
        numero=id
    if tipo =='personas':
        numero=id
    Asignation={

    'Numero':numero,
    'Fecha':fecha,
    'Tipo':tipo,
    'AsignadoA':id,
    'Activos':activos
    }
    if numero not in inventario['asignaciones']:
        inventario['asignaciones'].update({numero:Asignation})
    else:
        for item in activos:
            inventario['asignaciones'][numero]['Activos'].append(item)

    cf.rs.showSuccess(f'movimiento realizado con exito')
    cf.clear_screen()
    cf.addData('inventario.json',inventario)

def add_codigo(activos,inventario,codigo,tipo,fecha,id,encargado):

    activos.append(codigo)
    inventario['activos'][codigo]['Asignado_A']=id
    inventario['activos'][codigo]['estado']='Asignado'
    inventario[tipo][id]['activos_asignados'].append(codigo)
    nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
    historial={
        'nro_historial':nro_historial,
        'encargado':encargado,
        'fecha':fecha,
        'tipo_mov':tipo
    }
    inventario['activos'][codigo]['historial'].update({nro_historial:historial})

