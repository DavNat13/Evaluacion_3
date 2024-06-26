lista_estudiante = []

def agregar_estudiante(coleccion):

    nombre = input("")
    edad = input("")
    curso = input("")
    promedio = input("")

    lista_estudiante.append([nombre, edad, curso, promedio])
    print("Los datos se han agregado correctamente")

def menu (): 
    print("1. Agregar un estudiante.\n2. Ver todos los estudiantes.\3. Modificar un estudiante.\n4. Eliminar un estudiante\n5. Guardar colección en un archivo\n6. Salir del programa.")

def eliminar_producto ():
    if agregar_estudiante in lista_estudiante:
        print("")


def guardar_Archivo():
    with open ("lista_archivo.txt",'w') as archivo:
        archivo.write (f"{lista_estudiante}")