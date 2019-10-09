# coding: UTF-8
nota = 0

print "== Estágio 1 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
nota += peso1*nota1

print "== Estágio 2 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
nota += peso2*nota2

print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))
nota += peso3*nota3

print "== Resultados =="
print "Média parcial: %.1f" %nota
print "Nota na final, pra média 5.0 = %.1f" %((5-(nota*0.6))/0.4)
print "Nota na final, pra média 7.0 = %.1f" %((7-(nota*0.6))/0.4)
