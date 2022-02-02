""" Problema propuesto
Confeccionar una clase que administre una agenda personal.
Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el apellido de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa."""
#agregar sqlite
#agregar tkinter

class Agenda:
    def __init__(self):
        self.apellido=[]
        self.nombre=[]
        self.telefono=[]
        self.email=[]
        self.direccion=[]
    def menu(self):
        opcion=0
        while opcion!=6:
            print("*  M  E  N  U  *")
            print("1- Cargar contacto")
            print("2- Listar contactos")
            print("3- Buscar contactos")
            print("4- Eliminar contacto")
            print("5- Modificar contacto")
            print("6- Salir de la agenda")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.buscar()
            elif opcion==4:
                self.eliminar()
            elif opcion==5:
                self.modificar()

    def cargar(self):
            ape=input("Ingrese apellido del contacto : ")
            self.apellido.append(ape)
            nom=input("Ingrese nombre del contacto : ")
            self.nombre.append(nom)
            tel=input("Ingrese telefono : ")
            self.telefono.append(tel)
            ema=input("Ingrese email ")
            self.email.append(ema)
            dir=input("Ingrese direccion del contacto ")
            self.direccion.append(dir)

    def listar(self):
        print("***** Listado completo de la agenda *****")
        a=len(self.apellido)
        print("NUMERO DE REGISTROS INGRESADOS : ",a)
        for x in range(a):
            print(self.apellido[x],
                  self.nombre[x],
                  self.telefono[x],
                  self.email[x],
                  self.direccion[x])
        print("_____________________") 

    def buscar(self):
        print("______________________________________________")        
        apellido=input("Ingrese el apellido de la persona a consultar:")
        if apellido in self.apellido:
            x=self.apellido.index(apellido)
            print(self.apellido[x],
                  self.nombre[x],
                  self.telefono[x],
                  self.email[x],
                  self.direccion[x])
        else:
            print("No existe un contacto con ese nombre ")
        print("______________________________________________") 
    def eliminar(self):
        print("luego de eliminar un contacto no puede recuperarse ")        
        apellido=input("Ingrese el apellido del contacto a eliminar: ")
        if apellido in self.apellido:
            x=self.apellido.index(apellido)
            print(self.apellido.pop(x),
                  self.nombre.pop(x),
                  self.telefono.pop(x),
                  self.email.pop(x),
                  self.direccion.pop(x))
            print("el contacto: ",apellido," ha sido eliminado ")
        else:
            print("No existe un contacto con ese apellido")
        print("______________________________________________")
    def modificar(self):
        print("aqui vamos a modificar un contacto")        
        apellido=input("Ingrese el apellido del contacto a modificar: ")
        if apellido in self.apellido:
            x=self.apellido.index(apellido)
            print("datos de este contacto a modificar")
            print(self.apellido.pop(x),
                  self.nombre.pop(x),
                  self.telefono.pop(x),
                  self.email.pop(x),
                  self.direccion.pop(x))
            opcion=0
            while opcion!=6:
                print("*  M  E  N  U  modificacion de contacto *")
                print("1- Modificar apellido")
                print("2- Modificar Nombre")
                print("3- Modificar telefono")
                print("4- Modificar email")
                print("5- Modificar direccion postal")
                print("6- Salir menu modificacion")
                opcion=int(input("Ingrese su opcion:"))
                if opcion==1:
                    nuevoval=input("Apellido nuevo: ")
                    self.apellido.insert(x,nuevoval)
                elif opcion==2:
                    nombnuevo=input("Nombre nuevo :")
                    self.nombre.insert(x,nombnuevo)
                elif opcion==3:
                    telnue=input("Nuevo telefono: ")
                    self.telefono.insert(x,telnue)
                elif opcion==4:
                    emailn=input("Email nuevo: ")
                    self.email.insert(x,emailn)
                elif opcion==5:
                    direcnue=input("Direccion nuevo: ")
                    self.direccion.insert(x,direcnue)
                elif opcion==6:
                    self.menu()
        else:
            print("No existe un contacto con ese apellido")
        print("______________________________________________")

agenda=Agenda()
agenda.menu()