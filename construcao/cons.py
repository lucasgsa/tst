# coding: UTF-8
# Orçamento construção


preco = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))

altura_tijolo = float(raw_input("Digite a altura do tijolo (Em metros): "))
comprimento_tijolo = float(raw_input("Digite o comprimento do tijolo (Em metros): "))

altura_parede = float(raw_input("Digite a altura das paredes (Em metros): "))
comprimento_parede = float(raw_input("Digite o comprimento das paredes (Em metros): "))

num_tijolos_altura = altura_parede / altura_tijolo
num_tijolos_largura = comprimento_parede / comprimento_tijolo
num_tijolos_total = num_tijolos_altura * num_tijolos_largura

orcamento = num_tijolos_total*preco

print "O número total de tijolos é",num_tijolos_total,"e o orçamento final é de R$",orcamento
