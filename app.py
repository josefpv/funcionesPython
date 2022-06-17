from utils.funciones import Matematicas


funcs = Matematicas()

while True:
    
    # Menu
    try:

        funcs.limpiaPantalla()
        [print(fila) for fila in funcs.creaMenu()]
        opcionMenu = int(input("Seleccione una opcion del menu... "))

        if (opcionMenu) == 1:

            numero = int(input("Ingrese un numero entre el 1 y el 15: "))
            if numero >= 1 and numero <= 15:

                if funcs.numeroPrimo(numero):
                    print("El numero es primo")
                else:
                    print("El numero no es primo")
                
                input("Presione cualquier tecla a continuar...")

            else:
                input("Numero fuera del rango, por favor presione cualquier tecla para intentar de nuevo")

        elif opcionMenu == 2:
            
            numero = int(input("Ingrese un numero entre el 3 y el 10: "))
            if numero >= 3 and numero <= 10:
                print(f"Factorial de {numero} es {funcs.factorial(numero)}")

            input("Presione cualquier tecla a continuar...")

        elif opcionMenu == 3:
            funcs.palindrome()
        elif opcionMenu == 4:
            funcs.salir()
        else:
            input("Opcion invalida presione cualquier tecla he intente nuevamente...")

    except Exception() as error:
        input("Opcion invalida presione cualquier tecla he intente nuevamente...")
