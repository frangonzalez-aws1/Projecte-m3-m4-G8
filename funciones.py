import xml.etree.ElementTree as ET
def cargarcartas(alioene):
    if alioene == "aliado":
        try:
            archivoa = ET.parse("myBaraja.xml")
            archivoa=archivoa.getroot()
            print("\nSe ha cargado correctamente el archivo aliado\n")
            return archivoa, True
        except FileNotFoundError:
            print("\nNo se ha podido leer el fichero\n")
            return False, False
    else:
        try:
            archivoe = ET.parse("Enemigo.xml")
            archivoe = archivoe.getroot()
            print("\nSe ha cargado correctamente el archivo enemigo\n")
            return archivoe, True
        except FileNotFoundError:
            print("\nNo se ha podido leer el fichero\n")
            return False, False