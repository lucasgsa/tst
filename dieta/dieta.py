# coding: UTF-8
#Dieta - TST - Lucas Gabriel

peso_a_perder = float(raw_input())
tempo_horas = float(raw_input())
calorias_por_dia = float(raw_input())

peso_a_perder = peso_a_perder*7700
exercicios = tempo_horas*900

diario = exercicios+2000-calorias_por_dia

dias = peso_a_perder/diario

print "Você precisará de %.2f dias de dieta" % dias
