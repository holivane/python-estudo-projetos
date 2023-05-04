import random


def jogar():

    imprime_mensage_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = imprime_letras_acertadas(palavra_secreta)
    print("Acerte a palavra: ", letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            desenha_forca(erros)
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    palavra_secreta = palavra_secreta.upper()

    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprime_mensage_abertura():
    print("**********************************************************************")
    print("                Vamos jogar o jogo da Forca!!!")
    print("**********************************************************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta


def imprime_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? \n")
    chute = chute.strip().lower()
    return chute


def marca_chute_correto(chute, acertada, palavra):
    index = 0
    for letra in palavra:
        if (chute == letra):
            acertada[index] = letra
        index += 1


def desenha_forca(erros):
    print("--------------")
    print("|/           |")

    if (erros == 0):
        print("|           (_)")
        print("|")
        print("|")
        print("|")

    if (erros == 1):
        print("|           (_)")
        print("|            |")
        print("|            |")
        print("|")

    if (erros == 2):
        print("|           (_)")
        print("|           /|")
        print("|            |")
        print("|")

    if (erros == 3):
        print("|           (_)")
        print("|           /|\\")
        print("|            |")
        print("|")

    if (erros == 4):
        print("|           (_)")
        print("|           /|\\")
        print("|            |")
        print("|           /")

    if (erros == 5):
        print("|           (_)")
        print("|           /|\\")
        print("|            |")
        print("|           / \\")

    print("|")
    print("|_______________")


def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("A palavra é {}".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra é {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
