# coding: UTF-8
# CATEGORIA - TST - LUCAS GABRIEL

nome = raw_input()
idade = int(raw_input())
categoria = ""
if idade < 5:
	categoria = "Não pode competir."
elif idade <= 7:
	categoria = "Infantil A."
elif idade <= 10:
	categoria = "Infantil B."
elif idade <= 13:
	categoria = "Juvenil A."
elif idade <= 17:
	categoria = "Juvenil B."
elif idade > 17:
	categoria = "Senior."

print nome+", %i anos, %s" %(idade,categoria)
