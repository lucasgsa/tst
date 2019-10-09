# coding: UTF-8
# DESVIO PADRAO - TST - LUCAS GABRIEL

def desvio_padrao(sequencia,quantos):
	soma = 0
	for i in sequencia:
		soma += i
	media = soma/quantos
	passo1 = 0
	for i in sequencia:
		passo1 += (i-media)**2
	passo2 = passo1/(quantos-1)
	passo3 = passo2**0.5
	return passo3

sequencia1 = raw_input().split()
quantos1 = 0
sequencia2 = raw_input().split()
quantos2 = 0
for i in range(len(sequencia1)):
	sequencia1[i] = float(sequencia1[i])
	quantos1 += 1
for i in range(len(sequencia2)):
	sequencia2[i] = float(sequencia2[i])
	quantos2 += 1
	
des1 = desvio_padrao(sequencia1,quantos1)
des2 = desvio_padrao(sequencia2,quantos2)

if des1 > des2:
	print "A sequência 1 possui o maior desvio padrão (%.2f)." %(des1)
elif des1 < des2:
	print "A sequência 2 possui o maior desvio padrão (%.2f)." %(des2)
else:
	print "As sequências possuem o mesmo desvio padrão (%.2f)." %(des1)
