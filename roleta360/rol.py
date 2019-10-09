# coding: UTF-8
# CICLO TRIG - TST - LUCAS GABRIEL

angulo = int(raw_input())

# transformo os negativos para positivo
if angulo < 0:
	angulo += 360
angulo = angulo%360
	
if angulo == 90 or angulo == 180 or angulo == 270 or angulo == 0 or angulo == 360:
	print "Sobre eixos"
elif angulo < 90:
	print "Quadrante 1"
elif angulo < 180:
	print "Quadrante 2"
elif angulo < 270:
	print "Quadrante 3"
else:
	print "Quadrante 4"
	
