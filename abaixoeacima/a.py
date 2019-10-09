def organiza_por_media(lista):
	maiores = []
	maiores_i = []
	media = 0.0
	
	if len(lista) == 0:
		return []
	for i in lista:
		media += i
		
	media = media/len(lista)
		
	for i in range(len(lista)-1,-1,-1):
		if lista[i] > media:
			maiores.append(lista.pop(i))
	for i in range(len(maiores)-1,-1,-1):
		maiores_i.append(maiores[i])
	lista += maiores_i
	return lista
