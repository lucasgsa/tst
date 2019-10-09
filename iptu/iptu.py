# coding: UTF-8

area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))
iptu = (area*aliquota)+35.0
print "IPTU: R$ %.2f" %iptu
print
print "Pagamento:"
print "1. Quota única. R$ %.2f" %(iptu*0.75)
print "2. Em 6 parcelas. Total: R$ %.2f" %(iptu*0.95)
print "   6 x R$ %.2f" %((iptu*0.95)/6)
print "3. Em 10 parcelas. Total: R$ %.2f" %iptu
print "   10 x R$ %.2f" %((iptu)/10)
