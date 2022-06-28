v1 = float(input("Velocidad del vehiculo 1: "))
v2 = float(input("Velocidad del vehiculo 2: "))
print("Ingresar la distancia que separa a los vehiculos: ")
d = float(input("Distancia: "))

print("\nSalida: ")

if v1 > 0 and v2 > 0:
    t = d/(v1+v2)
    print(t, "segundos")
else:
    print("Error") 