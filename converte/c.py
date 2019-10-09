matricula_antiga = raw_input()
matricula_nova = "1"
for n in range(1,len(matricula_antiga)):
	if n == 5:
		matricula_nova += "0"
	matricula_nova += matricula_antiga[n]
print matricula_nova
