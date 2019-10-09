# coding: UTF-8

ax = int(raw_input())
ay = int(raw_input())

bx = int(raw_input())
by = int(raw_input())

cx = int(raw_input())
cy = int(raw_input())

primeira_reta = ((ax-bx)**2 + (ay-by)**2)**0.5

segunda_reta = ((bx-cx)**2 + (by-cy)**2)**0.5

terceira_reta = ((ax-cx)**2 + (ay-cy)**2)**0.5

perimetro = primeira_reta+segunda_reta+terceira_reta

print "O perímetro é de %.2f" %perimetro

