# jogo de adivinhação
from random import randint


def jogar_adivinhacao():
    numero_secreto = randint(1, 100)
    total_tentativas = 0
    pontos = 1000
    print("**********************************")
    print("          Jogo de sorteio         ")
    print("**********************************\n")
    print("sorteio de um numero entre 1 e 100")
    print("Escolha uma dificuldade:\n"
          "(1) fácil (2) normal (3)dificil")

    while not total_tentativas:
        dificuldade = int(input("dificuldade: "))
        if dificuldade == 1:
            total_tentativas = 20
        elif dificuldade == 2:
            total_tentativas = 10
        elif dificuldade == 3:
            total_tentativas = 5
        else:
            print("digite uma opção válida!!!")


    for rodada in range(1, total_tentativas + 1):
        chute = int(input("Digite um numero: "))
        print(f"tentativa {rodada} de {total_tentativas}")
        if chute > 101 or chute < 1:
            print("Só deve ser digitado numeros entre 1 e 100!!!")
            continue
        if numero_secreto == chute:
            print(f'voce acertou e fez {pontos} pontos \o/')
            break
        elif chute > numero_secreto:
            print('Voce errou. O seu numero foi maior que o numero secreto')
        elif chute < numero_secreto:
            print('Voce errou. O seu numero foi menor que o numero secreto')
        pontos_perdidos = abs(chute - numero_secreto)
        pontos -= pontos_perdidos

    print('fim do jogo')


if __name__ == "__main__":
    jogar_adivinhacao()
