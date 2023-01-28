def jogar_forca():
    print("**********************************")
    print("          Jogo de forca           ")
    print("**********************************\n")

    palavra_secreta = "amarelo"
    enforcou = False
    acertou = False

    # enquanto
    while not enforcou and not acertou:
        chute = input("digite uma letra: ")
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(letra)
            index += 1

    print("Fim jogo")


if __name__ == "__main__":
    jogar_forca()
