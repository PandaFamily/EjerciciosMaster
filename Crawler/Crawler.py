#!/usr/bin/env python
#    Copyright (C) 2011 Imanol Lazkano Ruiz a/k/a Norwegian

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

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

def CompruebaEnlace(CadenaEnlace):
    Resultado = CadenaEnlace.find('http:')
    return Resultado

# Esta es la funcion recursiva para ir descargando URLs
def MuestraEnlaces(EnlaceT, ProfundidadT):
    # Condicion de Salida para el fin del bucle recursivo.
    if ProfundidadT == -1: return 0
    print 'Profundidad: ', ProfundidadT, 'Enlace: ', EnlaceT

    # Abrimos el Enlace, descargamos la URL y la parseamos
    WebDownloader = urllib2.build_opener()
    print 'ANTES DE LA APERTURA DE ', EnlaceT
    CodigoHTML = WebDownloader.open(EnlaceT)
    CodigoSOUP = BS(CodigoHTML)
    print 'DESPUES DE LA APERTURA DE ', EnlaceT

    # Iteracion para sacar los enlaces
    Enlaces = [link['href'] for link
                        in CodigoSOUP.findAll('a')
                        if link.has_key('href')]

    # Iteracion recursiva que comprueba cada enlace
    for EnlaceTemporal in Enlaces:
        ResultadoTemporal = CompruebaEnlace(EnlaceTemporal)

        # Si la funcion para comprobar los enlaces no devuelve 0, el enlace hay que descartarlo.
        if ResultadoTemporal != 0:
            print 'Enlace Incorrecto: ', EnlaceTemporal
            continue
        else:
            print EnlaceTemporal
            MuestraEnlaces(EnlaceTemporal, Profundidad - 1)

# Comenzamos el bucle principal
Resultado = CompruebaEnlace(Enlace)
if Resultado != 0:
    print 'Enlace de entrada incorrecto: ', Enlace
    sys.exit(-1)

# Deberia ir bien ya
MuestraEnlaces(Enlace, Profundidad)
