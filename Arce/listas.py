agenda = []

#append agrega un elemento al final de la lista

agenda.append("carlos")
print(len(agenda))
print(agenda[0])
agenda.insert(0,"Maria")
print(agenda)
del agenda[0]
for i,item in enumerate (agenda):
    print(f'{item} esta en la pos {i}')
palabra = input("Ingrese el nombre a buscar: ")    
if palabra in agenda:
    print("Ok")
    

    