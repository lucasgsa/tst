# coding: UTF-8
# GREP - LUCAS GABRIEL - TST

palavra = raw_input()
vezes = input()

for i in range(vezes):
	frase = raw_input()
	for j in range(len(frase)-2):
		sub = frase[j]+frase[j+1]+frase[j+2]
		if sub == palavra:
			print frase
			break
		
