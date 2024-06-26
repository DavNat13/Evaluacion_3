lista_estudiante = []

def agregar_estudiante():
    
    nombre = input("")
    edad = input("")
    curso = input("")
    promedio = input("")

    lista_estudiante.append([nombre, edad, curso, promedio])
    print("Los datos se han agregado correctamente")