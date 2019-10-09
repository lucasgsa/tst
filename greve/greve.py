# coding: utf-8
# Eleição na ADUF

abstencao = int(raw_input())
a_favor = int(raw_input())
contra = int(raw_input())
total = float(abstencao+a_favor+contra)

print "Resultado da Votação"
print
print abstencao, "abstenções (%.2f%%)" %(abstencao*100/total)
print a_favor, "a favor (%.2f%%)" %(a_favor*100/total)
print contra, "contra (%.2f%%)" %(contra*100/total)

