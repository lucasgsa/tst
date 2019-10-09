area = float(raw_input())
valorm2 = float(raw_input())
preco = area*valorm2
vezes = raw_input()
if vezes == "vista":
	print "Total: R$ %.2f" %(preco*0.8)
elif vezes == "2x":
	preco = preco*0.9
	print "Total: R$ %.2f. Parcelas: R$ %.2f" %(preco,preco/2)
elif vezes == "3x":
	preco = preco*0.95
	print "Total: R$ %.2f. Parcelas: R$ %.2f" %(preco,preco/3)
