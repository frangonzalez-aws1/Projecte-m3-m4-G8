import random
from modulo.crearMazos import crearMazo
from faseliga import fliga, cargarcartas
def laliga(archivo):
    ##Creamos 'lista' para guardar os random
    lista=[]
    ##Creamos 'partida1' para introducir los 2 jugadores que pelearan
    partida1=[]
    ##Creamos 'partida1' para introducir los 2 siguientes jugadores que pelearan
    partida2=[]
    ##Ponemos en espera al jugador que no ha sido elegido
    espera=[]
    ##Creamos los mazos de cada jugador
    j1 = crearMazo('random', archivo)
    j2 = crearMazo('random', archivo)
    j3 = crearMazo('random', archivo)
    j4 = crearMazo('random', archivo)
    j5 = crearMazo('random', archivo)
    ##Diferenciamos los jugadores y les ponemos sus respectivos mazos
    jugadores = {1: {'jugador': '1', 'puntos': 0, 'mazo': j1},
                 2: {'jugador': '2', 'puntos': 0, 'mazo': j2},
                 3: {'jugador': '3', 'puntos': 0, 'mazo': j3},
                 4: {'jugador': '4', 'puntos': 0, 'mazo': j4},
                 5: {'jugador': '5', 'puntos': 0, 'mazo': j5}}
    ##Introducimos los 2 jugadores a 'pratida1'
    while len(partida1)<2:
        ran=random.randint(1,5)
        ##si el random no esta el la lista introducimos el jugador
        if ran not in lista:
            lista.append(ran)
            partida1.append(jugadores[ran])
    ##Introducimos los 2 jugadores a 'pratida2'
    while len(partida2)<2:
        ran = random.randint(1, 5)
        ##si el random no esta el la lista introducimos el jugador
        if ran not in lista:
            lista.append(ran)
            partida2.append(jugadores[ran])
    ##Introducimos el jugadore sobrante a 'espera'
    while len(espera)<1:
        ran = random.randint(1, 5)
        ##si el random no esta el la lista introducimos el jugador
        if ran not in lista:
            lista.append(ran)
            espera.append(jugadores[ran])
    while True:
        ##Escogemos un random para que empieze la partida
        atp=random.randint(1,2)
        a=fliga(partida1[0]['mazo'], partida1[1]['mazo'], atp)
        ##Escogemos un random para que empieze la partida
        atp=random.randint(1,2)
        b=fliga(partida2[0]['mazo'], partida2[1]['mazo'], atp)
        ##En caso de que ganen los jugadores locales hacemos...
        if a ==True and b==True:
            ##Les sumamos 20 puntos a los ganadores de las partidas
            partida1[0]['puntos'] += 20
            partida2[0]['puntos'] += 20
            ##Introducimos en partida2 el perdedor de 'partida1'
            partida2.append(partida1[1])
            ##Introducimos en espera el ganador de 'partida2'
            espera.append(partida2[0])
            # Introducimos en partida 1 el jugador que esta en 'espera'
            partida1.append(espera[0])
            del partida1[1], espera[0], partida2[0]
        ##En caso de que ganen el jugador local de 'partida1' y el visitante de 'partida2' hacemos...
        elif a==True and b==False:
            ##Les sumamos 20 puntos a los ganadores de las partidas
            partida1[0]['puntos'] += 20
            partida2[1]['puntos'] += 20
            ##Introducimos en partida2 el perdedor de 'partida1'
            partida2.append(partida1[1])
            ##Introducimos en espera el ganador de 'partida2'
            espera.append(partida2[1])
            # Introducimos en partida 1 el jugador que esta en 'espera'
            partida1.append(espera[0])
            del partida1[1], espera[0], partida2[1]
        ##En caso de que ganen el jugador visitante de 'partida1' y el local de 'partida2' hacemos...
        elif a==False and b==True:
            ##Les sumamos 20 puntos a los ganadores de las partidas
            partida1[1]['puntos'] += 20
            partida2[0]['puntos'] += 20
            ##Introducimos en partida2 el perdedor de 'partida1'
            partida2.append(partida1[0])
            ##Introducimos en espera el ganador de 'partida2'
            espera.append(partida2[0])
            # Introducimos en partida 1 el jugador que esta en 'espera'
            partida1.append(espera[0])
            del partida1[0], espera[0], partida2[0]
        ##En caso de que ganen los jugadores visitantes...
        elif a==False and b==False:
            ##Les sumamos 20 puntos a los ganadores de las partidas
            partida1[1]['puntos'] += 20
            partida2[1]['puntos'] += 20
            ##Introducimos en partida2 el perdedor de 'partida1'
            partida2.append(partida1[0])
            ##Introducimos en espera el ganador de 'partida2'
            espera.append(partida2[1])
            #Introducimos en partida 1 el jugador que esta en 'espera'
            partida1.append(espera[0])
            del partida1[0], espera[0], partida2[1]
        ##En caso de que algun jugador llegue a 100 puntos, gana el torneo y se termina la partida
        if jugadores[1]['puntos']==100:
            print("Ha ganado el torneo el jugador 1")
            break
        if jugadores[2]['puntos'] == 100:
            print("Ha ganado el torneo el jugador 2")
            break
        if jugadores[3]['puntos']==100:
            print("Ha ganado el torneo el jugador 3")
            break
        if jugadores[4]['puntos']==100:
            print("Ha ganado el torneo el jugador 4")
            break
        if jugadores[5]['puntos']==100:
            print("Ha ganado el torneo el jugador 5")
            break

