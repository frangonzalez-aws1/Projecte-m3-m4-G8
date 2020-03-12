from avqs2 import crearMazo
def menu(opcion, mazoEne, mazoAli, aene):

    dic={1:".Cargar Cartas",
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
        13:".Luchar Jugador vs Bot (liga)",
        14:".Salir"}

    while opcion !=14:
        try:
            for i in range (1, len(dic)+1):
                if i ==1 or i ==2 or i ==14:
                    print(str(i)+dic[i])

            opcion=int(input("Escoge una opcion"))

            if opcion ==1 or opcion==2:
                for i in range (1,len(dic)+1):
                    if i<11 or i>13 :
                        print(str(i)+dic[i])
                break
            if opcion>=3 and opcion<=6:
                if mazoEne==0:
                    for i in range(1, len(dic) + 1):
                        if  i<11 or i>13:
                            print(str(i) + dic[i])
                else:
                    for i in range(1, len(dic) + 1):
                        if  i!=11:
                            print(str(i) + dic[i])
                break

            if opcion >= 7 and opcion <= 10:
                if mazoAli == 0:
                    for i in range(1, len(dic) + 1):
                        if i < 11 or i > 13:
                            print(str(i) + dic[i])
                else:
                    for i in range(1, len(dic) + 1):
                        if i != 11:
                            print(str(i) + dic[i])
                break

            if opcion >= 11 and opcion <= 13:
                if aene == 1:
                    for i in range(1, len(dic) + 1):
                            print(str(i) + dic[i])
                else:
                    for i in range(1, len(dic) + 1):
                        if i != 11:
                            print(str(i) + dic[i])
                break
            if opcion==14:
                print("\nHa sido un placer")

            if opcion>14:
                print("\nOpcion no valida\n")
        except ValueError:
            print("\nOpcion no valida\n")
opcion=3
mazoEne=1
mazoAli=0
aene=0
menu(opcion, mazoEne, mazoAli, aene)