import random

jogadas = {
    1 : "pedra",
    2 : "papel",
    3 : "tesoura"
}

def gerar_jogada_cpu():
    jogada_cpu = jogadas[(random.randrange(1,4))]
    return jogada_cpu

print (" ============== INICIO DE JOGO ============== ")
print ()

def gerar_jogada_jogador():
    while True:
        jogada_jogador = input("Digite a sua jogada: (Pedra - Papel - Tesoura): ").lower()
        if jogada_jogador in jogadas.values():
            break
        else:
            print (f'{jogada_jogador} não é uma opção valida. Escolha Pedra - Papel - Tesoura') 
    return jogada_jogador

# define ganhador
def jogar(cpu, player):
    # talvez encapsular a função inteira em um while true para rodar quantas vezes o jogador quiser
    print()
    print(f'O computador jogou: {cpu}')
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
    #print (" ============== FIM DE JOGO ============== ")

def jogar_novamente():
    while True:
        jogar_novamente = input("Deseja jogar novamente? Digite S para (sim) ou N para (não) ")
        if jogar_novamente in ("s", "S", "n", "N"):
            break
        else:
            print ("Digite uma opção valida")

    if jogar_novamente in ("n", "N"):
        print (" ============== FIM DE JOGO ============== ")
        return False
    else:
        return True

def main():
    while True:
        jogada_cpu = gerar_jogada_cpu()
        jogada_jogador = gerar_jogada_jogador()
        jogar(jogada_cpu, jogada_jogador)
        novo_jogo = jogar_novamente()
        if novo_jogo == False:
            break
        
main() 