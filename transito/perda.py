# coding: UTF-8

segunda = float(raw_input())
terca = float(raw_input())
quarta = float(raw_input())
quinta = float(raw_input())
sexta = float(raw_input())
soma = segunda+terca+quarta+quinta+sexta
print "Você perdeu %i min na semana (média de %.1f min por dia)." %(soma, soma/5)
print "Isso significa %.2f%% da sua semana produtiva." %((soma/360)*5)
print "Daria para assistir %i episódio(s) de House." %(soma/50)
