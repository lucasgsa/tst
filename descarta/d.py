# coding: UTF-8
# TST - DESCARTA COINCIDENTES - LUCAS GABRIEL

descartados = []
num_descartados = 0
aceitos = []
num_aceitos = 0
numeros = int(raw_input())

for interacoes in range(numeros):
	num = raw_input()
	aceito = True
	for i in range(len(num)):
		if i == int(num[i]):
			aceito = False
	if aceito:
		aceitos.append(num)
		num_aceitos += 1
	else:
		descartados.append(num)
		num_descartados += 1
print "---"
print num_aceitos,"aceito(s)"
for n_aceito in aceitos:
	print n_aceito
print num_descartados,"descartado(s)"
for n_descartado in descartados:
	print n_descartado
