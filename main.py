from random import randint

def verify_number(x, y):
    if x == y:
        return "Parabéns! Você acertou"
    else:
        return "Você errou, tente novamente"

def main():
    random_n = randint(0, 10)
    n = int(input("Digite um número entre 0 e 10: "))

    print(verify_number(random_n, n))

if __name__ == "__main__":
    main()
