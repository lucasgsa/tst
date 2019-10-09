# coding: UTF-8
# IMPRIME RANKING - LUCAS GABRIEL - TST

pontos_ultimo = -1
atual = 1
ultimo = 1

times = int(raw_input())
for i in range(times):
	time = raw_input()
	pontos = int(raw_input())
	if pontos == pontos_ultimo:
		print "%i. %s (%i)" %(ultimo, time, pontos)
	else:
		print "%i. %s (%i)" %(atual, time, pontos)
		ultimo = atual
	atual += 1
	pontos_ultimo = pontos
