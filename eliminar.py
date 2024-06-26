
listaEstudiante = []
alumno = input("Ingresa alumnos:")

def eliminar_producto( listaEstudiante):
    if alumno in listaEstudiante:
        listaEstudiante.remove(alumno)
        print(f"alumno '{alumno}' eliminado de la lista.")
    else:
        print(f"El alumno '{alumno}' no está en la lista de compras.")

# Ejemplo de uso:
listaEstudiante
alumno_a_eliminar.remove = input("Ingresa el alumno que quieres eliminar--->")

print("Lista de estudiantes antes de eliminar:", listaEstudiante)
sacarEstudiante(listaEstudiante, alumno_a_eliminar)
print("Lista de compras después de eliminar:", listaEstudiante)


