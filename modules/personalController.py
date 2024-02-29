import modules.reusable as rs
import modules.coreFiles as cf 
from tabulate import tabulate

def addPersonal(inventario):
    personalData = inventario.get('personal')
    if personalData:
        for value in personalData.values():
            if (value["id"] == id):
                rs.showError("Ese ID ya se encuentra registrado")
# def searchActivo(data):
#     valor = input("Ingrese el id de la persona a buscar -> ")
#     result= data['personal'].get(valor)
#     transaccion,formulario,codigo,serial,marca,categoria,tipo,nombre,proveedor,responsable,precio,estado,historial,asignado = result.values()
#     displayList = [['Codigo transaccion',transaccion],['Nro formulario',formulario],['Codigo',codigo],['Serial',serial],['Marca',marca],['Categoria',categoria],['Tipo',tipo],['Nombre',nombre],['Proveedor',proveedor],['Responsable',responsable],['Precio',precio],['Estado',estado],['Asigado A',asignado]]
#     print(tabulate(displayList,tablefmt="grid"))
#     cf.pause_screen()
#     cf.clear_screen()