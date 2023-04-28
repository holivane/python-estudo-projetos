import forca
import adivinhacao

def escolher_jogo():
    print("***********************************************")
    print("***********  Escolha seu jogo  ****************")
    print("***********************************************")

    print("(1)Forca (2)Adivinhação")
    jogo = int(input("Qual jogo você quer jogar? \n"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

    print("Fim do jogo $(o_o)$")

if (__name__ == "__main__"):
    escolher_jogo()
