num_inicio = int(input('Digite o numero de inicio: '))
num_fim = int(input('Digite o numero de fim: '))
soma = 0

for i in range(num_inicio,  num_fim + 1, 1):

    if i % 2 == 1:
        continue
    elif i % 2 == 0:
        soma = soma + i
    else:
        print('nao ha numeros pares')

    print (i)

print (f'a soma dos numeros pares é: {soma}')