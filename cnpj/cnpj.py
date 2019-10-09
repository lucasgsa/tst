cnpj_incompleto = raw_input()
numeros = ["0","1","2","3","4","5","6","7","8","9"]
soma = 0
for c in cnpj_incompleto:
	if c in numeros:
		soma += int(c)
soma += 1
cnpj_incompleto = cnpj_incompleto+"/0001-"

numero = 0
for c in str(soma):
	numero += 1
if numero == 1:
	print cnpj_incompleto+"0%i" %soma
else:
	print cnpj_incompleto+"%i" %soma
