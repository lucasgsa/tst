altura = int(raw_input())
quantos = 1
espacos = altura-1
while quantos <= (altura*2)-1:
	print (" "*espacos)+"o"*quantos
	quantos += 2
	espacos -= 1
print (" "*(altura-1))+("o")
