aposta = int(raw_input())
cor = raw_input()

resultado = int(raw_input())
resultado_cor = raw_input()

if aposta == resultado and cor == resultado_cor:
	print "150"
elif aposta == resultado:
	print "100"
elif cor == resultado_cor:
	if resultado > aposta:
		print "80"
	elif resultado < aposta:
		print "100"
else:
	print 0
