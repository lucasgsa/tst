a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

eh = True

if b-c < 0:
	bc = c-b
else:
	bc = b-c

if a-c < 0:
	ac = c-a
else:
	ac = a-c
	
if a-b < 0:
	ab = b-a
else:
	ab = a-b
	
if not bc < a < b+c:
	eh = False
	
if not ac < b < a+c:
	eh = False
	
if not ab < c < a+b:
	eh = False

if eh:
	print "triangulo valido.", a+b+c
else:
	print "triangulo invalido."
