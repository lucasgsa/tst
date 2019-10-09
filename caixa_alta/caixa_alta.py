# coding: UTF-8

def paraMaiusculo(letra):
	k = ord(letra)
	if k < 97:
		return letra
	k -= 32
	return chr(k)
def paraMinusculo(letra):
	k = ord(letra)
	if k >= 97:
		return letra
	k += 32
	return chr(k)

def UmaLetra(frase,posicao):
	if (len(frase) == 1) or ((posicao == 0 or frase[posicao-1] == " ") and (posicao == len(frase)-1 or frase[posicao+1] == " ")):
		return True
	return False
	
def PrimeiraLetra(frase, posicao):
	if (posicao == 0 or frase[posicao-1] == " ") and (frase[posicao+1] != " "):
		return True
	return False

def caixa_alta(frase):
	nova = ""
	for posicao in range(len(frase)):
		letra = frase[posicao]
		
		if UmaLetra(frase, posicao):
			nova += paraMinusculo(letra)
		elif PrimeiraLetra(frase, posicao):
			nova += paraMaiusculo(letra)
		else:
			nova += letra
		
		
	return nova
