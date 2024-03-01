import modules.reusable as rs
import modules.coreFiles as cf 
from tabulate import tabulate

def addZona(inventario):
    addMore = True
    while addMore:
        nroZona = rs.checkInput('str', 'Ingrese el número de la zona')
        zonaData = inventario.get('zonas', {})
        
        if zonaData:
            for value in zonaData.values():
                if value['nroZona'] == nroZona:
                    rs.showError("Esa zona ya se encuentra registrada")
                    cf.clear_screen()
                    addZona(inventario)
                    return
        
        nombreZona = rs.checkInput('str', 'Ingrese el nombre de la zona')
        
        if zonaData:
            for value in list(zonaData.values()):
                if value['nombreZona'] == nombreZona:
                    rs.showError("Error: El nombre de la zona ya se encuentra en uso")
                    cf.clear_screen()
                    addZona(inventario)
                    return
                
        total_capacidad = rs.checkInput('int', 'Ingrese la capacidad máxima de equipos de la zona')
        capacidad = 0
        
        nueva_zona = {
            'nroZona': nroZona,
            'nombreZona': nombreZona,
            'total_capacidad': total_capacidad,
            'capacidad': capacidad,
            'activos_asignados': []
        }
        
        zonaData[nroZona] = nueva_zona
        cf.addData('inventario.json', inventario)
        rs.showSuccess('Zona registrada correctamente')
        
        addMore = rs.yesORnot('¿Desea ingresar otra zona?')
        cf.clear_screen()
    
def searchZona(data):
    if len(data['zonas']):
        valor = input("Ingrese el codigo de la zona a buscar -> ")
        result= data['zonas'].get(valor)
        nroZona,nombreZona,totalCapacidad,capacidad,activos = result.values()
        displayList = [['Numero de zona',nroZona],['Nombre zona',nombreZona],['Capacidad total',totalCapacidad],['Capacidad',capacidad],['Activos zona',activos]]
        print(tabulate(displayList,tablefmt="fancy_grid"))
        cf.pause_screen()
        cf.clear_screen()
    else: 
        rs.showError('No hay zonas registradas')
        cf.clear_screen()
def modifyZona(data, srcData):
    if len(data) <= 0:
        rs.showError('No se encontro informacion sobre ese activo')
        cf.clear_screen()
    else:
        for key in data.keys():
            if(key != 'nroZona'):
                if key != 'activos_asignados':
                    if(key != 'capacidad'):
                        if bool(rs.yesORnot(f'Desea modificar el {key}')):
                            cf.clear_screen()
                            data[key] = input(f'Ingrese el nuevo valor para {key}: ')
            srcData['zonas'][data['nroZona']].update(data)
        cf.UpdateFile('inventario.json', srcData)
        rs.showSuccess('Informacion modificada correctamente')
        cf.clear_screen()