# coding: UTF-8

palavra = raw_input()
inversa = ""
quantas = 0

for i in palavra:
	inversa = i+inversa

for i_letra in range(len(palavra)):
	if palavra[i_letra] == inversa[i_letra]:
		quantas += 1

print "A palavra %s contém %i caractere(s) coincidente(s) com a sua inversa." %(palavra, quantas)
