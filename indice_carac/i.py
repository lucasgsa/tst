# coding: UTF-8
# TST - INDICES DE CARACTERES - LUCAS GABRIEL

def quantos(f,letra):
	posicoes = []
	string = ""
	for i in range(len(f)):
		if f[i] == letra:
			posicoes.append(i)
	if len(posicoes) == 0:
		return "-1"
	
	for i in range(len(posicoes)):
		if i == len(posicoes)-1:
			string += str(posicoes[i])
		else:
			string += str(posicoes[i])+" "
	return string
	



frase = raw_input()
palavra = raw_input()
for i in palavra:
	print quantos(frase,i)
