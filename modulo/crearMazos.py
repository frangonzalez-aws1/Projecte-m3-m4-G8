def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'

    # Creamos el diccionario y continuamente, lo que haremos es darle el total de cartas que hay en el XML en el
    # diccionario.
    dic = {}

    # ATAQUE
    if tipo is types[0]:
        # Creamos las variables attack y card. <Attack> obtendra el numero de carta y su ataque, y se almacenara alli.
        attack = []
        card = 1
        for i in archivo.findall('deck/card//attack'):
            attack.append([card, i.text])
            card += 1

        # Ordenamos las cartas escogiendo los valores de ataque y despues eliminaremos las que no sean las 10
        # primeras. Lo que haremos con esto es obtener el top 10 de las cartas que tienen mas ataque.
        attack.sort(key=lambda attack: attack[:][1], reverse=True)
        del attack[10:]

        # Creamos las llaves necesarias en la variable principal para empezar a rellenarlas con el siguiente for que
        # tenemos.
        for i in attack:
            dic[i[0]] = {}

        for card in attack:
            # Escogemos las cartas en el findall.
            for child in archivo.findall('deck/card[' + str(card[0]) + ']'):
                # Ahora escogemos todos los hijos de la carta y las anadimos en el diccionario.
                for child2 in child:
                    if child2.tag == 'attack':
                        dic[card[0]][child2.tag] = int(child2.text)
                    elif child2.tag == 'defense':
                        dic[card[0]][child2.tag] = int(child2.text)
                    else:
                        dic[card[0]][child2.tag] = child2.text

                # Insertamos los atributos utilizando <>.attrib
                listAttrib = child.attrib
                dic[card[0]]['summonPoints'] = int(listAttrib['summonPoints'])
                dic[card[0]]['type'] = listAttrib['type']

    # DEFENSA
    elif tipo is types[1]:
        # Creamos las variables defend y card. <Defend> obtendra el numero de carta y su defensa, y se almacenara alli.
        defend = []
        card = 1
        for i in archivo.findall('deck/card//defense'):
            defend.append([card, i.text])
            card += 1

        # Ordenamos las cartas escogiendo los valores de defensa y despues eliminaremos las que no sean las 10
        # primeras. Lo que haremos con esto es obtener el top 10 de las cartas que tienen mas defensa.
        defend.sort(key=lambda defend: defend[:][1], reverse=True)
        del defend[10:]

        # Creamos las llaves necesarias en la variable principal para empezar a rellenarlas con el siguiente for que
        # tenemos.
        for i in defend:
            dic[i[0]] = {}

        for card in defend:
            # Escogemos las cartas en el findall.
            for child in archivo.findall('deck/card[' + str(card[0]) + ']'):
                # Ahora escogemos todos los hijos de la carta y las anadimos en el diccionario.
                for child2 in child:
                    if child2.tag == 'attack':
                        dic[card[0]][child2.tag] = int(child2.text)
                    elif child2.tag == 'defense':
                        dic[card[0]][child2.tag] = int(child2.text)
                    else:
                        dic[card[0]][child2.tag] = child2.text

                # Insertamos los atributos utilizando <>.attrib
                listAttrib = child.attrib
                dic[card[0]]['summonPoints'] = int(listAttrib['summonPoints'])
                dic[card[0]]['type'] = listAttrib['type']

    # RANDOM
    elif tipo is types[2]:
        import random
        # Creamos las variables randomL y card. <RandomL> obtendra el numero de carta, y se almacenara alli.
        randomL = []
        i = 1
        while i < 11:
            x = random.randint(1, len(archivo.findall('deck/card')))
            if x not in randomL:
                randomL.append(x)
                i += 1

        # Creamos las llaves necesarias en la variable principal para empezar a rellenarlas con el siguiente for que
        # tenemos.
        for i in randomL:
            dic[i] = {}

        for card in randomL:
            # Escogemos las cartas en el findall.
            for child in archivo.findall('deck/card[' + str(card) + ']'):
                # Ahora escogemos todos los hijos de la carta y las anadimos en el diccionario.
                for child2 in child:
                    if child2.tag == 'attack':
                        dic[card][child2.tag] = int(child2.text)
                    elif child2.tag == 'defense':
                        dic[card][child2.tag] = int(child2.text)
                    else:
                        dic[card][child2.tag] = child2.text

                # Insertamos los atributos utilizando <>.attrib
                listAttrib = child.attrib
                dic[card]['summonPoints'] = int(listAttrib['summonPoints'])
                dic[card]['type'] = listAttrib['type']

    # BALANCED
    elif tipo is types[3]:
        # Creamos las variables balanced y card. <Balanced> obtendra el numero de carta y su balanced, y se almacenara alli.
        balanced = []
        card = 1
        attacked = ''
        defensed = ''
        for i in archivo.findall('deck/card//'):
            if i.tag == 'attack':
                attacked = int(i.text)
            elif i.tag == 'defense':
                defensed = int(i.text)
            elif attacked != '' and defensed != '':
                # Evitamos que salga negativo los valores
                if attacked - defensed <= -1:
                    balanced.append([card, defensed - attacked])
                else:
                    balanced.append([card, attacked - defensed])
                attacked = ''
                defensed = ''
                card += 1

        # Ordenamos las cartas escogiendo los valores de balanced y despues eliminaremos las que no sean las 10
        # primeras. Lo que haremos con esto es obtener el top 10 de las cartas que tienen menos balanced.
        balanced.sort(key=lambda balanced: balanced[:][1], reverse=False)
        del balanced[10:]

        # Creamos las llaves necesarias en la variable principal para empezar a rellenarlas con el siguiente for que
        # tenemos.
        for i in balanced:
            dic[i[0]] = {}

        for card in balanced:
            # Escogemos las cartas en el findall.
            for child in archivo.findall('deck/card[' + str(card[0]) + ']'):
                # Ahora escogemos todos los hijos de la carta y las anadimos en el diccionario.
                for child2 in child:
                    if child2.tag == 'attack':
                        dic[card[0]][child2.tag] = int(child2.text)
                    elif child2.tag == 'defense':
                        dic[card[0]][child2.tag] = int(child2.text)
                    else:
                        dic[card[0]][child2.tag] = child2.text

                # Insertamos los atributos utilizando <>.attrib
                listAttrib = child.attrib
                dic[card[0]]['summonPoints'] = int(listAttrib['summonPoints'])
                dic[card[0]]['type'] = listAttrib['type']

    return dic