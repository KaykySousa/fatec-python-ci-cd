from main import verify_number

def test():
    assert verify_number(5, 5) == "Parabéns! Você acertou"
    assert verify_number(2, 5) == "Você errou, tente novamente"
