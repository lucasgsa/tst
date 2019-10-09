#coding: utf-8
def meu_in(valor, lista):
	condicao = False
	for i in range(len(lista)):
		if valor == lista[i]:
			return True
		else:
			condicao = False
	
	return condicao
	
def acordes(musica_1, musica_2):
	acordes_aprendidos = []
	
	for i in range(len(musica_1)):
		acordes_aprendidos.append(musica_1[i])
		
	for i in range(len(musica_2)):
		condicao = meu_in(musica_2[i], acordes_aprendidos)
		if condicao == False:
			acordes_aprendidos.append(musica_2[i])
			
			
				
	return acordes_aprendidos
	
	
m1 = ['a','b','c']
m2 = []
assert acordes(m1, m2) == ['a','b','c']
assert m1 == ['a','b','c']
assert m2 == []

m1 = ['c', 'd']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'a']
