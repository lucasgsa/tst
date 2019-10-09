# coding: UTF-8
# VENDAS POR CARTÃO - TST - LUCAS GABRIEL

valor = float(raw_input("Valor (R$): "))
tipo = raw_input("(D)ébito ou (C)rédito: ")
tipo = tipo.lower()
if tipo == "d":
	print "Valor líquido a receber: %.2f" %(valor*0.97)
elif tipo == "c":
	print "Valor líquido a receber: %.2f" %(valor*0.95)
else:
	print "Tipo incorreto. Tente novamente."
