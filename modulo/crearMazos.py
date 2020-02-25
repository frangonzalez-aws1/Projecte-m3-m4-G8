def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'

    mazos = {}

    if tipo is 'attack':
        c = 0
        card = 1
        for child in archivo.findall('deck/card/'):
            mazos[card] = 'p'
            print(child.tag, child.text)
            if c == 3:
                print('---')
                c = 0
                card += 1
                if card == 11:
                    break
            else:
                c += 1
    elif tipo is 'defend':
        print('Defensa:', archivo)
    elif tipo is 'random':
        print('Random:', archivo)
    elif tipo is 'balanced':
        print('Balanced:', archivo)

    print(mazos)

import xml.etree.ElementTree as ET
archivoA = ET.parse('../myBaraja.xml')
archivoA = archivoA.getroot()
# Elegir tipo de mazo
crearMazo('attack', archivoA)