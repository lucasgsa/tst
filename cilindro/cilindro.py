# coding: UTF-8
import math
print "Cálculo da Superfície de um Cilindro"
print "---"
diametro = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))
raio = diametro/2
area_circulo = math.pi*(raio**2)
circunferencia = 2*math.pi*raio
area_lado = circunferencia*altura
area_total = area_lado+(area_circulo*2)
print "---"
print "Área calculada: %.2f" %area_total

