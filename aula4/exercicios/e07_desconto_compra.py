# Exercício 7
# Leia o valor de uma compra. Se for maior que 100, aplique 10% de desconto.

# escreva seu código abaixo

valorCompra = float(input("Digite o valor da compra  "))
desconto = 0.10
if valorCompra >= 100:
    valorDesconto = valorCompra * desconto
    valorCompra = valorCompra - valorDesconto
    print("desconto de aplicado, valor atualizado", valorCompra)
else: 
    print("sem desconto")