let number1 = parseInt(prompt("Ingresa un número:"));
let number2 = parseInt(prompt("Ingresa otro número:"));
let eleccion = 0;

while (eleccion != 6) {
    console.log(
    `Indique la operación a realizar:
    1)suma
    2)resta
    3)multiplicación
    4)división
    5)cambio de valores
    6)salir`
    );

    eleccion = parseInt(prompt("Elige una opción:"));

    if (eleccion == 1) {
        console.log("Resultado", number1, "+", number2,"=",number1+number2);
    }
    
    if (eleccion == 2) {
        console.log("Resultado", number1, "-", number2,"=",number1-number2);
    }
    
    if (eleccion == 3) {
        console.log("Resultado", number1, "x", number2,"=",number1*number2);
    }

    if (eleccion == 4) {
        console.log("Resultado", number1, "/", number2,"=",number1/number2);
    }

    if (eleccion == 5) {        
        number1 = parseInt(prompt("Ingresa un número:"));
        number2 = parseInt(prompt("Ingresa otro número:"));
    }
    
    if (eleccion == 6) {
        console.log("Gracias por utilizar la calculadora creada por Bryan");
    }
}
