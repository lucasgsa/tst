numero = int(raw_input())
total = int(raw_input())
quantas = 0
for n in range(total):
	num = int(raw_input())
	if num%numero == 0:
		quantas += 1
print "%i (%.1f%%)" %(quantas, quantas*100.0/total)
