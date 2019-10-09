# coding: UTF-8
# Área Figuras - TST - LUCAS GABRIEL
import math

tipo = raw_input()
if tipo == "círculo":
	raio = float(raw_input())
	area = math.pi*(raio**2)
	print "Área do círculo: %.2f (cm2)" %area
	
elif tipo == "quadrado":
	lado = float(raw_input())
	print "Área do quadrado: %.2f (cm2)" %(lado**2)
	
elif tipo == "retângulo":
	lado1 = float(raw_input())
	lado2 = float(raw_input())
	print "Área do retângulo: %.2f (cm2)" %(lado1*lado2)

elif tipo == "triângulo":
	base = float(raw_input())
	altura = float(raw_input())
	print "Área do triângulo: %.2f (cm2)" %(base*altura/2)
