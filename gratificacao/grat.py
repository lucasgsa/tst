# coding: UTF-8
# Gratificação natalina - TST - LUCAS GABRIEL

codigo = int(raw_input())
if codigo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
elif codigo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
elif codigo == 3:
	dias = int(raw_input())
	g = (235-dias)*2.0
	if dias == 0:
		g_total = 500.0
	else:
		g_total = g
	print "Valor da gratificação R$ %.2f." %(g_total)
	print "Deverá receber em dezembro R$ %.2f." %(8000+g_total)

elif codigo == 4:
	dias = int(raw_input())
	g = (235-dias)*1.0
	if dias == 0:
		g_total = 300.0
	else:
		g_total = g
	print "Valor da gratificação R$ %.2f." %(g_total)
	print "Deverá receber em dezembro R$ %.2f." %(5000+g_total)
	
elif codigo == 5:
	dias = int(raw_input())
	g = (235-dias)*0.7
	if dias == 0:
		g_total = 200.0
	else:
		g_total = g
	print "Valor da gratificação R$ %.2f." %(g_total)
	print "Deverá receber em dezembro R$ %.2f." %(2800+g_total)
