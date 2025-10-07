numero = ''
tentativas = 0

while tentativas < 3:
    numero = int(input('Digite um numero: '))
    tentativas += 1
    # print(tentativas)
    if numero == 7 and tentativas < 3:
        print('Parabens! voce adivinhou!')
        break
    elif numero != 7 and tentativas < 3:
        print('Tente novamente')
    else:
        print('Tentativas esgotadas!')