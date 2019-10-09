# coding: UTF-8
# DV DE CONTA - TST - LUCAS GABRIEL

conta = raw_input()
soma = 0
for n in conta:
	soma += int(n)
digito = soma%11
if digito == 10:
	digito = "X"
print "%s-%s" %(conta, str(digito))
