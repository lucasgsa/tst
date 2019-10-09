conta  = raw_input()
soma = 0

for n in conta:
	soma += int(n)
resto = soma%11

n_resto = 0

for q in str(resto):
	n_resto += 1

if n_resto == 1:
	print conta+"-0"+str(resto)
else:
	print conta+"-"+str(resto)
