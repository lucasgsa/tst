# coding: UTF-8
capacidadetotal = float(raw_input("capacidade? "))
percentual = float(raw_input("percentual hoje? "))
gastod = float(raw_input("gasto diário? "))
volume = capacidadetotal*percentual/100
print "volume: %.2f" %volume
dias = volume/gastod
print "dias restantes:",int(dias)
