# coding: UTF-8
import math

tipo = raw_input()
tamanho = int(raw_input())

if tipo == "Fungicida":
	litros = 1.0*tamanho
	latas = math.ceil(litros/50.0)
	print int(latas),"Fungicida(s). %.2f reais." %(320*latas)
	
elif tipo == "Herbicida":
	litros = 0.3*tamanho
	latas = math.ceil(litros/1.0)	
	print int(latas),"Herbicida(s). %.2f reais." %(100*latas)
		
elif tipo == "Inseticida":
	litros = 2.5*tamanho
	latas = math.ceil(litros/30.0)
	print int(latas),"Inseticida(s). %.2f reais." %(400*latas)
