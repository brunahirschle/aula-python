def maior_numero(*kwargs):
    maior = 0
    # menor = 99999999999999

    for i in range(3):
        num = int(input('digite um numero: '))

        if num > maior:
            maior = num

        
        # if num < menor:
        #     menor = num
        
    print(f'o maior numero é {maior}')
    # print(f'o menor numero é {menor}')

maior_numero()


