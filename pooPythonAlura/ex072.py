#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#leia um número digitado pelo usuário e exiba-o por extenso

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
num = 0

print('digite um numero entre 0 e 20 \n')
print('digite 99 para sair \n')
while num != 99:
    num = int(input('digite um numero = '))
    if num > 21 or num < 0:
        if num != 99:
            print('Tente novamente.')
    else:
        print(extenso[num])
