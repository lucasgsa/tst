# coding: UTF-8
# TST - LUCAS GABRIEL - MELHOR ATAQUE

times = int(raw_input())


melhortime = []
quantos_gols = 0


total_gols = 0.0

for teams in range(times):
	nome = raw_input()
	gols = int(raw_input())
	total_gols += gols
	if gols == quantos_gols:
		melhortime.append(nome)
	elif gols > quantos_gols:
		melhortime = [nome]
		quantos_gols = gols
print "Time(s) com melhor ataque (%i gol(s)):" %quantos_gols
for teams in melhortime:
	print teams
print
print "Média de gols marcados: %.1f" %(total_gols/times)
