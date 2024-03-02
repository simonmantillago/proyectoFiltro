import modules.reusable as rs
import modules.coreFiles as cf 
from tabulate import tabulate

def addPersonal(inventario):
    addMore = True
    while addMore:
        id = rs.checkInput('str','Ingrese el id o nit de la persona o empresa').upper()
        personalData = inventario.get('personas',{})
        zonasData = inventario.get('zonas', {})
        if personalData:
            for value in personalData.values():
                if (value["id"] == id):
                    rs.showError("Ese id o nit ya se encuentra registrado")
                    addPersonal(inventario)
                    return
        
        if len(zonasData):
            for valor in zonasData.values():
                if (valor["nroZona"] == id):
                    rs.showError("Ese id ya se encuentra registrado en zonas")
                    addPersonal(inventario)
                    return
                
        nombre = rs.checkInput('str','Ingrese el nombre de la persona')
        email = rs.checkInput('str','Ingrese el email de la persona')
        movil = rs.checkInput('int',f'Ingrese el nro celular de {nombre}')
        casa = rs.yesORnot('Desea ingresar un numero fijo?')
        
        if casa == True:
            casa = rs.checkInput('int',f'Ingrese el nro fijo de {nombre}')
        else:
            casa = 'No tiene'   
                                
        personal = rs.yesORnot('Desea ingresar un numero personal?')
        if personal == True:
            personal = rs.checkInput('int',f'Ingrese el nro personal de {nombre}')
        else:
            personal = 'No tiene'    
        
        oficina = rs.yesORnot('Desea ingresar un numero de oficina?')
        if oficina == True:
            oficina = rs.checkInput('int',f'Ingrese el nro de oficina de {nombre}')
        else:
            oficina = 'No tiene'  
        
        nuevo_personal = {
            'id': id,
            'nombre':nombre,
            'email':email,
            'telefono':{
                'movil':movil,
                'casa':casa,
                'personal':personal,
                'oficina':oficina   
            },
            'activos_asignados':[]
        }      
        
        inventario.get('personas').update({id:nuevo_personal})
        cf.addData('inventario.json',inventario)
        addMore = rs.yesORnot('Desea ingresar otra persona?')
        cf.clear_screen()

def searchPersonal(data):
    if len(data['personas']):
        valor = input("Ingrese el id de la persona a buscar -> ").upper() ##puse el .upper()
        if valor in data['personas']:
            result= data['personas'].get(valor)
            id,nombre,email,telefonos,activos = result.values()
            movil,casa,personal,oficina = telefonos.values()
            displayList = [['Id',id],['Nombre',nombre],['Email',email],['Celular',movil],['Fijo',casa],['Nro Personal',personal],['Nro ofincina',oficina],['Activos asignados',activos]]
            print(tabulate(displayList,tablefmt="fancy_grid"))
            cf.pause_screen()
            cf.clear_screen()
        else:
            rs.showError(f'No hay activos registrados con el codigo {valor}') ## puse mensaje de error por si no lo encontraba
    else: 
        rs.showError('No hay personal registrado')
        cf.clear_screen()
        
        
def modifyPersonal(data, srcData):
    if len(data) <= 0:
        rs.showError('No se encontro informacion sobre ese activo')
        cf.clear_screen()
    else:
        for key in data.keys():
            if(key != 'id'):
                if key != 'activos_asignados':
                    if type(data[key]) == dict:
                        for key2 in data[key].keys():
                            if bool(rs.yesORnot(f'Desea modificar el {key2}')):
                                cf.clear_screen()
                                data[key][key2] = cf.checkFile('int',f'Ingrese el nuevo valor para {key2}: ') ## aqui le puse checkfiles por si lo quieren modificar que sea solo numero
                    else:
                        if bool(rs.yesORnot(f'Desea modificar el {key}')):
                            cf.clear_screen()
                            data[key] = input(f'Ingrese el nuevo valor para {key}: ')
            srcData['personas'][data['id']].update(data)
        cf.UpdateFile('inventario.json', srcData)
        rs.showSuccess('Informacion modificada correctamente')
        cf.clear_screen()