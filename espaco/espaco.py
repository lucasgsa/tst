# coding: UTF-8

nomes = []
espacos = []

for vezes in range(3):
	nome = raw_input()
	nomes.append(nome)
	tamanho = float(raw_input())
	espacos.append(tamanho)
print "SPLab - Espaço utilizado pelos usuários"
print "-"*45
print "Nr., Usuário, Espaço Utilizado\n"

ocupado1 = (espacos[0]/1024)/1024
ocupado2 = (espacos[1]/1024)/1024
ocupado3 = (espacos[2]/1024)/1024

print "1, %s, %.2f MB" %(nomes[0], ocupado1)
print "2, %s, %.2f MB" %(nomes[1], ocupado2)
print "3, %s, %.2f MB" %(nomes[2], ocupado3)
print
print "Espaço total ocupado: %.2f MB" %(ocupado1+ocupado2+ocupado3)
print "Espaço médio ocupado: %.2f MB" %((ocupado1+ocupado2+ocupado3)/3)
