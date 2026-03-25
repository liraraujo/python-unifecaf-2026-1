# Crie um aplicativo que leia uma lista de inteiros 
# e retorne todos os números ímpares

app = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = []

for i in app:
    if app[i] % 2 != 0:
        n.append(app[i])
        print(n)
    else:
        print("")