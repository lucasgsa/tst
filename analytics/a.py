# coding: UTF-8

def  conta_votos(votacoes, id):
	sim = nao = 0
	for voto in votacoes:
		voto = voto.split(",")
		if int(voto[2]) == id:
			if voto[1] == "sim":
				sim += 1
			else:
				nao += 1
	return [sim,nao]
