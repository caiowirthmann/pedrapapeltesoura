import random

jogadas = {
    1 : "pedra",
    2 : "papel",
    3 : "tesoura"
}

jogada_cpu = random.randrange(1,4)

jogada_jogador = input("Digite a sua jogada: Pedra - Papel - Tesoura --> ").lower()

# adicionar um while para checar se a jogada é valida 
if jogada_jogador not in jogadas.values():
    print (f'{jogada_jogador} não é uma opção valida')
else:
    print ('Jogada valida')

# define ganhador
def jogar(cpu, player):
    if cpu == player:
        print (" ===== EMPATE ===== ")
    print (" ===== Você ganhou ===== ")

jogar(jogada_cpu, jogada_jogador)