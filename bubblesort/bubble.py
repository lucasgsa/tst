def bubblesort(lista):
	while True:
		swapped = False
		for i in range(0, len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i],lista[i+1]=lista[i+1],lista[i]
				swapped = True
		if not swapped: 
			break
