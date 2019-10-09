# coding: UTF-8

pos1 = float(raw_input("Posição inicial? "))
velocidade1 = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
aceleracao = float(raw_input("Aceleração? "))

pos_final = pos1 + (velocidade1*tempo) + ((aceleracao*tempo**2)/2)
velocidade2 = velocidade1 + aceleracao*tempo
velocidade_media = velocidade1 + aceleracao*tempo/2

print
print "Dados da questão"
print "="*16

print "   Posição inicial: %.2f m" %pos1
print "Velocidade inicial: %.2f m/s" %velocidade1
print "        Aceleração: %.2f m/s2" %aceleracao
print "             Tempo: %.2f s" %tempo
print "  Velocidade final: %.2f m/s" %velocidade2
print "  Velocidade média: %.2f m/s" %velocidade_media
print "     Posição final: %.2f m" %pos_final
