cantidadEstudiantes = 0
cantidadQuices = 0
cantidadParciales = 0

cantidadTrabajos = 0
notaQuiz=0.0
notaTrabajo = 0.0
notaParcial = 0.0
notaFinal = 0.0
notaAcumulativa = 0.0
cantidadEstudiantes = int(input("Ingrese Cantidad de estudiantes Matriculados"))
for i in range(0,cantidadEstudiantes,1):
    print(f'Ingrese la cantidad de Quices para el estudiante Nro.{i+1}')
    cantidadQuices = int(input(":)_"))
    for j in range(0,cantidadQuices,1):
        notaQuiz += float(input(f'Ingrese la nota Quiz Nro.{j}'))
    print(f'Ingrese la cantidad de Trabajos para el estudiante Nro.{j+1}')
    cantidadTrabajos = int(input(":)_"))
    for k in range(0,cantidadTrabajos,1):
        notaTrabajo += float(input(f'Ingrese la nota trabajo Nro{k}'))
    print(f'Ingrese la cantidad de Parciales para el estudiante Nro.{k+1}')
    cantidadParciales = int(input(":)_"))
    for l in range(0,cantidadParciales,1):
        notaParcial += float(input(f'Ingrese la nota parciales Nro.{l+1}'))
    notaFinal = ((notaQuiz/cantidadQuices)*0.40)+((notaParcial/cantidadParciales)*0.50)+((notaTrabajo/cantidadTrabajos)*0.10)
    print(f"La nota final es : {notaFinal}")
    if (notaFinal>=3.0):
        print("Aprobo")
    else:
        print("Estudiante mucho vago perdio")
    notaAcumulativa+=notaFinal
    notaQuiz = 0.0
    notaParcial = 0.0
    notaTrabajo = 0.0
    notaFinal = 0.0
print(f"La nota promedio del curso es : {notaAcumulativa/cantidadEstudiantes}")