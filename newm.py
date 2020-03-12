from modulo.crearMazos import crearMazo
def menu():
    dic={0:".Salir",
        1:".Cargar Cartas",
        2:".Cargar cartas enemigo",
        3:".Crear mazo aleatorio",
        4:".Crear mazo ofensivo",
        5:".Crear mazo defensivo",
        6:".Crear mazo equilibrado",
        7:".Crear mazo aleatorio Enemigo",
        8:".Crear mazo ofensivo Enemigo",
        9:".Crear mazo defensivo Enemigo",
        10:".Crear mazo equilibrado Enemigo",
        11:".Luchar Jugador vs Jugador",
        12:".Luchar Jugador vs Bot (arcade)",
        13:".Luchar Jugador vs Bot (liga)"}
    fali=False
    fene=False
    mazoAli=False
    mazoEne=False
    while True:
        try:
            if fali==False and fene==False:
                for i in range(0,len(dic)):
                    if i <3:
                        print(str(i)+dic[i])

            if fali==True and fene==False:
                for i in range(0,len(dic)):
                    if i <7:
                        print(str(i)+dic[i])
                if mazoAli == True and mazoEne == False:
                    for i in range(0, len(dic)):
                        if i>10 and i!=11:
                            print(str(i) + dic[i])
            if fali==False and fene==True:
                for i in range(0,len(dic)):
                    if i<3 or i>6 and i<11:
                        print(str(i)+dic[i])
            if fali==True and fene==True:
                for i in range(0,len(dic)):
                    if i<11 or i ==14:
                        print(str(i)+dic[i])
                if mazoAli==True and mazoEne==False:
                    for i in range(0, len(dic)):
                        if i >11 and i<14:
                            print(str(i) + dic[i])
                if mazoAli==True and mazoEne==True:
                    for i in range(0, len(dic)):
                        if i >= 11 and i<14:
                            print(str(i) + dic[i])

            opcion=int(input("Escoge una opcion"))
            if opcion==1:
                fali=True
            elif opcion==2:
                fene=True
            elif opcion==3 and fali==True:
                mazoAli=True
            elif opcion == 4 and fali==True:
                mazoAli = True
            elif opcion==5 and fali==True:
                mazoAli=True
            elif opcion==6 and fali==True:
                mazoAli=True
            elif opcion==7 and fene==True:
                mazoEne=True
            elif opcion==8 and fene==True:
                mazoEne=True
            elif opcion==9 and fene==True:
                mazoEne=True
            elif opcion==10 and fene==True:
                mazoEne=True
            elif opcion==11 and mazoAli==True and mazoEne==True:
                pass
            elif opcion==12 and mazoAli==True:
                pass
            elif opcion==13 and mazoEne==True:
                pass
            elif opcion==0:
                print("\nHasta luego\n")
            else:
                print("\nOpcion no valida\n")
        except ValueError:
            print("\nOpcion no valida\n")
menu()