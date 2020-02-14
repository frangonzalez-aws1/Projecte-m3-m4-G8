import random
c = open('carta.xml', 'w+')

nombres = ['Pargilana','Coloclan','Canirme','Curgo','Calión','Bele','Histis','Marmenta','Conen','Voldole','Mille','Perofora','Estabie','Numba','Desego','Descierta','Elerochan','Recone','Esmador']
tipos = ['Infantería', 'Caballería', 'Lanceros']
descripciones = ['¡Por la marea!', 'En su corazón, esta el amor.', '¡Por los dioses que me dieron este poder!', 'Nadie es mejor que yo...', 'Indeseable bestia...', '¡Fuera de mi camino!', '¡Por el poder del agua!']

c.writelines('<cartas>\n')
for a in range(0, 19):
    descripcion = descripciones[random.randint(0, len(descripciones)-1)]
    tipo = tipos[random.randint(0, len(tipos) - 1)]
    ataque = random.randint(0,5)
    defensa = random.randint(0,5)
    invocacion = ataque + defensa
    if invocacion > 5:
        invocacion = 5
    c.write('\t<carta>\n'
            '\t\t<nombre>{}</nombre>\n'
            '\t\t<descripcion>{}</descripcion>\n'
            '\t\t<pts_invocacion>{}</pts_invocacion>\n'
            '\t\t<ataque>{}</ataque>\n'
            '\t\t<defensa>{}</defensa>\n'
            '\t\t<tipo>{}</tipo>\n'
            '\t</carta>\n'.format(nombres[a], descripcion, invocacion, ataque, defensa, tipo))
c.writelines('</cartas>\n')