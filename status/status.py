nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = int(raw_input())
porc_faltas = 100-((faltas*100.0)/30)
if porc_faltas > 75:
	media = (nota1+nota2+nota3)/3
	if media >= 7:
		print "aprovado por media"
	elif media >= 4:
		print "prova final"
	else:
		print "reprovado por nota"
else:
	print "reprovado por faltas"
