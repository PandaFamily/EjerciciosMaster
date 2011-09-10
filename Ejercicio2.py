# Segundo Ejercicio.
import sys

# Abrir el Fichero
FicheroPasswd = open("/etc/passwd")

# Inicializacion del Diccionario
DiccionarioUsuarios = {}

# Bucle de lectura de los usuarios
for line in FicheroPasswd.readlines():
	Usuario = line.split(':')
	DiccionarioUsuarios[Usuario[0]] = Usuario[5]

# Cierre del fichero
FicheroPasswd.close()

# Comprobamos si hay algun parametro pasado al script y se inicializa la variable Usuario
argv = sys.argv[1:]
if len(argv) < 1:
	print 'No se ha introducido usurio. Se pedira uno interactivamente.'
	Usuario = ''
else:
	print 'Usuario introducido en linea de comando: ' + sys.argv[1]
	Usuario = sys.argv[1]

# Vamos comprobando que el Usuario existe en la lista leida del fichero de passwd
while (not Usuario in DiccionarioUsuarios.keys()):
	if len(Usuario) > 0:
		print 'Usuario no encontrado en la lista local.'
	Usuario = raw_input('Introduce Usuario: ')

# Ya deberia haber un usuario valido en la varuable Usuario. Solo queda escribir su shell.
print 'Usuario local valido encontrado: ' + Usuario + '. Shell: ' + DiccionarioUsuarios[Usuario]

