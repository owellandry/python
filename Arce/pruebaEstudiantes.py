candidatos = []
opcion = True
while opcion==True:
    print("1. Digite para registrar \n2.Buscar candidato\n3.Eliminar candidato\n4.salir:) ")
    op = int(input("\nIngrese la opcion deseada:) "))
    if op == 1:
        nombre=input("Ingrese el nombre del candidato:) ")
        edad=int(input("Ingrese la edad del candidato:) "))
        fecha=input("Ingrese la fecha de nacimiento del candidato:) ")
        
        candidato = [nombre,edad,fecha]
        candidatos.append(candidato)
        print(f"El candidato {nombre} ha sido registrado exitosamente")
    elif op == 2:
        nombre = input("Digite el nombre del candidato a buscar:) ")
        for candidato in candidatos:
            if nombre in candidato:
                print(f"El candidato esta {nombre} registrado")
                print(candidato)
            else:
                print("El candidato no esta registrado")
    elif op == 3:
        nombre = input("Digite el nombre del candidato a eliminar:) ")
        for candidato in candidatos:
            if nombre in candidato:
                candidatos.remove(candidato)
                print(f"El candidato {nombre} está eliminado")
                print(candidatos)
                
            else:
                print("El candidato no esta registrado")   
       
    elif op == 4:
        opcion= False
        print(":) :) :) Gracias por utilizar el programa :) :) :)")

    else:
        print("Marca una accion valida para el menu:) ")