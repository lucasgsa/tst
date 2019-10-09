# coding: UTF-8
# CALCULADORA DE MEDIAS - TST - LUCAS GABRIEL

def media_aritmetica(lista):
	soma = 0.0
	for e in lista:
		soma += e
	print "Média Aritmética: %.4f" %(soma/len(lista))

def media_geometrica(lista):
	mult = 1
	for e in lista:
		mult = mult*e
	print "Média Geométrica: %.4f" %(mult**(1.0/len(lista)))
	
def media_harmonica(lista):
	soma = 0.0
	for e in lista:
		soma += 1.0/e
	print "Média Harmônica: %.4f" %(len(lista)/soma)
	
def paraFloat(lista):
	for e in range(len(lista)):
		lista[e] = float(lista[e])
		
while True:
	acabou = False
	entrada = raw_input().split()
	if entrada[0] == "Q":
		break
	lista = raw_input().split()
	paraFloat(lista)
	for comando in entrada:
		if comando == "MA":
			media_aritmetica(lista)
		if comando == "MG":
			media_geometrica(lista)
		if comando == "MH":
			media_harmonica(lista)
	print "----"
	if acabou:
		break
