#IMportamos las siguientes funciones
from modulo.crearMazos import crearMazo
from funciones import cargarcartas
from fases import fasepegarvspersona, fasepegar
##Imoportamos el random
import random
def menu():
    ##Creamos el menu
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
    ##Creamos las variables 'fali' y 'fene' para saber si los archivos se han cargado correctamente
    fali=False
    fene=False
    ##Creamos las variable 'mazoAli' y 'mazoEne' para saber si se han creado los mazos correctamente
    mazoAli=False
    mazoEne=False
    ##Creamos la variable 'puntos' para saber los puntos totales que tenemos en 'liga'
    puntos=0
    while True:
        try:
            ##Printamos las opciones de cargar cartas y cargar cartas enemigas
            if fali==False and fene==False:
                for i in range(0,len(dic)):
                    if i <3:
                        print(str(i)+dic[i])
            ##Printamos las opciones de crear mazos aliados
            if fali==True and fene==False:
                for i in range(0,len(dic)):
                    if i <7:
                        print(str(i)+dic[i])
                ##En case de que se haya creado el mazo aliado, tambien mostramos las opciones de luchar contra bot
                if mazoAli == True and mazoEne == False:
                    for i in range(0, len(dic)):
                        if i>10 and i!=11:
                            print(str(i) + dic[i])
            ##Printamos las opciones de crear mazos enemigos
            if fali==False and fene==True:
                for i in range(0,len(dic)):
                    if i<3 or i>6 and i<11:
                        print(str(i)+dic[i])
            ##Printamos las opciones de...
            if fali==True and fene==True:
                ##...crear mazos aliados y enemigos
                for i in range(0,len(dic)):
                    if i<11 or i ==14:
                        print(str(i)+dic[i])
                ##...jugar contra bots
                if mazoAli==True and mazoEne==False:
                    for i in range(0, len(dic)):
                        if i >11 and i<14:
                            print(str(i) + dic[i])
                ##...jugar contra bots y jugar contra otro jugador
                if mazoAli==True and mazoEne==True:
                    for i in range(0, len(dic)):
                        if i >= 11 and i<14:
                            print(str(i) + dic[i])
            ##Escogemos una opcion
            opcion=int(input("Escoge una opcion"))
            ##Cargamos las cartas aliadas y ponemos 'fali' en 'True'
            if opcion==1:
                aliado, fali=cargarcartas('aliado')
            elif opcion==2:
                ##Cargamos las cartas aliadas y ponemos 'fene' en 'True'
                enemigo, fene=cargarcartas('enemigo')
            ##Creamos el mazo aliado y ponemos 'mazoAli' en 'True'
            elif opcion==3 and fali==True:
                Mali=crearMazo('random', aliado)
                mazoAli = True
                ##En caso de que no tengamos el mazo enemigo creado, lo creamos para poder jugar contra el 'bot'
                if mazoEne==False:
                    Mene=crearMazo('random', aliado)
            ##Creamos el mazo aliado y ponemos 'mazoAli' en 'True'
            elif opcion == 4 and fali==True:
                Mali= crearMazo('attack', aliado)
                mazoAli = True
                ##En caso de que no tengamos el mazo enemigo creado, lo creamos para poder jugar contra el 'bot'
                if mazoEne == False:
                    Mene = crearMazo('attack', aliado)
            ##Creamos el mazo aliado y ponemos 'mazoAli' en 'True'
            elif opcion==5 and fali==True:
                Mali= crearMazo('defend', aliado)
                mazoAli = True
                ##En caso de que no tengamos el mazo enemigo creado, lo creamos para poder jugar contra el 'bot'
                if mazoEne == False:
                    Mene = crearMazo('defend', aliado)
            ##Creamos el mazo aliado y ponemos 'mazoAli' en 'True'
            elif opcion==6 and fali==True:
                Mali= crearMazo('balanced', aliado)
                mazoAli=True
                ##En caso de que no tengamos el mazo enemigo creado, lo creamos para poder jugar contra el 'bot'
                if mazoEne == False:
                    Mene= ('balanced', aliado)
            ##Creamos el mazo enemigo y ponemos 'mazoEne' en 'True'
            elif opcion==7 and fene==True:
                Mene = crearMazo('random', enemigo)
                mazoEne = True
                if fali==False:
                    print("Falta cargar el archivo aliado o crear el mazo aliado")
            ##Creamos el mazo enemigo y ponemos 'mazoEne' en 'True'
            elif opcion==8 and fene==True:
                Mene= crearMazo('attack', enemigo)
                mazoEne = True
                if fali==False:
                    print("Falta cargar el archivo aliado o crear el mazo aliado")
            ##Creamos el mazo enemigo y ponemos 'mazoEne' en 'True'
            elif opcion==9 and fene==True:
                Mene = crearMazo('defend', enemigo)
                mazoEne = True
                if fali==False:
                    print("Falta cargar el archivo aliado o crear el mazo aliado")
            ##Creamos el mazo enemigo y ponemos 'mazoEne' en 'True'
            elif opcion==10 and fene==True:
                Mene= crearMazo('balanced', enemigo)
                mazoEne = True
                if fali==False:
                    print("Falta cargar el archivo aliado o crear el mazo aliado")
            ##Empezamos la partida jugador contra jugador
            elif opcion==11 and mazoAli==True and mazoEne==True:
                ##Hacemos la seleccion de quien empieza primero
                atp=random.randint(1,2)
                ##Llamamos a la funcion introduciendo los valores necesarios
                fasepegarvspersona(Mali, Mene, atp)
            ##Empezamos la partida jugador contra bot (arcade)
            elif opcion==12 and mazoAli==True:
                ##Hacemos la seleccion de quien empieza primero
                atp = random.randint(1, 2)
                ##Llamamos a la funcion introduciendo los valores necesarios
                fasepegar(Mali, Mene, atp)
            ##Empezamos la partida jugador contra bot (liga)
            elif opcion==13 and mazoAli==True:
                ##Hacemos la seleccion de quien empieza primero
                atp = random.randint(1, 2)
                ##Llamamos a la funcion introduciendo los valores necesarios
                a=fasepegar(Mali, Mene, atp)
                ##Si ha ganado el mazo aliado sumamos 20 puntos a los puntos de liga
                if a==True:
                    puntos+=20
                    print('Has ganado')
                    print("Puntos Actuales-->", puntos)
                ##Si ha ganado el mazo aliado restamos 10 puntos a los puntos de liga
                elif a==False:
                    puntos -= 10
                    print("Has perdido")
                    print("Puntos Actuales-->", puntos)
            ##Salimos del programa
            elif opcion==0:
                print("\nHasta luego\n")
                break
            ##Si la opcion no es valida...
            else:
                print("\nOpcion no valida\n")
        ##Si la opcion no es valida...
        except ValueError:
            print("\nOpcion no valida\n")
menu()
