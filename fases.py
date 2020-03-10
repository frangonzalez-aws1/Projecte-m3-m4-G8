import random
def faseinv(dic, dic2):
    jugadores={'local':{'vida':10, 'pinv':5,}, 'enemigo':{'vida':10,'pinv':5}}
    invAli=[]
    invEne=[]
    lista=[]
    atp=random.randint(1,2)
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
    print(invAli)
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
    print(invEne)
from modulo.crearMazos import crearMazo
import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
mazoAli=crearMazo('random', archivoa)
mazoEnemigo=crearMazo('attack', archivoa)
faseinv(mazoAli, mazoEnemigo)
fasedes=0
faseconf=0
