def agrupa_multiplos(sequencia, divisor):
	aux = []
	aux2 = []
	for i in range(len(sequencia)-1,-1,-1):
		if sequencia[i] % divisor != 0:
			aux.append(sequencia.pop(i))
	for i in range(len(aux)-1,-1,-1):
		aux2.append(aux[i])
	sequencia += aux2
