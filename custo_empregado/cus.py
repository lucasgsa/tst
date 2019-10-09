# coding: UTF-8

base = float(raw_input())
dias = float(raw_input())
custo_transporte = float(raw_input())*dias

if base <= 1317.07:
	custo_empregado = base*0.08
elif base <= 2195.12:
	custo_empregado = base*0.09
else:
	custo_empregado = base*0.11
	
custo_empregador = base*1.2

porc_transporte = base*0.06

if custo_transporte > porc_transporte:
	custo_empregado += base*0.06
	custo_empregador += (porc_transporte-custo_transporte)*-1

print "O salário base é R$ %.2f" %base
print "O custo mensal para o empregador é de R$ %.2f" %custo_empregador
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" %(base-custo_empregado)
