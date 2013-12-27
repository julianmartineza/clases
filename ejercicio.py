MiLista = ["juan", "eljach", 15, 1.75]
MiLista[0] = "pedro"
MiLista[1] = "perez"
MiLista[2] = 24
MiLista[3] = 1.68

print "Mis datos son: "

for x in MiLista:
	print x

edad = MiLista[2]
if edad > 18:
	print "Soy mayor de edad"
else:
	print "Soy menor de edad"
