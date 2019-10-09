# coding: UTF-8

print "Análise da Turma"
print "==="

aprovados = int(raw_input("Número de aprovados? "))
reprovados = int(raw_input("Número de reprovados? "))

total_turma = aprovados + reprovados
porc_aprovados = float(aprovados)*100/total_turma
porc_reprovados = float(reprovados)*100/total_turma

print "---"
print "Total de alunos na turma:",total_turma
print "Aprovados: %i = %.1f%%" %(aprovados, porc_aprovados)
print "Reprovados: %i = %.1f%%" %(reprovados, porc_reprovados)
