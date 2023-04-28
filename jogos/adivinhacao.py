import random

def jogar():
    print("***********************************************")
    print("     Vamos jogar um jogo de Adivinhação!!!")
    print("***********************************************")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 150

    print("Qual o nívl de dificuldade?")
    print("1- Fácil 2- Médio 3- Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
        print("Você escolheu o nível Fácil")
    elif (nivel == 2):
        total_de_tentativas = 10
        print("Você escolheu o nível Médio")
    else:
        total_de_tentativas = 5
        print("Você escolheu o nível Difícil")

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Vocês acertou!!!!!!!!! O número secreto é {}".format(chute_str))
            break
        else:
            if (maior):
                print(
                    "Você errou! {} é maior que o número secreto =(".format(chute_str))
            elif (menor):
                print(
                    "Você errou! {} é menor que o número secreto =(".format(chute_str))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Você ganhou {} pontos :)".format(pontos))
