def caixa_registradora(lista, meta):
    soma = 0
    comissoes = 0
    for valor in lista:
        soma += valor
        if valor < 1000.0:
            comissoes += valor * 0.05
        elif valor < 5000.0:
            comissoes += valor * 0.10
        else:
            comissoes += valor * 0.15
    if soma < meta:
        situacao = "Prejuizo"
    else:
        situacao = "Lucro"
    return [soma, comissoes, situacao]

