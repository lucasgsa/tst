# coding: UTF-8
entrada = raw_input()
vogais = ["a","e","i","o","u","A","E","I","O","U"]
for l in entrada:
	print "<%s> %s" %(l, "sim" if l in vogais else "nao")
