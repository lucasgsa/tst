custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissao = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())
primeira = custo+(custo*despesas/100)+(custo*lucro/100)
segunda = 100-impostos-comissao-descontos-encargos
print (primeira/segunda)*100
