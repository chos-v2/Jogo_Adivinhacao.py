from random import randint

numero_secreto = randint(1, 100)
tentativas = 0

def linhas():
    print("-----------------------")

linhas()
print("JOGO DAS TENTATIVAS")
linhas()

while True:
    try:
        tentativa = int(input("ESCOLHA UM NUMERO ENTRE 1 E 100: "))
    except ValueError:
        print("ENTRADA INVÁLIDA, DIGITE APENAS NÚMEROS INTEIROS")
        continue

    tentativas += 1

    if tentativa < 1 or tentativa > 100:
        print("DIGITE APENAS NUMEROS ENTRE 1 E 100")
        pass

    elif tentativa < numero_secreto:
        print("VOCÊ ERROU, TENTE UM NUMERO MAIOR")

    elif tentativa > numero_secreto:
        print("VOCE ERROU, TENTE UM NUMERO MENOR")

    else:
        linhas()
        print(f"VOCE ACERTOU, O NUMERO ERA {numero_secreto}!")
        print(f"TOTAL DE TENTATIVAS: {tentativas}")
        linhas()
        break