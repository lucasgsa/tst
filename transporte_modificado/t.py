# coding: UTF-8
# TRANSPORTE MODIFICADO - TST - LUCAS GABRIEL
import math

pessoas  = int(raw_input())
dinheiro = float(raw_input())

para_tav = pessoas*100.0
para_taxi = (math.ceil((pessoas/4.0)))*200
para_onibus = pessoas*22

if dinheiro >= para_tav:
	print "TAV. R$ %.2F" %para_tav
elif dinheiro >= para_taxi:
	print "Táxi. R$ %.2f" %para_taxi
elif dinheiro >= para_onibus:
	print "Ônibus. R$ %.2f" %para_onibus
else:
	print "Não é possível realizar a viagem."
