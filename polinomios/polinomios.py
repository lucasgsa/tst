def calcula(lista,x):
	inicial = 0
	soma = 0
	for e in lista:
		soma += e*(x)**inicial
		inicial += 1
	return soma

poli = []
while True:
	entrada = raw_input().split()
	if entrada[0] == "p:":
		poli = []
		print "novo polinomio"
		for i in range(1,len(entrada)):
			poli.append(int(entrada[i]))
	elif entrada[0] == "fim":
		break
	else:
		print calcula(poli,int(entrada[0]))
