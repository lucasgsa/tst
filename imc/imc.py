peso = float(raw_input())
altura = float(raw_input())

imc = peso/altura**2

diferenca_imc = (imc-24.9)

peso_real = ((imc-diferenca_imc)*altura**2)-peso


print "IMC atual = %.2f" %imc
print "Peso a ser ganho/perdido = %.2f" %peso_real
