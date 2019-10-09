# TELEFONIA - TST - LUCAS GABRIEL

preco = 0.0
minutos = int(raw_input())
if minutos <= 3:
	print "R$ %.2f" %((0.5*minutos)+1)
elif minutos > 3:
	if (minutos - 3)%5 == 0:
		preco = ((minutos)/5)*3
		print "R$ %.2f" %(preco+1)
	else:
		preco = (((minutos)/5)*3) + ((minutos)%5)*0.7
		print "R$ %.2f" %(preco+1) 
