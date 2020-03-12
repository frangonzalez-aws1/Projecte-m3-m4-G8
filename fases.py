##Importamos random
import random
def faseinv(dic, dic2):
    ##Creamos una lista para guardar los random
    lista=[]
    while jugadores['local']['pinv']>0 and len(lista)<20:
           try:
               ##Cogemos un numero aleatorio
                ran=random.randint(1,20)
               ##Si ese numero aleatorio no esta en la lista lo añadimos
                if ran not in lista:
                    lista.append(ran)
                    ##Si los puntos de invocacion de esa carta son menores que los
                    ##puntos de invocacion del jugador, invocamos la carta
                    if  dic[ran]['summonPoints']<=jugadores['local']['pinv']:
                        jugadores['local']['pinv']-=dic[int(ran)]['summonPoints']
                        invAli.append(dic[ran])
           except KeyError:
                pass

    lista=[]
    while jugadores['enemigo']['pinv']>0 and len(lista)<20:
        try:
            ##Cogemos un numero aleatorio
            ran = random.randint(1, 20)
            ##Si ese numero aleatorio no esta en la lista lo añadimos
            if ran not in lista:
                lista.append(ran)
                ##Si los puntos de invocacion de esa carta son menores que los
                ##puntos de invocacion del jugador, invocamos la carta
                if dic2[ran]['summonPoints'] <= jugadores['enemigo']['pinv']:
                    jugadores['enemigo']['pinv'] -= dic2[int(ran)]['summonPoints']
                    invEne.append(dic2[ran])
        except KeyError:
            pass
    jugadores['local']['pinv']=5
    jugadores['enemigo']['pinv']=5
    return invAli, invEne
