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
def fliga(mazoAli,mazoEne,atp):
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
            return True
        elif jugadores['local']['vida']<=0 and jugadores['enemigo']['vida']>0:
            return False
        elif cnt==3 and jugadores['local']['vida']>jugadores['enemigo']['vida']:
            return True
        elif cnt==3 and jugadores['local']['vida']<jugadores['enemigo']['vida']:
            return False
        elif cnt==3 and jugadores['local']['vida']==jugadores['enemigo']['vida']:
            return False
import xml.etree.ElementTree as ET
def cargarcartas(alioene):
    if alioene == "aliado":
        try:
            archivoa = ET.parse("myBaraja.xml")
            archivoa=archivoa.getroot()
            return archivoa
        except FileNotFoundError:
            print("\nNo se ha podido leer el fichero\n")
            return False, False
    else:
        try:
            archivoe = ET.parse("Enemigo.xml")
            archivoe = archivoe.getroot()
            return archivoe
        except FileNotFoundError:
            print("\nNo se ha podido leer el fichero\n")
            return False, False