# coding: UTF-8
# LImpeza - TST - LUCAS GABRIEL

codigo = int(raw_input())
if codigo == 1:
	tanque = int(raw_input())
	preco = tanque*80
	print "R$ %i,00" %preco
	if preco >= 200:
		print "Brinde!"
		
elif codigo == 2:
	tanque = int(raw_input())
	preco = tanque*50
	print "R$ %i,00" %preco
	if preco >= 200:
		print "Brinde!"

elif codigo == 3:
	print "R$ 50,00"

