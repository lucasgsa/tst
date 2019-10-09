bin = raw_input()
inicial = 2**(len(bin)-1)
soma = 0
for i in bin:
	print "%i * %i = %i" %(int(i),inicial,int(i)*inicial)
	soma += int(i)*inicial
	inicial = inicial/2
print "%s(2) = %i(10)" %(bin,soma)
