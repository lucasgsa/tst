vitorias = 0
empates = 0
derrotas = 0
gols_pro = 0
gols_contra = 0
pontos_casa = 0
pontos_fora = 0
pontos = 0

for jogo in range(10):
	resultado, onde = raw_input().split()
	if onde == "(c)":
		time1 = int(resultado[0])
		time2 = int(resultado[2])
		gols_pro += time1
		gols_contra += time2
		if time1 > time2:
			pontos_casa += 3
			vitorias += 1
			pontos += 3
		elif time1 == time2:
			pontos_casa += 1
			empates += 1
			pontos += 1
		else:
			derrotas += 1

	elif onde == "(f)":
		time2 = int(resultado[0])
		time1 = int(resultado[2])
		gols_pro += time1
		gols_contra += time2
		if time1 > time2:
			pontos_fora += 3
			vitorias += 1
			pontos += 3
		elif time1 == time2:
			pontos_fora += 1
			empates += 1
			pontos += 1
		else:
			derrotas += 1
print "%iv, %ie, %id" %(vitorias,empates,derrotas)
print "pontos:", pontos
print "saldo: %i (%i pro, %i contra)" %(gols_pro-gols_contra, gols_pro, gols_contra)
print "pontos em casa:" ,pontos_casa
print "pontos fora:", pontos_fora
