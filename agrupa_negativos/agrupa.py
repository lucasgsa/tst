def agrupa_negativos(lista):
	dic = {"nao-negativos":[],"negativos":[]}
	for n in lista:
		if n >= 0:
			dic["nao-negativos"].append(n)
		else:
			dic["negativos"].append(n)
	return dic
