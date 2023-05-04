import forca
import adivinhacao

def escolher_jogo():
    print("\n")
    print("**********************************************************************")
    print("***********************  Escolha seu jogo  ***************************")
    print("**********************************************************************")

    print("\n(1)Forca (2)Adivinhação\n")
    jogo = int(input("Qual jogo você quer jogar? \n"))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()
