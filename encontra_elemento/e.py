# coding: UTF-8
# ENCONTRA ELEMENTO - TST - LUCAS GABRIEL


numero = raw_input()
sequencia = raw_input().split()

esta = False

for e in sequencia:
	if e == numero:
		esta = True
		break
print "sim" if esta else "não"
