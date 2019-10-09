def busca(lista, elemento):
	pos = -1
	for e in range(len(lista)):
		if lista[e] == elemento:
			pos = e
			break
	return pos

seq = []
print busca(seq,9)
