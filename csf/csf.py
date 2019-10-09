# coding: UTF-8
# CSF - TST - LUCAS GABRIEL

nota_enem = float(raw_input())
creditos_concluidos = float(raw_input())

porcentagem_creditos = (creditos_concluidos*100)/416

if nota_enem >= 600.0:
	enem = True
else:
	enem = False

if porcentagem_creditos >= 20.0 and porcentagem_creditos <= 90.0:
	creditos = True
else:
	creditos = False

if enem == True and creditos == True:
	print "Todas as condições satisfeitas."
elif enem == True and creditos == False:
	print "Condição CRÉDITOS não satisfeita."
elif enem == False and creditos == True:
	print "Condição ENEM não satisfeita."
else:
	print "Nenhuma condição satisfeita."
