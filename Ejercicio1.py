# Primer Ejercicio.
FicheroPasswd = open("/etc/passwd")
for line in FicheroPasswd.readlines():
	Usuario = line.split(':')
	print Usuario[0] + " -> " + Usuario[6].rstrip('\n')

