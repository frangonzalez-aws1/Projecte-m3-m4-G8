def jugar():
    while True:
        menujvsb()
        comp()
        if opcion == 1:
            print("Cartas Cargadas")
        elif opcion == 2:
            print("Cartas enemigas cargadas")
        elif opcion == 3:
            print("mazo creado")
        elif opcion == 4:
            print("mazo creado")
        elif opcion == 5:
            print("mazo creado")
        elif opcion == 6:
            print("mazo creado")
        elif opcion == 7:
            print("mazo creado")
        elif opcion == 8:
            print("mazo creado")
        elif opcion == 9:
            print("mazo creado")
        elif opcion == 10:
            print("mazo creado")
        elif opcion == 11:
            print("Pratida terminada")
            break
        elif opcion == 12:
            print("Pratida terminada")
            break
        else:
            print("Opcion Incorrecta")
def jugarpvsp():
    while True:
        menujvsj()
        comp()
        if opcion == 1:
            print("Cartas Cargadas")
        elif opcion == 2:
            print("Cartas enemigas cargadas")
        elif opcion == 3:
            print("mazo creado")
        elif opcion == 4:
            print("mazo creado")
        elif opcion == 5:
            print("mazo creado")
        elif opcion == 6:
            print("mazo creado")
        elif opcion == 7:
            print("mazo creado")
        elif opcion == 8:
            print("mazo creado")
        elif opcion == 9:
            print("mazo creado")
        elif opcion == 10:
            print("mazo creado")
        elif opcion == 11:
            print("Pratida terminada")
            break
        elif opcion == 12:
            print("Pratida terminada")
            break
        elif opcion ==13:
            print("Pratida terminada")
            break
        else:
            print("Opcion Incorrecta")
def comp():
    while True:
        try:
            global opcion
            opcion=int(input("Escoge una opcion"))
            break
        except ValueError:
            print("Opcion incorrecta")
def menucec():
    print("1.Cargar Cartas\n"
          "2.Cargar cartas enemigo\n"
          "3.Crear mazo aleatorio Enemigo\n"
          "4.Crear mazo ofensivo Enemigo\n"
          "5.Crear mazo defensivo Enemigo\n"
          "6.Crear mazo equilibrado Enemigo\n"
          "0.Salir")
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
def menu():
    cc=False
    cec=False
    mc=False
    mec=False
    while True:
        print("1.Cargar Cartas\n"
              "2.Cargar cartas enemigo\n"
              "0.Salir")
        comp()
        if opcion == 1:
            print("cartas cargadas")
            cc=True
            if cc==True and cec ==False:
                while True:
                    menucc()
                    comp()
                    if opcion==1:
                        print("Cartas Cargadas")
                    elif opcion == 2:
                        print("Cartas enemigas cargadas")
                        cec=True
                        break
                    elif opcion==3:
                        print("mazo creado")
                        mc=True
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        elif mc==True and mec==True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion==4:
                        print("mazo creado")
                        mc=True
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        elif mc==True and mec==True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion==5:
                        print("mazo creado")
                        mc=True
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        elif mc==True and mec==True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion==6:
                        print("mazo creado")
                        mc=True
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        elif mc==True and mec==True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 7:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 8:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 9:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 10:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugar()
                            cc = False
                            mc = False
                            mec = False
                            break
            ##Va con la opcion 2
            if cc == True and cec == True:
                while True:
                    menucc()
                    comp()
                    if opcion == 1:
                        print("Cartas Cargadas")
                    elif opcion == 2:
                        print("Cartas enemigas cargadas")
                    elif opcion == 3:
                        print("mazo creado")
                        mc = True
                        if mc == True and mec == False:
                            print("Falta crear el mazo enemigo")
                        elif mc == True and mec == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 4:
                        print("mazo creado")
                        mc = True
                        if mc == True and mec == False:
                            print("Falta crear el mazo enemigo")
                        elif mc == True and mec == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 5:
                        print("mazo creado")
                        mc = True
                        if mc == True and mec == False:
                            print("Falta crear el mazo enemigo")
                        elif mc == True and mec == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 6:
                        print("mazo creado")
                        mc = True
                        if mc == True and mec == False:
                            print("Falta crear el mazo enemigo")
                        elif mc == True and mec == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 7:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 8:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 9:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
                    elif opcion == 10:
                        print("mazo enemigo creado")
                        mec = True
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        elif mec == True and mc == True:
                            jugarpvsp()
                            cc = False
                            cec = False
                            mc = False
                            mec = False
                            break
            else:
                print("Falta crear el mazo aliado")
        elif opcion ==2:
            print("cartas enemigas cartadas")
            cec=True
            if cc==False and cec==True:
                menucec()
                comp()
        elif opcion==0:
            break
menu()