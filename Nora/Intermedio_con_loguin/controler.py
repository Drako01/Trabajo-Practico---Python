"""Se define el modulo Controlador con el patron MVC,
el cual va a conectar los modulos Controlador y vista."""

from tkinter import Tk
from vista import Aplicacion
from vista import Loguin
        
class AppLogin:
    """Clase que da inicio a la pantalla loguin."""
    def __init__(self, ventana):
        objeto = Loguin(ventana)

if __name__ == "__main__":
    root = Tk()
    miapp = AppLogin(root)
    root.mainloop()
    
class AppPrincipal:
    """Clase que da inicio a la aplicación de Agenda de Contactos."""
    def __init__(self, ventana):
        Aplicacion(ventana)
           
if __name__ == "__main__":
    root = Tk()
    miapp = AppPrincipal(root)
    root.mainloop()
