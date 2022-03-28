from forca import jogar_forca
from adivinhacao import jogar_adivinhacao

print("")
print("(1)Forca \n (2) Adivinhação")
jogo = input("Digite qual jogo: ")

while True:
    if jogo == "1":
        print("jogando forca")
        jogar_forca()
    elif jogo == "2":
        print("jogando forca")
        jogar_adivinhacao()
    else:
        print("selecione uma opção válida!!!")