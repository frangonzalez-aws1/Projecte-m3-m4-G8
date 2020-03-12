import random
def faseinv(dic, dic2):
    lista=[]
    while jugadores['local']['pinv']>0 and len(lista)<20:
           try:
                ran=random.randint(1,20)
                if ran not in lista:
                    lista.append(ran)
                    if  dic[ran]['summonPoints']<=jugadores['local']['pinv']:
                        jugadores['local']['pinv']-=dic[int(ran)]['summonPoints']
                        invAli.append(dic[ran])
           except KeyError:
                pass

    lista=[]
    while jugadores['enemigo']['pinv']>0 and len(lista)<20:
            try:
                ran=random.randint(1,20)
                if ran not in lista:
                    lista.append(ran)
                    if dic2[ran]['summonPoints']<=jugadores['enemigo']['pinv']:
                            jugadores['enemigo']['pinv']-=dic2[ran]['summonPoints']
                            invEne.append(dic2[ran])
            except KeyError:
                pass
    jugadores['local']['pinv']=5
    jugadores['enemigo']['pinv']=5
    return invAli, invEne
def fasepegarvspersona(mazoAli,mazoEne,atp):
    global invAli, invEne, jugadores
    jugadores = {'local': {'vida': 10, 'pinv': 5, }, 'enemigo': {'vida': 10, 'pinv': 5}}
    invAli = []
    invEne = []
    cnt=0
    cnt2=0
    print("Comienza el jugador",atp)
    while jugadores['local']['vida']>0 and jugadores['enemigo']['vida']>0 and cnt<3:
        if len(invAli)==0 or len(invEne)==0 or cnt2==2:
            invEne=[]
            invAli=[]
            faseinv(mazoAli, mazoEne)
            print("El jugador 1 (Aliado) ha invocado a:", invAli)
            print("El jugador 2 (Enemigo) ha invocado a:", invEne)
            input("Pulse enter para iniciar la fase de combate")
            if atp==1:
                print("Turno del jugador 1 (Aliado)")
                try:
                    for i in range (0,len(invAli)):
                        if (invAli[i]['attack']*2)-invEne[i]['defense']>=0:
                            if invAli[i]['type']=='infantry' and invEne[i]['type']=='lancer':
                                jugadores['enemigo']['vida']-= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                del[invEne[i]]
                                atp = 2
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['type']=='lancer' and invEne[i]['type']=='chivalry':
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                del [invEne[i]]
                                atp = 2
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['type'] == 'chivalry' and invEne[i]['type'] == 'infantry':
                                jugadores['enemigo']['vida'] -= (invAli[i]['attack']*2) - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:", invEne[i]['name'])
                                del [invEne[i]]
                                atp = 2
                                cnt2 = 0
                                cnt = 0
                            elif invAli[i]['attack']-invEne[i]['defense']>=0:
                                jugadores['enemigo']['vida'] -= invAli[i]['attack'] - invEne[i]['defense']
                                print("Jugador 1 (aliado) ha elimnado a:",invEne[i]['name'] )
                                del [invEne[i]]
                                atp = 2
                                cnt2 = 0
                                cnt = 0
                            else:
                                atp = 2
                                print("Esta carta(",invAli[i]['name'],") no ha hecho nada")
                        else:
                            atp = 2
                            print("Esta carta(", invAli[i]['name'], ") no ha hecho nada")

                except IndexError:
                    for x in range(i,len(invAli)):
                        jugadores['enemigo']['vida'] -= invAli[x]['attack']
                        print("Esta carta(", invAli[i]['name'], ")  ha hecho un ataque directo")
                    atp = 2
                    cnt2 = 0
                    cnt = 0
                print("Fin del turno del Jugador 1 (Aliado)")
                input("Pulse enter para continuar")
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
        cnt2+=1
        cnt+=1
        print('El jugador 1(aliado)tiene', jugadores['local']['vida'],"puntos de vida")
        print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'],"puntos de vida")
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
            if atp == 1:
                atp = 2
            elif atp == 2:
                atp = 1
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
        if atp ==1:
            atp=2
        elif atp==2:
            atp=1
        cnt2+=1
        cnt+=1
        if jugadores['local']['vida']>0 and jugadores['enemigo']['vida']<=0:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Pratida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar\n")
            return True
        elif jugadores['local']['vida']<=0 and jugadores['enemigo']['vida']>0:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Pratida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar\n")
            return False
        elif cnt==3 and jugadores['local']['vida']>jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Pratida finalizada, ha ganado el jugador 1 (aliado)")
            input("Pulse enter para continuar\n")
            return True
        elif cnt==3 and jugadores['local']['vida']<jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Pratida finalizada, ha ganado el jugador 2 (enemigo)")
            input("Pulse enter para continuar\n")
            print()
            return False
        elif cnt==3 and jugadores['local']['vida']==jugadores['enemigo']['vida']:
            print('El jugador 1(aliado)tiene', jugadores['local']['vida'], "puntos de vida")
            print('El jugador 2(enemigo)tiene', jugadores['enemigo']['vida'], "puntos de vida")
            print("Pratida finalizada, ha quedado en un empate")
            input("Pulse enter para continuar\n")
            return False