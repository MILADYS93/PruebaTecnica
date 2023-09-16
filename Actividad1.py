from datetime import date

#solicitar el año de nacimiento
Año_Nacimiento = int(input("Ingrese su año de nacimiento: "))

#año actual
Año_actual =date.today().year

#calulando la edad

Edad =Año_actual-Año_Nacimiento

print (f"Tu edad es:{Edad} ")
