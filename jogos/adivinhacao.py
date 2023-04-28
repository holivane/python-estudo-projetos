import random

print("***********************************************")
print("     Vamos jogar um jogo de Adivinhação!!!")
print("***********************************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0
pontos = 150

print("Você ganhou {} pontos :)".format(pontos))
