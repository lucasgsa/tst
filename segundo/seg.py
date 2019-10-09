# coding: UTF-8
# SEGUNDO - TST - LUCAS GABRIEL

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())
n4 = int(raw_input())

print "Considerando os números %i, %i, %i e %i" %(n1,n2,n3,n4)

m1 = 0
m2 = 0
m3 = 0
m4 = 0

m1 = n1
#Segundo numero
if n2 >= m1:
	m2 = m1
	m1 = n2
else:
	m2 = n2
#Terceiro numero	
if n3 >= m1:
	m3 = m2
	m2 = m1
	m1 = n3
elif n3 >= m2:
	m3 = m2
	m2 = n3
else:
	m3 = n3
#Quarto numero
if n4 >= m1:
	m4 = m3
	m3 = m2
	m2 = m1
	m1 = n4
elif n4 >= m2:
	m4 = m3
	m3 = m2
	m2 = n4
elif n4 >= m3:
	m4 = m3
	m3 = n4
else:
	m4 = n4
#Conclusao
print "O segundo menor número é", m3
print "O segundo maior número é", m2
