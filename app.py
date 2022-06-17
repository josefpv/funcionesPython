from utils.funciones import Matematicas


funcs = Matematicas()

while True:
    
    # Menu
    try:

        funcs.limpiaPantalla()
        [print(fila) for fila in funcs.creaMenu()]
        opcionMenu = int(input("Seleccione una opcion del menu... "))

        if (opcionMenu) == 1:
            funcs.numeroPrimo()
        elif opcionMenu == 2:
            funcs.factorial()
        elif opcionMenu == 3:
            funcs.palindrome()
        elif opcionMenu == 4:
            funcs.salir()
        else:
            input("Opcion invalida presione cualquier tecla he intente nuevamente...")

    except Exception() as error:
        input("Opcion invalida presione cualquier tecla he intente nuevamente...")
