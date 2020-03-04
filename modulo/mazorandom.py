import random
def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'

    dic = {}

    if tipo is 'attack':
       print(dic)
    elif tipo is 'defend':
        print(dic)
    elif tipo is 'random':
        print('Random:', archivo)
        cnt3=0
        cnt=1
        while cnt3<10:
            ran = str(random.randint(1, 21))
            for child in archivo.findall('deck/card/['+ran+']'):
                trobat=0
                d = {}
                for child2 in child:
                    for i in dic.values():
                        if child2.text == i['name']:
                            trobat=1
                            break
                    d[child2.tag ] = child2.text
                if trobat == 0:
                    dic[cnt]=d
                    cnt += 1

            cnt3+=1
        print(dic)
    elif tipo is 'balanced':
        print('Balanced:', archivo)

import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()

crearMazo('random', archivoa)