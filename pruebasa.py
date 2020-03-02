def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'
    cont=0
    c=10
    dic={1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}, 10:{}}
    if tipo is 'attack':
       for child in archivo.findall('deck/'):
            print(child.tag, child.value)
    elif tipo is 'defend':
        for child in archivo.findall('deck/card/'):
            for child2 in archivo.findall('deck/card/'+child):
                if int(child2.text) == 5:
                    dic[cont]=('deck/card/'+child)
            cont+=1
        print(dic)
    elif tipo is 'random':
        print('Random:', archivo)
    elif tipo is 'balanced':
        print('Balanced:', archivo)

import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
crearMazo('defend', archivoa)