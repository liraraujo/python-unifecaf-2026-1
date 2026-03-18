# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

# escreva seu código abaixo
def alunoresultado(media):
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado")

nota1 = int(input("digite a nota 1  "))
nota2 = int(input("digite a nota 2  "))
media = (nota1 + nota2)/2

alunoresultado(media)