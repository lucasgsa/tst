# coding: UTF-8

def paraMaiusculo(letra):
	k = ord(letra)
	if k < 97:
		return letra
	k -= 32
	return chr(k)
def paraMinusculo(letra):
	k = ord(letra)
	if k >= 97:
		return letra
	k += 32
	return chr(k)

def caixa_alta(frase):
	nova = ""
	for l in range(len(frase)):
		# Primeiro
		if l == 0 and len(frase) > 1 and frase[l] != " ":
			if frase[1] == " ":
				nova += paraMinusculo(frase[l])
			else:
				nova += paraMaiusculo(frase[l])
		# Ultimo
		elif l == len(frase)-1 and len(frase) > 1 and frase[l ] != " ":
			if frase[l-1] == " ":
				nova += paraMinusculo(frase[l])
			else:
				nova += frase[l]
		#Resto
		elif frase[l] != " ":
			# Uma letra
			if frase[l-1] == " " and frase[l+1] == " ":
					nova += paraMinusculo(frase[l])
			elif frase[l-1] == " ":
				nova += paraMaiusculo(frase[l])
			else:
				nova += frase[l]
		else:
			nova += " "	
	return nova
	
print caixa_alta(raw_input())
