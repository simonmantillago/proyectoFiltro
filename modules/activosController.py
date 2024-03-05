import modules.coreFiles as cf 
from tabulate import tabulate
#modulo dedicado al crud de activos

def addActivo(inventario):
    codigo_transaccion = cf.rs.checkInput('str','Ingrese el codigo de la transaccion')
    numero_formulario = cf.rs.checkInput('str','Ingrese el numero de formulario') ## puse para que fuera un int por que estaba como str
    
    
    activosData = inventario.get('activos')
    if activosData: # verificacion de que no se repitan
        for value in activosData.values():
            if (value["codigo_transaccion"] == codigo_transaccion or
                value["numero_formulario"] == numero_formulario):
                cf.rs.showError("Error: El codigo de transaccion o el numero de formulario ya existen en el inventario.")
                addActivo(inventario)
                return
    addMore = True
    while addMore:
        codigo = cf.rs.checkInput('str','Ingrese el codigo del equipo').upper()
        
        # Verificar si el codigo ya existe en el inventario
        if codigo in activosData:
            cf.rs.showError("Error: El codigo del equipo ya existe en el inventario.")
            cf.clear_screen()
            iscodigo=not(cf.rs.yesORnot('Desea intentarlo nuevamente'))
            if iscodigo==True:
                cf.clear_screen()
                return
            
        
        
        numero_serial = cf.rs.checkInput('str','Ingrese el numero serial').upper()
        if any(value["numero_serial"] == numero_serial for value in activosData.values()):
            cf.rs.showError("Error: El numero serial ya existe en el inventario.")
            cf.clear_screen()
            continue
        
        
        marca = cf.rs.checkInput('str','Ingrese la marca').capitalize()
        categoria = cf.rs.checkInput('str','Ingrese la categoria').capitalize()
        tipo = cf.rs.checkInput('str','Ingrese el tipo del equipo').capitalize()
        nombre = cf.rs.checkInput('str','Ingrese el nombre del equipo')
        proveedor = cf.rs.checkInput('str','Ingrese el nombre del proveedor')
        empresa_responsable = cf.rs.checkInput('str','Ingrese el nombre de la empresa responsable')
        precio = cf.rs.checkInput('float','Ingrese el precio del equipo') ## arregle este para que sea un float
        estado = "No asignado"
        historial = {}
        Asignado_A = "N/A"
        
        
        nuevo_activo = {
            "codigo_transaccion": codigo_transaccion,
            "numero_formulario": numero_formulario,
            "codigo": codigo,
            "numero_serial": numero_serial,
            "marca": marca,
            "categoria": categoria,
            "tipo": tipo,
            "nombre": nombre,
            "proveedor": proveedor,
            "empresa_responsable": empresa_responsable,
            "precio": precio,
            "estado": estado,
            "historial": historial,
            "Asignado_A": Asignado_A
        }
        inventario.get('activos').update({codigo:nuevo_activo})
        cf.addData('inventario.json',inventario)
        cf.rs.showSuccess('Activo registrado de manera correcta')
        addMore = cf.rs.yesORnot('Desea ingresar otro activo dentro de la misma transaccion?')
        cf.clear_screen()
        
def searchActivo(data):
    if len(data['activos']):
        valor = input("Ingrese el codigo del activo a buscar -> ").upper()
        if valor in data['activos']: ### le puse esto por que si no, al darle un codigo que no sirviera se dañaba
            result= data['activos'].get(valor)
            transaccion,formulario,codigo,serial,marca,categoria,tipo,nombre,proveedor,responsable,precio,estado,historial,asignado = result.values()
            displayList = [['Codigo transaccion',transaccion],['Nro formulario',formulario],['Codigo',codigo],['Serial',serial],['Marca',marca],['Categoria',categoria],['Tipo',tipo],['Nombre',nombre],['Proveedor',proveedor],['Responsable',responsable],['Precio',precio],['Estado',estado],['Asigado A',asignado]]
            print(tabulate(displayList,tablefmt="fancy_grid"))
            cf.pause_screen()
            cf.clear_screen()
        else:
            cf.rs.showError(f'No hay activos registrados con el codigo {valor}') ## puse mensaje de error por si no lo encontraba
    else: 
        cf.rs.showError('No hay activos registrados')
        cf.clear_screen()

def modifyActivo(data, srcData):
    if len(data) <= 0:
        cf.rs.showError('No se encontro informacion sobre ese activo')
        cf.clear_screen()
    else:
        for key in data.keys(): #recorrer el diccionario y no permitir que se modifiquen algunos datos
            if(key != 'codigo'):
                if(key != 'Asignado_A'): ##AQUI LE PUSE EL CONDICIONAL PARA QUE ESTO NO SE PUEDA MODIFICAR, POR QUE SI NO VALEMOS MONDA
                    if(key != 'estado'): ##AQUI LE PUSE EL CONDICIONAL PARA QUE ESTO NO SE PUEDA MODIFICAR, POR QUE SI NO VALEMOS MONDA
                        if (key!='historial'):## creo que es mejor que esto no se modifique   
                            if bool(cf.rs.yesORnot(f'Desea modificar el {key}')):
                                if (key=='precio'): ## puse esto por si modifican el precio solo puedan meter un float
                                    cf.clear_screen()
                                    data[key] = cf.rs.checkInput('float','Ingrese el nuevo precio del activo')
                                elif key == 'numero_formulario':
                                    cf.clear_screen()
                                    data[key] = cf.rs.checkInput('int','Ingrese el nuevo numero de formulario')
                                else:
                                    cf.clear_screen()
                                    data[key] = input(f'Ingrese el nuevo valor para {key}: ')
                                    
            srcData['activos'][data['codigo']].update(data)
        cf.UpdateFile('inventario.json', srcData)
        cf.rs.showSuccess('Informacion modificada correctamente')
        cf.clear_screen()