def fasepegarvspersona(mazoAli,mazoEne,atp):
    global invAli, invEne, jugadores
    ##Creamos la variable jugadores con la vida y los puntos de invocacion de cada jugador
    jugadores = {'local': {'vida': 10, 'pinv': 5, }, 'enemigo': {'vida': 10, 'pinv': 5}}
    ##Creamos las variables 'invAli' y 'invEne' para guardar las cartas invocadas
    invAli = []
    invEne = []
    ##Creamos los siguientes contadores
    ##'cnt' lo utilizamos para cuando en 3 turnos diferentes no se haya hecho nada se termine la partida
    cnt=0
    ##'cnt2' lo utilizamos para cuando en un mismo turno no se haya nada se vuelvan a invocar las cartas
    cnt2=0
    print("Comienza el jugador",atp)
    while jugadores['local']['vida']>0 and jugadores['enemigo']['vida']>0 and cnt<3:
        ##Si despues de pelear, uno de los jugadores se queda sin cartas invocadas, volvemos a invocar
        if len(invAli)==0 or len(invEne)==0 or cnt2==2:
            invEne=[]
            invAli=[]
            ##Llamamos a la funcion para invocar las cartas
            faseinv(mazoAli, mazoEne)
            print("El jugador 1 (Aliado) ha invocado a:", invAli)
            print("El jugador 2 (Enemigo) ha invocado a:", invEne)
            input("Pulse enter para iniciar la fase de combate")
            if atp==1:
                print("Turno del jugador 1 (Aliado)")
                try:
                    for i in range (0,len(invAli)):
                        ##Si el daño multiplicado por 2 es mayor a la defensa...
                        if (invAli[i]['attack']*2)-invEne[i]['defense']>=0:
                            ##Comprobamos si el 'tipo' de carta es fuerte contra la otra
                            if invAli[i]['type']=='infantry' and invEne[i]['type']=='lancer':
                                ##En caso de que lo sea multiplicamos el danyo por 2
                                jugadores['enemigo']['vida']-= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                ##Borramos la carta invocada
                                del[invEne[i]]
                                atp = 2
                                ##Ponemos las variables a 0
                                cnt2 = 0
                                cnt = 0
                            ##Comprobamos si el 'tipo' de carta es fuerte contra la otra
                            elif invAli[i]['type']=='lancer' and invEne[i]['type']=='chivalry':
                                ##En caso de que lo sea multiplicamos el danyo por 2
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                ##Borramos la carta invocada
                                del [invEne[i]]
                                atp = 2
                                ##Ponemos las variables a 0
                                cnt2 = 0
                                cnt = 0
                            ##Comprobamos si el 'tipo' de carta es fuerte contra la otra
                            elif invAli[i]['type'] == 'chivalry' and invEne[i]['type'] == 'infantry':
                                ##En caso de que lo sea multiplicamos el danyo por 2
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                ##Borramos la carta invocada
                                del [invEne[i]]
                                atp = 2
                                ##Ponemos las variables a 0
                                cnt2 = 0
                                cnt = 0
                            ##En caso de que no tenga vetaja de tipo hacemos la resta normal
                            elif invAli[i]['attack']-invEne[i]['defense']>=0:
                                ##Hacemos la resta normal
                                jugadores['enemigo']['vida'] -= invAli[i]['attack'] - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:",invEne[i]['name'] )
                                ##Borramos la carta invocada
                                del [invEne[i]]
                                atp = 2
                                ##Ponemos las variables a 0
                                cnt2 = 0
                                cnt = 0
                            else:
                                ##Si no hay cambios printamos...
                                atp = 2
                                print("Esta carta(",invAli[i]['name'],") no ha hecho nada")
                        else:
                            ##Si no hay cambios printamos...
                            atp = 2
                            print("Esta carta(", invAli[i]['name'], ") no ha hecho nada")
                except IndexError:
                    ##Si no hay cartas invocadas enemigas se ataca directamente
                    for x in range(i,len(invAli)):
                        ##Restamos la vida al
                        jugadores['enemigo']['vida'] -= invAli[x]['attack']
                        print("Esta carta(", invAli[i]['name'], ")  ha hecho un ataque directo")
                    atp = 2
                    ##Ponemos las variables a 0
                    cnt2 = 0
                    cnt = 0
                print("Fin del turno del Jugador 1 (Aliado)")
                input("Pulse enter para continuar")
            ##Cambiamos 'atp' a 2
            atp=2
            if atp==2:
                print("Turno del jugador 2 (Enemigo)")
                try:
                    for i in range (0,len(invEne)):
                        if (invEne[i]['attack']*2)-invAli[i]['defense']>=0:
                            if invEne[i]['type'] == 'infantry' and invAli[i]['type'] == 'lancer ':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                print("Jugador 2 (enemigo) ha elimnado a:", invAli[i]['name'])
                                del [invAli[i]]
                                atp=1
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['type'] == 'lancer' and invAli[i]['type'] == 'chivalry':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                print("Jugador 2 (enemigo) ha elimnado a:", invAli[i]['name'])
                                del [invAli[i]]
                                atp=1
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['type'] == 'chivalry' and invAli[i]['type'] == 'infantry':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                print("Jugador 2 (enemigo) ha elimnado a:", invAli[i]['name'])
                                del [invAli[i]]
                                atp=1
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['attack']-invAli[i]['defense']>=0:
                                jugadores['local']['vida'] -= invEne[i]['attack'] - invAli[i]['defense']
                                print("Jugador 2 (enemigo) ha elimnado a:", invAli[i]['name'])
                                del [invAli[i]]
                                atp=1
                                cnt2 = 0
                                cnt=0
                            else:
                                atp=1
                                print("Esta carta(", invEne[i]['name'], ") no ha hecho nada")
                        else:
                            atp=1
                            print("Esta carta(", invEne[i]['name'], ") no ha hecho nada")

                except IndexError:
                    for x in range(i,len(invEne)):
                        jugadores['local']['vida'] -= invEne[x]['attack']
                        print("Esta carta(", invEne[i]['name'], ")ha hecho un ataque directo")
                    atp=1
                    cnt2 = 0
                    cnt = 0
        atp=1
        print("Fin del turno del Jugador 2 (Enemigo)")
        ##Sumamos 1 a los dos contadores
        cnt2+=1
        cnt+=1
        ##Printamos los puntos de vida de cada jugador en cada turno
        print('El jugador 1(aliado)tiene', jugadores['local']['vida'],"puntos de vida")
        print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'],"puntos de vida")
        ##Si gana el jugador aliado devolvemos 'True', y si pierde devolvemos 'False'
        if jugadores['local']['vida'] > 0 and jugadores['enemigo']['vida'] <= 0:
            print("Pratida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar")
            return True
        elif jugadores['local']['vida'] <= 0 and jugadores['enemigo']['vida'] > 0:
            print("Pratida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar")
            return False
        elif cnt == 3 and jugadores['local']['vida'] > jugadores['enemigo']['vida']:
            print("Pratida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar")
            return True
        elif cnt == 3 and jugadores['local']['vida'] < jugadores['enemigo']['vida']:
            print("Pratida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar")
            print()
            return False
        elif cnt == 3 and jugadores['local']['vida'] == jugadores['enemigo']['vida']:
            print("Pratida finalizada, ha quedado en un empate")
            input("Pulse enter para continuar")
            return False
        input("Pulse enter para continuar")

