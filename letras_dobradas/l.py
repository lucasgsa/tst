# coding: UTF-8

dobradas = []
normais = []

for i in range(int(raw_input())):
	palavra = raw_input()
	dobr = False
	for l in range(0,len(palavra)-1):
		if palavra[l] == palavra[l+1]:
			dobr = True
	if dobr:
		dobradas.append(palavra)
	else:
		normais.append(palavra)
		
print "%i palavra(s) com letras dobradas:" %(len(dobradas))
for p in dobradas:
	print p
print "---"
print "%i palavra(s) sem letras dobradas:" %(len(normais))
for p in normais:
	print p
