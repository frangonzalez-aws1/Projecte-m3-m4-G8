def crearMazo(tipo, archivo):
    import random
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
                    dic[card[0]][child2.tag] = child2.text

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
                    dic[card[0]][child2.tag] = child2.text

    # RANDOM
    elif tipo is types[2]:
        cnt3 = 0
        cnt = 1
        while cnt3 < 11:
            # ERROR: Si en la carta pongo más de 20 cartas solo me contara las 20 y no todas las que ponga.
            ran = str(random.randint(1, len(archivo.findall('deck/card')) + 1))
            for child in archivo.findall('deck/card[' + ran + ']'):
                trobat = 0
                d = {}
                for child2 in child:
                    for i in dic.values():
                        if child2.text == i['name']:
                            trobat = 1
                            break
                    d[child2.tag] = child2.text
                if trobat == 0:
                    dic[cnt] = d
                    cnt += 1

            cnt3 += 1

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
        balanced.sort(key=lambda defend: defend[:][1], reverse=False)
        del balanced[10:]

        # Creamos las llaves necesarias en la variable principal para empezar a rellenarlas con el siguiente for que
        # tenemos.
        for i in balanced:
            dic[i[0]] = {}

        for card in balanced:
            # Escogemos las cartas en el findall.
            for child in archivo.findall('deck/card[' + str(card[0]) + ']'):
                #    Ahora escogemos todos los hijos de la carta y las anadimos en el diccionario.
                for child2 in child:
                    dic[card[0]][child2.tag] = child2.text

    return dic