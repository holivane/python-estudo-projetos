import forca
import adivinhacao


print("***********************************************")
print("*************Escolha seu jogo******************")
print("***********************************************")

print("(1)Forca (2)Adivinhação")
jogo = int(input("Qual jogo você quer jogar? \n"))

if (jogo == 1):
    print("Jogando Forca")
elif (jogo == 2):
    print("Jogando Adivinhação")

print("Fim do jogo $(o_o)$")
