# coding: UTF-8
# INTEIROS POSITIVOS DIVISIVEIS - TST - LUCAS GABRIEL

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())

for n in range(1, k+1):
	if n % a == 0 and n % b == 0:
		print n
