# coding: UTF-8


salario_bruto = float(raw_input())
horas_de_trabalho = float(raw_input())
ganhos_por_hora = salario_bruto / horas_de_trabalho


print "Salário Bruto =", salario_bruto
print "Hora Bruta =", ganhos_por_hora

ir = salario_bruto*0.11
print "Desconto IR =", ir

inss = salario_bruto*0.08
print "Desconto INSS =", inss


sindicato = salario_bruto*0.05
print "Desconto Sindicato =", sindicato

liquido = salario_bruto-ir-inss-sindicato
print "Salário Líquido =", liquido

hora_liquida = liquido/horas_de_trabalho
print "Hora Líquida =", hora_liquida
