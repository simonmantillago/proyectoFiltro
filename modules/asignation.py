import modules.coreFiles as cf
from datetime import datetime
from tabulate import tabulate

#######################################################################################################################################
#######################################################################################################################################
# ADD

def addAsignation(inventario,tipo):
    #constantes
    activos=[]
    fecha=str(datetime.now().date())
    encargado=cf.rs.checkInput('str','Ingrese el nombre del encargado de las asignaciones')
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

        elif op==2:
            tipo='zonas' ## evalua en zonas si existe o no
            id_zona=cf.rs.checkInput('str','Ingrese el ID de la Zona a la cual se le asignara el o los activos').upper()
            cf.clear_screen()
            if id_zona  in inventario['zonas']:
                id=id_zona
                isTipo=False
            else:
                cf.rs.showError('El ID no corresponde a ninguna Zona registrada')

    isActivo=True
    while isActivo:
        codigo=cf.rs.checkInput('srt','ingrese el codigo del producto a asignar').upper()
        cf.clear_screen()
        if (codigo in inventario['activos']) and (codigo not in activos): ## evalua si el codigo es valido
                if (inventario['activos'][codigo]['estado']=='No asignado'): ## evalua que el activo no este asignado 
                    if tipo=='zonas':  ## evalua en la zona si tiene capacidad para realizar la asignacion
                        if inventario[tipo][id]['cantidad_activos']<inventario[tipo][id]['total_capacidad']:
                            inventario[tipo][id]['cantidad_activos']+=1
                            add_codigo(activos,inventario,codigo,tipo,fecha,id,encargado) ## asigna, cambia estados e ingresa info al json
                            
                        else:
                            cf.rs.showError('esta zona ya cuenta con la maxima capacidad de activos')
                            break
                    else:
                        add_codigo(activos,inventario,codigo,tipo,fecha,id,encargado)# asigna, cambia estados e ingresa info al json
                else:
                    cf.rs.showError(f'el producto se encuentra {inventario["activos"][codigo]["estado"]}')
        else:
                cf.rs.showError('El id no corresponde a ningun activo registrado')
        isActivo=cf.rs.yesORnot('Desea agregar otro activo a la asignación')
        if activos==[]: ## si se quieren salir de la asignación 
            isActivo=not(cf.rs.yesORnot('Desea salir de asignaciones'))
            cf.clear_screen()
        else:
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

            cf.rs.showSuccess(f'El activo {codigo} ya fue asignado')
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


#######################################################################################################################################
#######################################################################################################################################
# SEARCH
    
def search_Asignation(inventario):
    nro_asignation=cf.rs.checkInput('str','Ingrese el numero de la asignacion a buscar').upper()
    if nro_asignation in inventario['asignaciones']:
        numero,fecha,tipo,AsignadoA,activos=inventario['asignaciones'][nro_asignation].values()
        Asignacion=[['Nro Asignacion',numero],['Fecha de Asignacion',fecha],['Tipo de Asignacion',tipo],['Asignado A',AsignadoA],['Activos Asignados',activos]]
        print(tabulate(Asignacion,tablefmt='fancy_grid'))
        cf.pause_screen()
    else:
        cf.rs.showError('El numero suministrado no corresponde a ninguna asignación')
    cf.clear_screen()
    