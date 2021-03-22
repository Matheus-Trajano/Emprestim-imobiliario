nome_cliente = str(input("Olá, qual o seu nome?"))
salario_cliente = float(input("Poderia me informar o valor do seu salário?"))
casa_vale = float(input("Qual o valor da casa em negociação?"))
anos_de_pagamento = int(input("Em quantos anos voce pretende pagar pelo imóvel?"))

prestacao_min = casa_vale / (anos_de_pagamento * 12)
meses = (anos_de_pagamento * 12)
parcela_minima = salario_cliente * 30 / 100  # valor da prestação mensal não pode ser superior a 30% do salário.
txt = float(prestacao_min / salario_cliente * 100)

print(nome_cliente, ", para conseguir o imóvel no valor de R$", casa_vale, "as parcelas serao de R$", prestacao_min,
      "durante", meses, "meses,ou seja,", anos_de_pagamento, "anos.")

if prestacao_min <= parcela_minima:
    print(
        "Parabéns,você conseguiu o empréstimo para sua nova casa, a TraSantos esta feliz por sua conquista, "
        "pode contar conosco.")
else:
    print("o seu impréstimo não foi concedido devido ao valor execeder o limite de 30%, chegando a {txt:.0f}%.".format(
        txt=txt))
