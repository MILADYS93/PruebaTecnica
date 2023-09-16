
DatosPersonas ={}

#crear 

def CreacionPersona(nombre,apellido,telefono,correo):

    datos={
        'Nombre':nombre,
        'Apellido':apellido,
        'Telefono':telefono,
        'Correo':correo
    }

    DatosPersonas[correo] = datos
    print("se agrego correctamente.")

#leer datos

def leer_Informacion(correo):
    datos = DatosPersonas.get(correo)
    if datos:
      print("Información de la persona:")
      for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    else:
        print("Persona no encontrada.")

 

#  actualizar 
def actualizar_Datos(correo, campo, nuevo_valor):
    dato = DatosPersonas.get(correo)
    if dato:
        if campo in dato:
            dato[campo] = nuevo_valor
            print("Información actualizada con éxito.")
        
    else:
        print("Persona no encontrada.")

 # eliminar
def eliminar_Persona(correo):
    if correo in DatosPersonas:
        del DatosPersonas[correo]
        print(f" la Persona con correo {correo} fue eliminada exitosamente.")
    else:
        print(f"No se encontró ninguna persona con el correo {correo}.")


 # Menú 
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar persona")
    print("2. Leer persona")
    print("3. Actualizar datos")
    print("4. Eliminar datos")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo: ")
        CreacionPersona(nombre, apellido, telefono, correo)
    elif opcion == "2":
        correo = input("Ingrese el correo de la persona que desea leer: ")
        leer_Informacion(correo)
    elif opcion == "3":
        correo = input("Ingrese el correo de la persona que desea actualizar: ")
        campo = input("Ingrese el campo que desea actualizar (Nombre/Apellido/Teléfono/Correo): ")
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
        actualizar_Datos(correo, campo, nuevo_valor)
    elif opcion == "4":
        correo = input("Ingrese el correo de la persona que desea eliminar: ")
        eliminar_Persona(correo)
    elif opcion == "5":
        print("hasta pronto.")
        break
    else:
        print("ingrese un número válido.")