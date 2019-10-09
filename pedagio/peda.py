# coding: UTF-8
# PEDÁGIO - TST - LUCAS GABRIEL

tipo = raw_input()
if tipo == "Automóvel utilitário":
	print "Valor a pagar: R$ 11.40."
elif tipo == "Ônibus":
	eixos = int(raw_input())
	print "Valor a pagar: R$ %.2f." %(eixos*11.40)
elif tipo == "Caminhão":
	eixos = int(raw_input())
	print "Valor a pagar: R$ %.2f." %(eixos*9.60)
elif tipo == "Motocicleta":
	print "Valor a pagar: R$ 5.70."
else:
	print "Veículo não cadastrado."
