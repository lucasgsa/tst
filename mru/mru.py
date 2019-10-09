# coding: UTF-8
#LUCAS GABRIEL - TST - MRU

pos_1 = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())

pos_final = pos_1+(velocidade*tempo)

print "Posição final do móvel"
print "S(%.1f) = %.1f m" %(tempo, pos_final)
