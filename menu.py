##Menu cartas cargadas
def menucc():
        print("1.Cargar Cartas\n"
              "2.Cargar cartas enemigo\n"
              "3.Crear mazo aleatorio\n"
              "4.Crear mazo ofensivo\n"
              "5.Crear mazo defensivo\n"
              "6.Crear mazo equilibrado\n"
              "7.Crear mazo aleatorio Enemigo\n"
              "8.Crear mazo ofensivo Enemigo\n"
              "9.Crear mazo defensivo Enemigo\n"
              "10.Crear mazo equilibrado Enemigo\n"
              "0.Salir")
##Menu cartas cargadas y mazos creados (PARA LUCHAR CONTRA UN BOT)
def menujvsb():
    print("1.Cargar Cartas\n"
          "2.Cargar cartas enemigo\n"
          "3.Crear mazo aleatorio\n"
          "4.Crear mazo ofensivo\n"
          "5.Crear mazo defensivo\n"
          "6.Crear mazo equilibrado\n"
          "7.Crear mazo aleatorio Enemigo\n"
          "8.Crear mazo ofensivo Enemigo\n"
          "9.Crear mazo defensivo Enemigo\n"
          "10.Crear mazo equilibrado Enemigo\n"
          "11.Luchar Jugador vs Bot (arcade)\n"
          "12.Luchar Jugador vs Bot (liga)\n"
          "0.Salir")
##Menu cartas cargadas y mazos creados (PARA LUCHAR CONTRA OTRO JUGADOR)
def menujvsj():
    print("1.Cargar Cartas\n"
          "2.Cargar cartas enemigo\n"
          "3.Crear mazo aleatorio\n"
          "4.Crear mazo ofensivo\n"
          "5.Crear mazo defensivo\n"
          "6.Crear mazo equilibrado\n"
          "7.Crear mazo aleatorio Enemigo\n"
          "8.Crear mazo ofensivo Enemigo\n"
          "9.Crear mazo defensivo Enemigo\n"
          "10.Crear mazo equilibrado Enemigo\n"
          "11.Luchar Jugador vs Jugador\n"
          "12.Luchar Jugador vs Bot (arcade)\n"
          "13.Luchar Jugador vs Bot (liga)\n"
          "0.Salir")
##Comprovar opocion
def comp():
    while True:
        try:
            global opcion
            opcion=int(input("Escoge una opcion"))
            break
        except ValueError:
            print("Opcion incorrecta")
##Menu principal
def menu():
    mec=''
    mc=''
    while True:
        print ("1.Cargar Cartas\n"
               "2.Cargar cartas enemigo\n"
               "0.Salir")
        comp()
        if opcion==1:
            print("Cartas Cargadas")
            cc=True
            while cc==True:
                menucc()
                comp()
                if opcion==1:
                    print("Cartas Cargadas")
                elif opcion == 2:
                    print("Cartas enemigas cargadas")
                    cec=True
                    while cec==True:
                        menucc()
                        comp()
                        if opcion == 1:
                            print("Cartas Cargadas")
                        elif opcion == 2:
                            print("Cartas enemigas cargadas")
                        elif opcion==3:
                            print("mazo creado")
                            mc=True
                            while mc==True and mec==True:
                                menujvsj()
                                break
                        elif opcion == 7:
                            print("mazo enemigo creado")
                            mec=True
                            while mc == True and mec==True:
                                menujvsj()
                                cc=False
                                cec=False
                                mc=False
                                mec=False

                elif opcion==0:
                    break
                else:
                    print("Opcion no valida")
        elif opcion==2:
            print("Cartas Cargadas")
            cc=True
            while cc==True:
                menucc()
                comp()
                if opcion == 1:
                    print("Cartas Cargadas")
            if opcion == 0:
                break
        elif opcion==0:
            break
        else:
            print ("Opcion no valida")
menu()