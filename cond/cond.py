# coding: UTF-8
# Construção de condomínio - TST - Lucas Gabriel

lado1 = float(raw_input())
lado2 = float(raw_input())
area_casa = float(raw_input())

area_total = lado1*lado2
total_casas = int(area_total/area_casa)

print total_casas,"casa(s) pode(m) ser construída(s) no terreno."
