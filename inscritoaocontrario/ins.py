# coding: UTF-8
import math

raio = float(raw_input())
area_circulo = math.pi*(raio**2)

#Calcula lado do triangulo
lado_triangulo = (raio*2)/2**0.5
area_triangulo = lado_triangulo**2

area_nao_comum = area_circulo-area_triangulo
print "Área não comum: %.5f" %area_nao_comum
