# coding: UTF-8
# LEI ESTADUAL - TST - LUCAS GABRIEL

idade = int(raw_input("Idade? "))
if idade < 12:
	print "criança (meia entrada)"
elif idade >= 65:
	print "idoso (meia entrada)"
else:
	estudante = raw_input("Estudante? ")
	if estudante == "s":
		publica = raw_input("Rede Pública? ")
		if publica == "s":
			print "estudante da rede pública (isento)"
		else:
			print "estudante (meia entrada)"
	else:
		print "adulto (inteira)"
