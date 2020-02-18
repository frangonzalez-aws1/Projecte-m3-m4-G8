def leerXML(xml):
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml)
    root = tree.getroot()
    xmlDic = {}
    for c in root.findall('carta/*'):
        xmlDic

leerXML('../carta.xml')