import time
import parametros as pa
import os
import core as cr
def updateInfo(bodega:dict,value:dict):
    os.system('clear')
    bodega.update(value) 
    print("Estamos procesando su información .....")
    time.sleep(pa.TIME_STOP)

def buscarItem(bodega:dict): 
    os.system('clear')
    codigo = input("Ingrese el codigo del producto : ")
    dataItem = bodega.get(codigo, -1)
    if dataItem == -1:
        print("El producto no existe")
    else:
        comprarProducto(dataItem,codigo,bodega)

def comprarProducto(dataItem:dict,llave:str,bodega:dict):
    if dataItem['estado']:
        cantidad = int(input("Ingrese la cantidad a comprar"))
        
        dataItem['valorc'] = float(input("Ingrese el valor de compra :"))
        dataItem['valorv'] = dataItem['valorc'] * pa.PROCENTAJE_VENTA
        bodega.update({llave:dataItem}) 
    else:
        print("El producto ya no se encuentra disponible para la compra")
        time.sleep(pa.TIME_STOP)

def dardebaja(bodega:dict):
    os.system('clear')
    codigo =input("Ingrese el codigo del producto a dar de Baja")
    dataItem = bodega.get(codigo, -1)

    if dataItem == -1:
        print("El producto no existe")
    else:
        dataItem["estado"]=False
        bodega.update({codigo:dataItem})
        
def delItem(bodega:dict):
    cr.delInfo(pa.BD_PRODUCTOS,bodega)
    
