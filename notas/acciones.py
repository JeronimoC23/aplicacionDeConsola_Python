import notas.nota as modelo

class Acciones:

    def crear (self, usuario):
        print("Ok "+ str(usuario[1]+ " vamos a crear una nueva nota"))
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("Has guardado la nota " )

        else:
            print("No se a guardado la nota" + str(usuario[1]))


    def mostrar (self, usuario):
        print("\n Las notas son:")

        nota = modelo.Nota(usuario_id[0])
        notas = nota.listar()
        for nota in notas:
            print(nota[2])
            print(nota[3])

    def borrar (self, usuario):
        print("Vamos a borrar: ")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")

        else:
            print("No se pudo eliminar la nota")