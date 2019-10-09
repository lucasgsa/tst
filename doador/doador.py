# coding: UTF-8

abo = True
rh = True

abo_paciente = raw_input()
rh_paciente = raw_input()

abo_doador = raw_input()
rh_doador = raw_input()

# Testes ABO
if abo_paciente == "AB":
	abo = True
	
elif abo_paciente == "A":
	if abo_doador == "A" or abo_doador == "O":
		abo = True
	else:
		abo = False
		
elif abo_paciente == "B":
	if abo_doador == "B" or abo_doador == "O":
		abo = True
	else:
		abo = False
		
elif abo_paciente == "O":
	if abo_doador == "O":
		abo = True
	else:
		abo = False
		
# Testes RH
if rh_paciente == "+":
	rh = True
if rh_paciente == "-":
	if rh_doador == "-":
		rh = True
	else:
		rh = False

if abo == True and rh == True:
	print "compatível"
else:
	print "incompatível"
