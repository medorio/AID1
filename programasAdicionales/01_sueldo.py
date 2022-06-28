sueldo = int(input("Ingresa el sueldo: "))
if (sueldo >=1000):
    sueldo = sueldo + (sueldo * 0.15)
    print("Sueldo incrementa 15%")
elif (sueldo <1000):
    sueldo = sueldo 
    print("Sueldo no incrementa")
print(f"El sueldo del empleado es: {sueldo} ")  
