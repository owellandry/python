clientes ={}
clientes.update({"123":{"nombre":"juan","Email":"juan@gmail.com","Amante":"carlina patricia maria"}})
print(clientes)
clientes.update({
    "124":{
        "nombre":"carlos mario",
        "Email":"xxxx@gmail.com"
        ,"Amante":"teodora clementina"
        }
  
    })#modifica el valor del diccionario

print(clientes)

for key in clientes:
    print(key)#Imprime la llave
    print(clientes[key])#Imprime el cntenido de las llaves 
#for key,valor in clientes.items():
 #   print(f'{key} : {valor["nombre"]}')
for key,valor in clientes.items():
    for llave,value in valor.items():
        print(f'{llave.upper()} : {value}')


#busquedas en diccionarios
palabra = input("Ingrese el Id del cliente a buscar:) ")
resul = bool(clientes.get(palabra,""))
if(resul):
    print("Item encontrado")
    print(clientes.get(palabra,""))
else:
    print("item no encontrado")
    
#eliminar items de diccionarios
palabra = input("Ingrese el Ide del cliente a borrar")
result = bool(clientes.pop(palabra,""))
if(result):
    print("Item eliminado")
else:
    print("El resultado no se borro")
print(clientes)

    
