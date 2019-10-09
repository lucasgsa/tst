atual = float(raw_input("Valor atual? "))
novo = float(raw_input("Novo valor? "))

reajuste = ((novo/atual) * 100) - 100

print "Reajuste de %.1f%%" %reajuste
