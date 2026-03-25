# Crie um algoritmo que leia uma lista de inteiros e retorne a 
# soma de todos os elementos

a = [1, 2, 3, 4, 5]
n = 0


for i in range(len(a)):
    n = a[i] + n
    print(n)