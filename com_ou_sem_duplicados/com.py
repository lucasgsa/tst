num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())
num4 = int(raw_input())
num5 = int(raw_input())
duplicado = False
if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
	duplicado = True
elif num2 == num3 or num2 == num4 or num2 == num5:
	duplicado = True
elif num3 == num4 or num3 == num5:
	duplicado = True
elif num4 == num5:
	duplicado = True

if duplicado:
	print "com duplicados"
else:
	print "sem duplicados"
