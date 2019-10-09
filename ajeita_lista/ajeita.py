def ajeita_lista(lista):
	pares = 0
	for i in range(len(lista)):
		if lista[i]%2==0:
			j = i
			pares += 1
			while j > 0 and (lista[j] > lista[j-1] or lista[j-1]%2 != 0):
				lista[j],lista[j-1] = lista[j-1],lista[j]
				j -= 1
	for i in range(pares, len(lista)):
		j = i
		while j > pares and (lista[j] < lista[j-1]):
			lista[j],lista[j-1] = lista[j-1],lista[j]
			j-= 1
