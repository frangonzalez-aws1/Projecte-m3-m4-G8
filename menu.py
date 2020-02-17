def menu():
    while True:
        print ("1.Cargar Cartas\n"
               "2.Cargar cartas enemigo\n"
               "3.Salir")
        while True:
            try:
                opcion=int(input("Escoge una opcion"))
                break
            except ValueError:
                print ("Opcion incorrecta")
        if opcion==1:
            pass
        elif opcion==2:
            pass
        elif opcion==3:
            break
        else:
            print ("opcion no valida")
menu()