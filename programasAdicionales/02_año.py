año = float(input("Ingresa el año: "))

if(año % 100 != 0):
    if(año % 4 == 0):
        print ("Año bisiesto")
    else:
        print ("Año no bisisesto")

elif(año % 400 == 0):
    print ("Año bisiesto")
else:
    print("Año no bisiesto")


