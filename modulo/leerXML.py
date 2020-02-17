def leerXML(xml):
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml)
    root = tree.getroot()
    change = 1
    for c in root.findall('carta/*'):
        if change
        print(c.text)

leerXML('../carta.xml')