def busca_matriz(matriz, elemento):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == elemento:
				return (i, j)
	return
