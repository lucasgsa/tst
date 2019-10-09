# coding: UTF-8
import math
capacidade = float(raw_input("Capacidade de revestimento? "))
print ""
print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))
print ""
print "== Resultados =="
area_chao = (comprimento*largura)
area_parede1 = comprimento*altura*2
area_parede2 = largura*altura*2
area_total = area_chao+area_parede1+area_parede2
print "Área total a revestir:",area_total,"m2"
print "Número de caixas:",int(math.ceil(area_total/capacidade))
