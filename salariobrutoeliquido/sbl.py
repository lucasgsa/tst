# coding: UTF-8

nome = raw_input()
horas_extras = float(raw_input())
salario_minimo = float(raw_input())
preco_hora_extra = float(raw_input())

bruto = 4*salario_minimo + horas_extras*preco_hora_extra

liquido = bruto - (bruto*0.2) - (bruto*0.12)

print "O Salário Bruto de %s é de R$ %.2f" %(nome, bruto)
print "O Salário Líquido de %s é de R$ %.2f" %(nome, liquido)
