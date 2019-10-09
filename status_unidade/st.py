# coding: UTF-8
# STATUS UNIDADE - TST - LUCAS GABRIEL

mts = int(raw_input())
notas = 0
for vezes in range(mts):
	nota = float(raw_input())
	notas += nota
if mts > 2:
	media = (notas/mts)-0.5
else:
	media = notas/mts
print media
if mts == 1 or media < 6.0:
	print "Aluno ainda não aprovado na unidade"
else:
	print "Aluno aprovado na unidade"
	
