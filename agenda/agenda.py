# coding: UTF-8
# AGENDA - TST - LUCAS GABRIEL

def organizar(nomes,numeros):
	for i in range(len(nomes)):
		j = i
		while j > 0 and nomes[j] < nomes[j-1]:
			nomes[j],nomes[j-1] = nomes[j-1],nomes[j]
			numeros[j],numeros[j-1] = numeros[j-1],numeros[j]
			j -= 1
			
def nalista(lista,nome):
	nalista = False
	for e in lista:
		if e == nome:
			nalista = True
			break
	return nalista

nomes = []
numeros = []

while True:
	comando = raw_input()
	if comando == "finalizar":
		break
	elif comando == "inserir":
		vezes = int(raw_input())
		for n in range(vezes):
			nomes.append(raw_input())
			numeros.append(raw_input())
		organizar(nomes,numeros)
	elif comando == "buscar":
		n = raw_input()
		if nalista(nomes,n):
			for e in range(len(nomes)):
				if nomes[e] == n:
					print "Nome: %s" %nomes[e]
					print "Fone: %s" %numeros[e]
					print "----------"
		else:
			print "Nome inexistente" 
			print "----------"
	elif comando == "imprimir":
		for e in range(len(nomes)):
			print "Nome: %s" %nomes[e]
			print "Fone: %s" %numeros[e]
			print "----------"
