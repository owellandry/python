import os
import time
import parametros as pa
import crud
import core as cr
bodega = {}
op = True

if (cr.checkFile(pa.BD_PRODUCTOS)):
    bodega =cr.LoadInfo(pa.BD_PRODUCTOS)
while op:
    try:
        os.system('clear')
        print("***************************")
        print("*  GESTOR DE INVENTARIOS  *")
        print("***************************")
        print(f'1. Registrar producto\n2.Comprar Producto\n3.Ajuste de Inventario\n4. Dar de baja al producto\n5.Borrar producto\n6.salir')
        rta = int(input(":)_"))
    except ValueError:
        op=True
        print(f'La opcion debe ser un entero')
        print(f'Espere un momento estamos procesando su error')
        time.sleep(pa.TIME_STOP)
    else:
        if rta == 1:
            os.system('clear')
            print("***************************")
            print("*  REGISTRO DE PRODUCTOS  *")
            print("***************************")
            nombre = input(f"Ingrese el nombre del producto :")
            codigo = input(f"Ingrese el Codigo del producto :")
            valorCompra = 0.0
            valorVenta = 0.0
            stockMin = int(input(f"Ingrese el StockMin del producto :"))
            stockMax = int(input(f"Ingrese el StockMax del producto :"))
            estado = True
            item = {
                    codigo:{
                        "nombreProducto" : nombre,
                        "valorc" : valorCompra,
                        "valorv" : valorVenta,
                        "stockmin" : stockMin,
                        "stockmax" : stockMax,
                        "compras":[],
                        "ventas":[]
                    }
            }
            crud.updateInfo(bodega,item)
            if cr.checkFile(pa.BD_PRODUCTOS):
                cr.crearInfo(pa.BD_PRODUCTOS,bodega,item)
            else:
                cr.crearInfo(pa.BD_PRODUCTOS,bodega)
        elif rta == 2:
            print(crud.buscarItem(bodega))
            print(crud.comprarProducto(bodega))
            time.sleep(pa.TIME_STOP)
        elif rta == 4:
            crud.dardebaja(bodega)
            
            time.sleep(pa.TIME_STOP)
        elif rta == 5:
            crud.delItem(bodega)
            time.sleep(pa.TIME_STOP)
        
        
        elif rta == 6:
            op=False