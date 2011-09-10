# Primer Ejercicio.
FicheroPasswd = open("/etc/passwd")
DiccionarioUsuarios = 0
for line in FicheroPasswd.readlines():
	Usuario = line.split(':')
	DiccionarioUsuarios[Usuario[0]]=Usuario[1]
	print DiccionarioUsuarios
