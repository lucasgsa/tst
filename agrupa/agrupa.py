def naLista(lista,elemento):
	esta = False
	for i in lista:
		if i == elemento:
			return True
	return False

def agrupa_proximos(lista,n,d):
	final = []
	n = range(n-d+1,n+d)
	for e in lista:
		if naLista(n, e):
			final.append(e)
	return final
