maior_nome = raw_input()
maior = len(maior_nome)

segundo = raw_input()
if len(segundo) < maior:
	maior_nome = segundo
	maior = len(segundo)
	
terceiro = raw_input()
if len(terceiro) < maior:
	maior_nome = terceiro
	maior = len(terceiro)
	
print maior_nome,maior
