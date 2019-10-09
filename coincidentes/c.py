# coding: UTF-8
# COINCIDENTES - TST - LUCAS GABRIEL

p1 = raw_input()
p2 = raw_input()

total = 0

letras = len(p1) + len(p2)

print "Letras coincidentes"

if len(p1) >= len(p2):
	for l in range(len(p2)):
		if p2[l] == p1[l]:
			print "'%s' na posição %i" %(p2[l],l+1)
			total += 1
else:
	for l in range(len(p1)):
		if p1[l] == p2[l]:
			print "'%s' na posição %i" %(p1[l],l+1)
			total += 1
print "Total de letras coincidentes: %i (%i%%)" %(total, total*100/letras)
