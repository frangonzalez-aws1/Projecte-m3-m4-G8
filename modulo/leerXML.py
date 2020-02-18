def leerXML(xml):
    import xml.etree.ElementTree as ET

    estructura_xml = ET.parse(xml)

    # Obtiene el elemento raíz:
    raiz = estructura_xml.getroot()

    for elemento_hijo in raiz:
        print(elemento_hijo)

leerXML('../carta.xml')
