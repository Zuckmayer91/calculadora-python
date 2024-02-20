number1=int(input("Ingresa un número:"))
number2=int(input("Ingresa otro número:"))
eleccion= 0

while eleccion != 6:
    print(
    """ Indique la operación a realizar:
    1)suma
    2)resta
    3)multiplicación
    4)división
    5)cambio de valores
    6)salir
    """)

    eleccion = int(input())

    if eleccion == 1:
        print("")
        print("Resultado", number1, "+", number2,"=",number1+number2)
    
    if eleccion == 2:
        print("")
        print("Resultado", number1, "-", number2,"=",number1-number2)

    
    if eleccion == 3:
        print("")
        print("Resultado", number1, "x", number2,"=",number1*number2)


    if eleccion == 4:
        print("")
        print("Resultado", number1, "/", number2,"=",number1/number2)

    if eleccion == 5:        
        number1=int(input("Ingresa un número:"))
        number2=int(input("Ingresa otro número:"))
    
    if eleccion == 6:
        print("Gracias por utilizar la calculadora creada por Bryan")