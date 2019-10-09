mes = 0
meses = {1:"jan",2:"fev",3:"mar",4:"abr",5:"mai",6:"jun",7:"jul",8:"ago",9:"set",10:"out",11:"nov",12:"dez"}
valor_mes = 0
dinheiro = 0
for i in range(12):
	dinheiro += 500
	valor = int(raw_input())
	dinheiro -= valor
	if dinheiro >= valor_mes:
		valor_mes = dinheiro
		mes = i
mes += 1
print meses[mes]
