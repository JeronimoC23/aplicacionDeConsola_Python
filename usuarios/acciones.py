import usuarios.usuario as modelo
import notas.acciones 

class Acciones:

    def registro(self):
        print("A registrarse")
        nombre = input("¿Cual es tu nombre: ")
        apellidos = input("¿Cual es tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
    
        usuario = modelo.Usuario(nombre, apellidos, email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("Perfecto "+ registro[1].nombre + " Estas registrado!")

        else:
            print("No te has registrado correctamente")

    def login(self):
        print("Identifiquese (ahrepolicia): ")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print("Bienvenido " + str(login[1]) + " te has registrado en el sistema el " + str(login[5]))
                self.proximasAcciones(login)
       
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            #print("Error: {}".format(err))
            print("\n Usuario o contraseña incorrectos")
       
        # except mysql.connector.ProgrammingError as err:
        #     if err.errno == errorcode.ER_SYNTAX_ERROR:
        #         print("Check your syntax!")
        #     else:
        #         print("Error: {}".format(err))
            
    def proximasAcciones(self, usuario):
        print(
            """
            Acciones disponibles:
                -Crear notas (crear)
                -Mostrar notas (mostrar)
                -Eliminar notas (eliminar)
                -Salir (salir)
            """)
        accion = input ("Que quiere hacer? ")
        hazEl = notas.acciones.Acciones()


        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion =="mostrar":
            print("MOSTRAR")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("ELIMINAR")
            self.proximasAcciones(usuario)

        elif accion=="salir":
            print("Hasta pronto! ")
            exit()
        