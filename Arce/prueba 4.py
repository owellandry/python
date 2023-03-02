inscritos = int(input("Digite el numero de personas inscritas:) "))
for i in range(0,inscritos,1):
    puntaje = int(input(f"Digite el puntaje del participante. Nro:{i+1}"))
    if puntaje >10 and puntaje<60:
        print("Estan en el nivel basico")
    elif puntaje >60 and puntaje <80:
        print("Estan en el nivel intermedio :) 
              ")
    elif puntaje >80 and puntaje<100:
        print("Estan en el nivel avanzado  :)") 