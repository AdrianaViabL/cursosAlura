#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#leia um número digitado pelo usuário e exiba-o por extenso

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
num = 0

print('digite 99 para sair')
print('digite 99 para sair')
while num != 99:
    if num > 21 or num < 0:
        print('Tente novamente.')
