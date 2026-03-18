# Exercício 1
# Peça a idade do usuário e informe se ele é maior ou menor de idade.

# escreva seu código abaixo

idade = int(input("Digite sua idade "))

def verificadorDeIdade(idade):
    if idade >= 18: 
        print("maior de idade")

    else:
        print("menor de idade")

verificadorDeIdade(idade)