palavras = [raw_input(),raw_input(),raw_input()]
palavra_final = ""


for l in range(len(palavras[0])):
	a = palavras[0][l]
	b = palavras[1][l]
	c = palavras[2][l]
	if (a >= b and a >= c):
		palavra_final += a
	elif (b >= a and b >= c):
		palavra_final += b
	else:
		palavra_final += c
print palavra_final
