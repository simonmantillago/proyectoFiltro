from csv import reader
import modules.coreFiles as f

def convertExel(data_inventario):
    datos_excel=[]
    with open("excelData/DatosVisual.csv","r") as file:
        lector=reader(file)
        for row in lector:
            datos_excel.append(row[0].split(';'))
        
    for idx,item in enumerate(datos_excel):
        producto={
        
        'codigo_transaccion':item[0],
        'numero_formulario':item[1],
        'codigo':item[2],
        'numero_serial':item[3],
        'marca':item[4],
        'categoria':item[5],
        'tipo':item[6],
        'nombre':item[7],
        'proveedor':item[8],
        'empresa_responsable':item[9],
        'precio':item[10],
        'estado':'No asignado',
        'historial':{},
        'Asignado_A':'N/A'
        }

        data_inventario.get('activos').update({item[2]:producto})
        f.addData('inventario.json',data_inventario)

    