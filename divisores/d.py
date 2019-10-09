# coding: UTF-8
# DIVISORES - TST - LUCAS GABRIEL

numero = int(raw_input())

for teste in range(1,(numero/2)+1):
	if numero%teste == 0:
		print teste
