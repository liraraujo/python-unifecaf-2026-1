# Peça a senha ao usuário e continue pedindo até ele digitar: unifecaf
# - estrutura do while: while condição:
# - use input para ler a senha

senha = input("Digite a senha: ")

if senha == "unifecaf":
    print("Senha correta!")
while senha != "unifecaf":
    print("Senha incorreta, tente novamente.")
    senha = input("Digite a senha: ")