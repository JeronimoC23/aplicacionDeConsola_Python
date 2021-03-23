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
        