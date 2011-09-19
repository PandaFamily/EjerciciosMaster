#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys

Profundidad = 3
Enlace = 'http://meneame.net'

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
        MuestraEnlaces(EnlaceTemporal, Profundidad - 1)
MuestraEnlaces(Enlace, Profundidad)
