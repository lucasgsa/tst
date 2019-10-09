def soma(lista):
	soma = 0
	for e in lista:
		soma += e
	return soma

def divisores(numero):
	div = []
	for e in range(1, numero+1):
		if numero%e == 0:
			div.append(e)
	return soma(div)

numeros = []
while True:
	entrada = input()
	if entrada == -1: break
	elif entrada < 0: continue
	else:
		numeros.append(entrada)

print "Somas:"
for e in numeros:
	print divisores(e)
