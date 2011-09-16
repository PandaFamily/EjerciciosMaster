#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys

Profundidad = 3
Enlace = 'http://meneame.net'

def MuestraEnlaces(Enlace, Profundidad):
    if Profundidad == 0: return 0
    WebDownloader = urllib2.build_opener()
    CodigoHTML = WebDownloader.open(Enlace)
    CodigoSOUP = BS(CodigoHTML)
    Enlaces = [link['href'] for link
                        in CodigoSOUP.findAll('a')
                        if link.has_key('href')]
    for EnlaceTemporal in Enlaces:
        print EnlaceTemporal
        MuestraEnlaces(EnlaceTemporal, Profundidad - 1)
