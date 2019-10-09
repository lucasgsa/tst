# coding: UTF-8
# INICIO CONSOANTES - LUCAS GABRIEL - TST

total = int(raw_input())
vogais = ["a","e","i","o","u"]
consoantes = 0

for p in range(total):
	palavra = raw_input()
	palavra = palavra.lower()
	if palavra[0] not in vogais:
		consoantes += 1
print "total de palavras:",total
print "iniciadas por consoantes: %i (%.2f%%)" %(consoantes, float(consoantes*100)/total)
