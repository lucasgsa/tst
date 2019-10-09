# coding: UTF-8
# Passagem Aérea - TST - Lucas Gabriel

distancia = float(raw_input())
aliquota = float(raw_input())
preco = (distancia*aliquota)+51.0

print "Valor da passagem: R$ %.2f" %preco
print
print "Pagamento:"
print "1. À vista. R$ %.2f" %(preco*0.75)
print "2. Em 6 parcelas. Total: R$ %.2f" %(preco*0.95)
print "   6 x R$ %.2f" %((preco*0.95)/6)
print "3. Em 10 parcelas. Total: R$ %.2f" %preco
print "   10 x R$ %.2f" %((preco)/10)
