def menor_da_lista(lista):
	menor = lista[0]
	for e in lista:
		if e < menor: menor = e
	return menor

def altura(matriz, posicoes):
	alturas = []
	alturas.append(posicoes[0]+1)
	alturas.append(posicoes[1]+1)
	alturas.append(matriz-posicoes[0])
	alturas.append(matriz-posicoes[1])
	return menor_da_lista(alturas)
	
def cria_matriz(ordem):
	matriz = []
	for i in range(ordem):
		n = []
		for j in range(ordem):
			n.append(0)
		matriz.append(n)
	return matriz

def meu_join(lista):
	texto = ""
	for i in range(len(lista)):
		texto += str(lista[i])
		if i != len(lista)-1:
			texto += " "
	return texto

entrada = int(raw_input())
matriz = cria_matriz(entrada)
for i in range(len(matriz)):
	for j in range(len(matriz)):
		matriz[i][j] = altura(entrada, [i,j])
	print meu_join(matriz[i])
