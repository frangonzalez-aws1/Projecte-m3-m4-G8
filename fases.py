import random
def faseinv(dic, dic2):
    invAli=[]
    invEne=[]
    lista=[]
    while jugadores['local']['pinv']>0 and len(lista)<20:
           try:
                ran=random.randint(1,20)
                if ran not in lista:
                    lista.append(ran)
                    if  dic[ran]['summonPoints']<=jugadores['local']['pinv']:
                        jugadores['local']['pinv']-=dic[int(ran)]['summonPoints']
                        invAli.append(dic[ran])
                        del dic[int(ran)]
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
                            del dic2[ran]
            except KeyError:
                pass
    return invAli, invEne
from modulo.crearMazos import crearMazo
import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
mazoAli=crearMazo('random', archivoa)
mazoEnemigo=crearMazo('attack', archivoa)
atp=random.randint(1,2)
jugadores={'local':{'vida':10, 'pinv':5,}, 'enemigo':{'vida':10,'pinv':5}}
def fasepegar(atp):
        a, y=faseinv(mazoAli, mazoEnemigo)
        print(a)
        print(y)
        if atp==1:
            try:
                for i in range (0,len(a)):
                    if a[i]['attack']-y[i]['defense']>=0:
                        if a[i]['type']=='infantry' and y[i]['type']=='lancer':
                            jugadores['enemigo']['vida']-=2 * a[i]['attack'] - y[i]['defense']
                        elif a[i]['type']=='lancer' and y[i]['type']=='chivalry':
                            jugadores['enemigo']['vida'] -= 2 * a[i]['attack'] - y[i]['defense']
                        elif a[i]['type'] == 'chivalry' and y[i]['type'] == 'infantry':
                            jugadores['enemigo']['vida'] -= 2 * a[i]['attack'] - y[i]['defense']
                        else:
                            jugadores['enemigo']['vida'] -= a[i]['attack'] - y[i]['defense']
                print('enemigo',jugadores['enemigo']['vida'])
                atp=2
            except IndexError:
                    for x in range(i,len(a)):
                        if a[x]['type']=='infantry' and y[x]['type']=='lancer ':
                            jugadores['enemigo']['vida']-=2 * a[x]['attack'] - y[x]['defense']
                        elif a[x]['type']=='lancer' and y[x]['type']=='chivalry':
                            jugadores['enemigo']['vida'] -= 2 * a[x]['attack'] - y[x]['defense']
                        elif a[x]['type'] == 'chivalry' and y[x]['type'] == 'infantry':
                            jugadores['enemigo']['vida'] -= 2 * a[x]['attack'] - y[x]['defense']
                        else:
                            jugadores['enemigo']['vida'] -= a[i]['attack'] - y[i]['defense']
                    print('enemigo', jugadores['enemigo']['vida'])
                    atp=2
        if atp==2:
            try:
                for i in range (0,len(y)):
                    if y[i]['attack']-a[i]['defense']>=0:
                        if y[i]['type'] == 'infantry' and a[i]['type'] == 'lancer ':
                            jugadores['enemigo']['vida'] -= 2 * y[i]['attack'] - a[i]['defense']
                        elif y[i]['type'] == 'lancer' and a[i]['type'] == 'chivalry':
                            jugadores['enemigo']['vida'] -= 2 * y[i]['attack'] - a[i]['defense']
                        elif y[i]['type'] == 'chivalry' and a[i]['type'] == 'infantry':
                            jugadores['enemigo']['vida'] -= 2 * y[i]['attack'] - a[i]['defense']
                        else:
                            jugadores['enemigo']['vida'] -= y[i]['attack'] - a[i]['defense']
                print('aliado',jugadores['local']['vida'])
                atp=1
            except IndexError:
                for x in range(i,len(y)):
                    if y[x]['type'] == 'infantry' and a[x]['type'] == 'lancer ':
                        jugadores['enemigo']['vida'] -= 2 * y[x]['attack'] - a[x]['defense']
                    elif y[x]['type'] == 'lancer' and a[i]['type'] == 'chivalry':
                        jugadores['enemigo']['vida'] -= 2 * y[x]['attack'] - a[x]['defense']
                    elif y[x]['type'] == 'chivalry' and a[x]['type'] == 'infantry':
                        jugadores['enemigo']['vida'] -= 2 * y[x]['attack'] - a[x]['defense']
                    else:
                        jugadores['enemigo']['vida'] -= y[x]['attack'] - a[x]['defense']
                print('aliado',jugadores['local']['vida'])
                atp=1
fasepegar(atp)