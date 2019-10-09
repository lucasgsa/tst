# coding: UTF-8
# LUCAS GABRIEL - APROVADOS E REPROVADOS - TST

total_alunos = int(raw_input())
#Aprovados
soma_aprov = 0.0
alunos_aprov = 0.0
#Reprovados
soma_reprov = 0.0
alunos_reprov = 0.0
for n in range(total_alunos):
	nota = float(raw_input())
	if nota < 7.0:
		soma_reprov += nota
		alunos_reprov += 1
	else:
		soma_aprov += nota
		alunos_aprov += 1
print "Reprovados: %i" %alunos_reprov
if alunos_reprov != 0:
	print "Média: %.1f" %(soma_reprov/alunos_reprov)
print 
print "Aprovados: %i" %alunos_aprov
if alunos_aprov != 0:
	print "Média: %.1f" %(soma_aprov/alunos_aprov)
