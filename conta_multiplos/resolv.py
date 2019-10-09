# coding: UTF-8

mult=input()
quantas = 0
while True:
	entrada = raw_input().split()
	if entrada[0] == 'fim': break
	if int(entrada[0])%mult == 0 and int(entrada[1])%mult == 0:
		quantas += 1
print quantas
