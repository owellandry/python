import json

def crearInfo(*args):
    
    if(checkFile(args[0])==False):
        with open('data/'+args[0], "w") as write_file:
                json.dump(args[1], write_file,indent = 4)
                write_file.close()
    else:
        with open('data/'+args[0],'r+') as file:
             file.seek(0)
             args[1].update(args[2])
             json.dump(args[1], file, indent = 4)
             file.close()

def editarInfo(*args):
        with open('data/'+args[0], "w") as write_file:
                json.dump(args[1], write_file,indent = 4)
                write_file.close()

def delInfo(*args):
    
        
        validar = False
        while validar == False:
            codigo = input("Digite el codigo del producto que sea borrar:)_ ")
            validar = bool(args[1].get(codigo,''))
            
            if validar: 
                args[1].pop(codigo)
                with open('data/'+args[0],'w') as file:
                    json.dump(args[1], file, indent = 4)
                    file.close()
            else:
                print("No se puede eliminar el producto")
                validar =bool(input("Desea intentarlo con otro producto Enter(s) o N(salir)"))
       
def LoadInfo(fileName)->dict:
        with open('data/'+fileName, "r") as read_file:
            dicc = json.load(read_file)
        return dicc
        read_file.close()

def checkFile(filePath):
    try:
        with open('data/'+filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False