def leerXML():
    import xml.etree.ElementTree as ET
    tree = ET.parse('../carta.xml')
    root = tree.getroot()
    for a in root.findall('carta/*'):
        print(a.attrib)

leerXML()