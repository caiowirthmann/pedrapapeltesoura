import random

jogadas = {
    1 : "pedra",
    2 : "papel",
    3 : "tesoura"
}

jogada_cpu = jogadas[(random.randrange(1,4))]

print (" ============== INICIO DE JOGO ============== ")
print ()

while True:
    jogada_jogador = input("Digite a sua jogada: (Pedra - Papel - Tesoura) --> ").lower()
    if jogada_jogador in jogadas.values():
        break
    else:
        print (f'{jogada_jogador} não é uma opção valida') 

# define ganhador
def jogar(cpu, player):
    print()
    print(f'O computador jogou {cpu}')
    print()
    if cpu == player:
        print (" ================ EMPATE! ================ ")

    # simples mas pode ser que tenha um jeito melhor de fazer
    # esse cruzamento para checar a combinação
    if player == "pedra" and cpu == "tesoura":
        print (" ================ VITÓRIA ================ ")
    if player == "pedra" and cpu == "papel":
        print (" ================ DERROTA ================ ")
    if player == "papel" and cpu == "tesoura":
        print (" ================ DERROTA ================ ")
    if player == "papel" and cpu == "pedra":
        print (" ================ VITÓRIA ================ ")
    if player == "tesoura" and cpu == "papel":
        print (" ================ VITÓRIA ================ ")
    if player == "tesoura" and cpu == "pedra":
        print (" ================ DERROTA ================ ")
    
    print ()
    print (" ============== FIM DE JOGO ============== ")

jogar(jogada_cpu, jogada_jogador)       