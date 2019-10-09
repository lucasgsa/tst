# coding: UTF-8
# Custo INSS - TST - LUCAS GABRIEL


base = float(raw_input())

if base <= 1317.07:
	custo_empregado = base*0.08
elif base <= 2195.12:
	custo_empregado = base*0.09
else:
	custo_empregado = base*0.11
	
custo_empregador = base*0.12

print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" %custo_empregador
print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" %custo_empregado
