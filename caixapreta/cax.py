# coding: UTF-8

validos = 0
inc = False
caixas = int(raw_input())
for i in range(caixas):
	entrada = raw_input().split()
	if not inc:
		for n in range(len(entrada)):
			entrada[n] = int(entrada[n])
		if entrada[0] < 0:
			print "dado inconsistente. peso negativo."
			inc = True
		else:
			validos += 1
		if inc:
			continue
		if entrada[1] < 0:
			print "dado inconsistente. combustível negativo."
			inc = True
		else:
			validos += 1
		if inc:
			continue
		if entrada[2] < 0:
			print "dado inconsistente. altitude negativa."
			inc = True
		else:
			validos += 1
print validos,"dados válidos."
		
