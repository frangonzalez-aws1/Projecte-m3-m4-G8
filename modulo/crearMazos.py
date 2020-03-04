def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'
    dic = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}}

    cnt = 1
    for child in archivo.findall('deck/card/'):
        if cnt == 11:
            break
        if child.tag == 'name':
            dic[cnt]['name'] = child.text

        elif child.tag == 'description':
            dic[cnt]['description'] = child.text

        elif child.tag == 'attack':
            dic[cnt]['attack'] = child.text

        elif child.tag == 'defense':
            dic[cnt]['defense'] = child.text
            cnt += 1

    cnt2 = 1
    for child in archivo.findall('deck/card'):
        if cnt2 == 11:
            break
        dic[cnt2]['summonPoints'] = child.attrib['summonPoints']
        dic[cnt2]['type'] = child.attrib['type']
        cnt2 += 1

    if tipo is 'attack':
       print(dic)
    elif tipo is 'defend':
        print(dic)
    elif tipo is 'random':
        print('Random:', archivo)
    elif tipo is 'balanced':
        print('Balanced:', archivo)

import xml.etree.ElementTree as ET
archivoa = ET.parse('../myBaraja.xml')
archivoa = archivoa.getroot()

crearMazo('attack', archivoa)