import xml.etree.ElementTree as ET
##cargamos el xml con las cartas
def c(alioene):
    if alioene == "aliado":
        try:
            archivoa = ET.parse("myBaraja.xml")
            return archivoa
        except FileNotFoundError:
            return False
    else:
        try:
            archivoe = ET.parse("Enemigo.xml")
            return archivoe
        except FileNotFoundError:
            print("No se ha podido leer el fichero")
##menu mazos creados (jvsb)
def jugar():
    while True:
        menujvsb()
        comp()
        if opcion == 1:
            c("aliado")
            print("Cartas Cargadas")
        elif opcion == 2:
            c("enemigo")
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
##Menu mazos creado (jvsj)
def jugarpvsp():
    while True:
        menujvsj()
        comp()
        if opcion == 1:
            c("aliado")
            print("Cartas Cargadas")
        elif opcion == 2:
            c("enemigo")
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
##Comprovar opcion
def comp():
    while True:
        try:
            global opcion
            opcion=int(input("Escoge una opcion"))
            break
        except ValueError:
            print("Opcion incorrecta")
##Menu cartas cargadas enemigas
def menucec():
    print("1.Cargar Cartas\n"
          "2.Cargar cartas enemigo\n"
          "3.Crear mazo aleatorio Enemigo\n"
          "4.Crear mazo ofensivo Enemigo\n"
          "5.Crear mazo defensivo Enemigo\n"
          "6.Crear mazo equilibrado Enemigo\n"
          "0.Salir")
