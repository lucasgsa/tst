# coding: UTF-8

tweets = int(raw_input())
paginas = tweets/400
perdidos = tweets%400
porcentagem = float(perdidos)*100/tweets

print "Serão necessárias %i página(s) para visualizar os tweets." %paginas
print "%.1f%% dos tweets serão perdidos." %porcentagem
