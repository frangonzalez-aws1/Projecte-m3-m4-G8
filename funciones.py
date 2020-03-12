import xml.etree.ElementTree as ET
def cargarcartas(alioene):
    if alioene == "aliado":
        try:
            archivoa = ET.parse("myBaraja.xml")
            print("Se ha cargado correctamente el archivo aliado")
            return archivoa
        except FileNotFoundError:
            print("No se ha podido leer el fichero")
            return False
    else:
        try:
            archivoe = ET.parse("Enemigo.xml")
            print("Se ha cargado correctamente el archivo enemigo")
            return archivoe
        except FileNotFoundError:
            print("No se ha podido leer el fichero")
            return False