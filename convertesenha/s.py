senha = raw_input()
senha1 = ""
senha_nova = senha[0]
for i in range(1,len(senha)):
	senha1 += senha[i]
trocas = 0
for l in senha1:
	if l == "A" or l == "a":
		senha_nova += "4"
		trocas += 1
	elif l == "E" or l == "e":
		senha_nova += "3"
		trocas += 1
	elif l == "I" or l == "i":
		senha_nova += "1"
		trocas += 1
	elif l == "O" or l == "o":
		senha_nova += "0"
		trocas += 1
	else:
		senha_nova += l
print senha_nova, "(%i troca(s))" %trocas
