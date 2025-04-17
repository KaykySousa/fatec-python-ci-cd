from random import randint

random_n = randint(0, 10)
n = int(input("Digite um número entre 0 e 10: "))

if random_n == n:
    print("Parabéns! Você acertou")
else:
    print("Você errou, tente novamente")
