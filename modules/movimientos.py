import modules.coreFiles as cf
import modules.asignation as a
from datetime import datetime
def mov(inventario,estado,tipo_mov,encargado):
    codigo=cf.rs.checkInput('str','Ingrese el codigo del activo').upper()
    if codigo in inventario['activos']:
        fecha=str(datetime.now().date())
        nro_historial=str(len(inventario['activos'][codigo]['historial'])+1).zfill(3)
        id=inventario['activos'][codigo]['Asignado_A']
        inventario['activos'][codigo]['Asignado_A']=''
        inventario['activos'][codigo]['estado']=estado
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
        cf.rs.showSuccess('El movimiento se realizó con exito')

    else:
        cf.rs.showError('El codigo no existe')

def cam(inventario,encargado):
    mov(inventario,'No asignado','Retorno')
    a.addAsignation(inventario,'Re-asignacion',encargado)

