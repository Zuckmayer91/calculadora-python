def ingresar_numeros():
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    return num1, num2

def realizar_operacion(operacion, num1, num2):
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: No se puede dividir por cero.")
            return None
    else:
        return None

def main():
    num1, num2 = ingresar_numeros()
    eleccion = 0

    while eleccion != 6:
        print(
            """ Indique la operación a realizar:
            1) suma
            2) resta
            3) multiplicación
            4) división
            5) cambio de valores
            6) salir
            """)

        eleccion = int(input())

        if eleccion in range(1, 5):
            resultado = realizar_operacion(eleccion, num1, num2)
            if resultado is not None:
                print(f"Resultado: {resultado}")
        elif eleccion == 5:
            num1, num2 = ingresar_numeros()
        elif eleccion == 6:
            print("Gracias por utilizar la calculadora creada por Bryan")

if __name__ == "__main__":
    main()
