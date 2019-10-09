#coding: utf-8
def meu_in(valor, lista):
	condicao = False
	for i in range(len(lista)):
		if lista[i] == valor:
			return True
		else:
			condicao = False
			
	return condicao
	
def tem_afinidade(l1, l2):
	afinidade = []
	for artista in l1:
		afinidade.append(artista)
	
	c = 0	
	for artista in l2:
		verifica = meu_in(artista, afinidade)
		if verifica == True:
			c += 1
		
	if c >= 3:
		return True
	else:
		return False
		
l1 = ['zezo', 'u2', 'jquest']
l2 = ['zezo', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
