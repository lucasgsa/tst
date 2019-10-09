a = float(raw_input())
b = float(raw_input())
c = float(raw_input())
delta = (b**2) - (4*a*c)
if delta < 0:
	print "sem raizes reais"
elif delta > 0:
	x1 = ((-b) + (delta**0.5))/(2*a)
	x2 = ((-b) - (delta**0.5))/(2*a)
	print "x1 = %.2f" %x1
	print "x2 = %.2f" %x2
else:
	x = (-b)/(2*a)
	print "x = %.2f" %x
