# coding: UTF-8
# AVALIAÇÃO DOCENTE - TST - LUCAS GABRIEL

semestres = int(raw_input())
ensino = int(raw_input())
intelectual = int(raw_input())
orientacao = int(raw_input())
adm = int(raw_input())

media = (ensino+intelectual+orientacao+adm)/semestres
if semestres < 4:
	print "Promoção indeferida. Número de semestres insuficiente."
elif ensino < 320 or intelectual < 100 or orientacao < 20:
	print "Promoção indeferida. Pontuação mínima não alcançada."
elif media < 140:
	print "Promoção indeferida. Média insuficiente."
else:
	print "Promoção deferida. Parabéns!"
