# coding: UTF-8
# MAIOR CORRENTE - TST - LUCAS GABRIEL

tensao1 = float(raw_input())
resistencia1 = float(raw_input())
corrente1 = tensao1/resistencia1

tensao2 = float(raw_input())
resistencia2 = float(raw_input())
corrente2 = tensao2/resistencia2

tensao3 = float(raw_input())
resistencia3 = float(raw_input())
corrente3 = tensao3/resistencia3


maior = 1
maior_corrente = corrente1

if corrente2 > corrente1 and corrente2 > corrente3:
	maior_corrente = corrente2
	maior = 2

if corrente3 > maior_corrente:
	maior_corrente = corrente3
	maior = 3
	
print "condutor com maior corrente:",maior
if maior_corrente < 0.001:
	print "maior corrente: %.2f µA" %(maior_corrente*1000000)
elif maior_corrente < 1:
	print "maior corrente: %.2f mA" %(maior_corrente*1000)
elif maior_corrente >= 1:
	print "maior corrente: %.2f A" %(maior_corrente)