def fasepegar(mazoAli,mazoEne,atp):
    global invAli, invEne, jugadores
    jugadores = {'local': {'vida': 10, 'pinv': 5, }, 'enemigo': {'vida': 10, 'pinv': 5}}
    invAli = []
    invEne = []
    cnt=0
    cnt2=0
    while jugadores['local']['vida']>0 and jugadores['enemigo']['vida']>0 and cnt<3:
        if len(invAli)==0 or len(invEne)==0 or cnt2==2:
            invEne=[]
            invAli=[]
            faseinv(mazoAli, mazoEne)
            if atp==1:
                try:
                    for i in range (0,len(invAli)):
                        if (invAli[i]['attack']*2)-invEne[i]['defense']>=0:
                            if invAli[i]['type']=='infantry' and invEne[i]['type']=='lancer':
                                jugadores['enemigo']['vida']-= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print()
                                del[invEne[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['type']=='lancer' and invEne[i]['type']=='chivalry':
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                del [invEne[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['type'] == 'chivalry' and invEne[i]['type'] == 'infantry':
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                del [invEne[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['attack']-invEne[i]['defense']>=0:
                                jugadores['enemigo']['vida'] -= invAli[i]['attack'] - invEne[i]['defense']
                                del [invEne[i]]
                                cnt2 = 0
                                cnt = 0
                except IndexError:
                    for x in range(i,len(invAli)):
                        jugadores['enemigo']['vida'] -= invAli[x]['attack']
                    cnt2 = 0
                    cnt = 0
            atp=2
            if atp==2:
                try:
                    for i in range (0,len(invEne)):
                        if (invEne[i]['attack']*2)-invAli[i]['defense']>=0:
                            if invEne[i]['type'] == 'infantry' and invAli[i]['type'] == 'lancer ':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                del [invAli[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['type'] == 'lancer' and invAli[i]['type'] == 'chivalry':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                del [invAli[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['type'] == 'chivalry' and invAli[i]['type'] == 'infantry':
                                jugadores['local']['vida'] -= (invEne[i]['attack']*2) - invAli[i]['defense']
                                del [invAli[i]]
                                cnt2 = 0
                                cnt = 0
                            elif invEne[i]['attack']-invAli[i]['defense']>=0:
                                jugadores['local']['vida'] -= invEne[i]['attack'] - invAli[i]['defense']
                                del [invAli[i]]
                                cnt2 = 0
                                cnt=0
                except IndexError:
                    for x in range(i,len(invEne)):
                            jugadores['local']['vida'] -= invEne[x]['attack']
                    cnt2 = 0
                    cnt = 0
        atp=1
        cnt2+=1
        cnt+=1
        if jugadores['local']['vida']>0 and jugadores['enemigo']['vida']<=0:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Partida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar")
            return True
        elif jugadores['local']['vida']<=0 and jugadores['enemigo']['vida']>0:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Partida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar")
            return False
        elif cnt==3 and jugadores['local']['vida']>jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Partida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar")
            return True
        elif cnt==3 and jugadores['local']['vida']<jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Partida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar")
            print()
            return False
        elif cnt==3 and jugadores['local']['vida']==jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Partida finalizada, ha quedado en un empate")
            input("Pulse enter para continuar")
            return False