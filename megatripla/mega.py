n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())
n1 = n1%11
n2 = n2%11
n3 = n3%11
numeros = []

#numero 1 - adiciona 0
if n1 == 10:
	numeros.append(str(10))
else:
	numeros.append("0"+str(n1))
	
# numero 2
if n2 == 10:
	numeros.append(str(10))
else:
	numeros.append("0"+str(n2))
	
# numero 3	
if n3 == 10:
	numeros.append(str(10))
else:
	numeros.append("0"+str(n3))

print numeros[0]+"-"+numeros[1]+"-"+numeros[2]
