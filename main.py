"""
Proyecto Python + MySql
-Abrir asistente
-Login o registro
-Si registro, creara un usuario en la base de datos
-Si login, identifica el usuario y nos da opciones
-Crear nota, mostrar notas, borrarlas.
"""
print("""
Acciones disponibles:
    -registro
    -login

""")

from usuarios import acciones

hazEl=acciones.Acciones()
accion = input("¿Que quieres hacer?: ")
    
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
  

