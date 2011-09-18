#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import argparse
import sys

# Analizamos los argumentos
Analizador = argparse.ArgumentParser(description="Naveguemos por Internet")
Analizador.add_argument('url', nargs=1, help='Punto de Entrada')
Analizador.add_argument('-p', '--profundidad', type=int, default=1, help='Profundidad del crawl')
Argumentos=Analizador.parse_args()

# Inicializamos los argumentos
Enlace = Argumentos.url.pop()
Profundidad = Argumentos.profundidad

# Esta es la funcion recursiva para ir descargando URLs
def MuestraEnlaces(EnlaceT, ProfundidadT):
    if ProfundidadT == 0: return 0
    print 'Profundidad: ', ProfundidadT, 'Enlace: ', EnlaceT
    WebDownloader = urllib2.build_opener()
    CodigoHTML = WebDownloader.open(EnlaceT)
    CodigoSOUP = BS(CodigoHTML)
    Enlaces = [link['href'] for link
                        in CodigoSOUP.findAll('a')
                        if link.has_key('href')]
    for EnlaceTemporal in Enlaces:
        print EnlaceTemporal
        MuestraEnlaces(EnlaceTemporal, Profundidad - 1)

# Llamamos a la funcion
MuestraEnlaces(Enlace, Profundidad)
