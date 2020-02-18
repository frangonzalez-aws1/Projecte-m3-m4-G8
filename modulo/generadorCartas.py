def generadorCartas():
    import random
    c = open('../carta.xml', 'w+')

    # Asignamos los nombres a las cartas
    nombres = ['Pargilana','Coloclan','Canirme','Curgo','Calión','Bele','Histis','Marmenta','Conen','Voldole','Mille','Perofora','Estabie','Numba','Desego','Descierta','Elerochan','Recone','Esmador','Hembad','Almen']
    # Asignamos los tipos de cada carta
    tipos = ['Infantería', 'Caballería', 'Lanceros']
    # Creamos las distintas descripciones. Después, cada asignación será aleatoria.
    descripciones = ['¡Por la marea!', 'En su corazón, esta el amor.', '¡Por los dioses que me dieron este poder!', 'Nadie es mejor que yo...', 'Indeseable bestia...', '¡Fuera de mi camino!', '¡Por el poder del agua!']

    c.writelines('<playerConfig>\n'
                 '\t<playerLife>10</playerLife>\n'
                 '\t<summonPointsPlayer>5</summonPointsPlayer>\n'
                 '\t<deck>0</deck>\n'
                 '</playerConfig>\n\n'
                 '<cards>\n')
    for a in range(1, 21):
        # El número de la lista saldrá aleatoriamente asi asignado el valor de ese número a la descripción y al tipo.
        descripcion = descripciones[random.randint(0, len(descripciones)-1)]
        tipo = tipos[random.randint(0, len(tipos) - 1)]
        # Asignamos aleatoriamente los ataques y defensas.
        ataque = random.randint(0,5)
        defensa = random.randint(0,5)
        # Sumamos los ataques y defensas para la invocación. Si es mayor a 5, se mantendrá como 5.
        invocacion = ataque + defensa
        if invocacion > 5:
            invocacion = 5
        c.write('\t<card summonPoints="{}" type="{}">\n'
                '\t\t<name>{}</name>\n'
                '\t\t<description>{}</description>\n'
                '\t\t<attack>{}</attack>\n'
                '\t\t<defense>{}</defense>\n'
                '\t</card>\n'.format(invocacion, tipo, nombres[a], descripcion, ataque, defensa))
    c.writelines('</cards>\n')

generadorCartas()