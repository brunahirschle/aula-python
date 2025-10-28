usuario = ''
senha = ''
tentativas = 3

while tentativas >= 1:
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha: ')
    tentativas -= 1

    if usuario != 'Bruna' and senha != '1234':
        print(f'erro, restam {tentativas} tentativas')

    if usuario == 'Bruna' and senha == '1234':
        print('Boas-vindas!')
        break
    
    if tentativas <= 0:
        print('acesso bloqueado')
        print('acesso bloqueado')
        print('acesso bloqueado')