##Menu cartas aliadas y enemigas cargadas
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
##Menu jugador vs bot
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
##Menu jugador vs jugador
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
    ##cartas aliadas cargadas
    cc=False
    ##cartas enemigas cargadas
    cec=False
    ##mazo aliado creado
    mc=False
    ##mazo enemigo creado
    mec=False
    while True:
        print("1.Cargar Cartas\n"
              "2.Cargar cartas enemigo\n"
              "0.Salir")
        comp()
        ##cargamos cartas aliadas y ponemos "cc" en True(Cargar cartas aliadas)
        if opcion == 1:
            if c('aliado') is not False:
                print('Cartas cargadas')
            print("cartas cargadas")
            cc=True
            ##comprovamos que "cc" este en True (cargar cartas aliadas) y mostramos la siguiente parte del menu
            if cc==True and cec ==False:
                while True:
                    menucc()
                    comp()
                    if opcion==1:
                        c("aliado")
                        print("Cartas Cargadas")
                    ##Cargamos las cartas enemigas, ponemos "cec" en True(cargar enemigas cargadas) y hacemos un break para mostrar el siguiente menu
                    elif opcion == 2:
                        c("enemigo")
                        print("Cartas enemigas cargadas")
                        cec=True
                        break
                    ##Creamos el mazo aliado y ponemos "mc" en true
                    elif opcion==3:
                        print("mazo creado")
                        mc=True
                        ##En caso de que solo tengamos el mazo aliado creado nos saltara un aviso de que falta crear el mazo enemigo
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mc==True and mec==True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mc" en true
                    elif opcion==4:
                        print("mazo creado")
                        mc=True
                        ##En caso de que solo tengamos el mazo aliado creado nos saltara un aviso de que falta crear el mazo enemigo
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mc==True and mec==True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mc" en true
                    elif opcion==5:
                        print("mazo creado")
                        mc=True
                        ##En caso de que solo tengamos el mazo aliado creado nos saltara un aviso de que falta crear el mazo enemigo
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mc==True and mec==True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mc" en true
                    elif opcion==6:
                        print("mazo creado")
                        mc=True
                        ##En caso de que solo tengamos el mazo aliado creado nos saltara un aviso de que falta crear el mazo enemigo
                        if mc==True and mec==False:
                            print("Falta crear el mazo enemigo")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mc==True and mec==True:
                            jugar()
                            ##una vez terminada la prtida ponemos todas las variables en false y volveremos al menu principal
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mec" en true
                    elif opcion == 7:
                        print("mazo enemigo creado")
                        mec = True
                        ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mec == True and mc == True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mec" en true
                    elif opcion == 8:
                        print("mazo enemigo creado")
                        mec = True
                        ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mec == True and mc == True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mec" en true
                    elif opcion == 9:
                        print("mazo enemigo creado")
                        mec = True
                        ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mec == True and mc == True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
                    ##Creamos el mazo aliado y ponemos "mec" en true
                    elif opcion == 10:
                        print("mazo enemigo creado")
                        mec = True
                        ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                        if mec == True and mc == False:
                            print("Falta crear el mazo aliado")
                        ##en caso de tener los 2 mazos creados nos mostrara el siguiente menu
                        elif mec == True and mc == True:
                            jugar()
                            ##En caso de que solo tengamos el mazo enemigo creado nos saltara un aviso de que falta crear el mazo aliado
                            cc = False
                            mc = False
                            mec = False
                            break
            ##Una vez cargadas las cartas enemigas y hecho el break, hacemos la comprovacion de que sea correcto que tenemos los 2 mazos cargados
            if cc == True and cec == True:
                while True:
                    menucc()
                    comp()
                    if opcion == 1:
                        c("aliado")
                    elif opcion == 2:
                        c("enemigo")
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
            elif cc==False and cec==True:
                print("Falta crear el mazo aliado")
        elif opcion == 2:
            c("enemigo")
            print('Cartas enemigas cargadas')
            cec= True
            if cec == True and cc == False:
                while True:
                    menucec()
                    comp()
                    if opcion == 1:
                        c("aliado")
                        print('Cartas aliadas cargadas')
                        cc = True
                        break
                    elif opcion == 2:
                        c("enemigo")
                        print('Cartas enemigas cargadas')
                    elif opcion == 3:
                        print('Mazo enemigo creado')
                        mec = True
                        if mec == True and mc == False:
                            if mc==False and cc==False:
                                    print('Falta cargar y crear el mazo aliado')
                            elif mc ==False and cc==True:
                                print("Falta crear el mazo enemigo")
                        elif mc == True and mec == True:
                            jugar()
                            cc = False
                            cec=False
                            mc = False
                            mec = False
                            break
                    elif opcion == 4:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                if mc == False and cc == False:
                                    print('Falta cargar y crear el mazo aliado')
                                elif mc == False and cc == True:
                                    print("Falta crear el mazo enemigo")
                            elif mc == True and mec == True:
                                jugar()
                                cc = False
                                cec = False
                                mc = False
                                mec = False
                                break
                    elif opcion == 5:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                if mc == False and cc == False:
                                    print('Falta cargar y crear el mazo aliado')
                                elif mc == False and cc == True:
                                    print("Falta crear el mazo enemigo")
                            elif mc == True and mec == True:
                                jugar()
                                cc = False
                                cec = False
                                mc = False
                                mec = False
                                break
                    elif opcion == 6:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                if mc == False and cc == False:
                                    print('Falta cargar y crear el mazo aliado')
                                elif mc == False and cc == True:
                                    print("Falta crear el mazo enemigo")
                            elif mc == True and mec == True:
                                jugar()
                                cc = False
                                cec = False
                                mc = False
                                mec = False
                                break

                if cc == True and cec == True:
                    while True:
                        menucc()
                        comp()
                        if opcion == 1:
                            c("aliado")
                            print('Cartas aliadas cargadas')
                        elif opcion == 2:
                            c("enemigo")
                            print('Cartas enemigas cargadas')
                        elif opcion == 3:
                            print('Mazo aliado creado')
                            mc = True
                            if mc == True and mec == False:
                                print('Falta crear el mazo aliado')
                            elif mc == True and mec == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 4:
                            print('Mazo aliado creado')
                            mc = True
                            if mc == True and mec == False:
                                print('Falta crear el mazo aliado')
                            elif mc == True and mec == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 5:
                            print('Mazo aliado creado')
                            mc = True
                            if mc == True and mec == False:
                                print('Falta crear el mazo aliado')
                            elif mc == True and mec == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 6:
                            print('Mazo aliado creado')
                            mc = True
                            if mc == True and mec == False:
                                print('Falta crear el mazo aliado')
                            elif mc == True and mec == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 7:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                print('Falta crear el mazo aliado')
                            elif mec == True and mc == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 8:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                print('Falta crear el mazo aliado')
                            elif mec == True and mc == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 9:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                print('Falta crear el mazo aliado')
                            elif mec == True and mc == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                        elif opcion == 10:
                            print('Mazo enemigo creado')
                            mec = True
                            if mec == True and mc == False:
                                print('Falta crear el mazo aliado')
                            elif mec == True and mc == True:
                                jugarpvsp()
                                cc = False
                                cec = False
                                mec = False
                                mc = False
                                break
                else:
                    print('Falta crear el mazo aliado')
        elif opcion==0:
            print("Adios")
            break
menu()
