# Novo CPF - TST - Lucas Gabriel

parte1 = raw_input()
parte2 = raw_input()
parte3 = raw_input()
cpf = parte1+"."+parte2+"."+parte3+"-"

soma_parte3 = 0
for n in parte3:
	soma_parte3 += int(n)
if soma_parte3 >= 10:
	cpf = cpf+str(soma_parte3)
else:
	cpf = cpf+"0"+str(soma_parte3)
print cpf
