tarefas = []

def adicionar_tarefa():
    nome = input('nome da tarefa: ')
    descricao = input('descrição: ')
    prioridade = input('prioridade (baixa/media/alta): ')
    categoria = input('categoria: ')

    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }

    tarefas.append(tarefa)
    print('Tarefas adicionadas com sucesso!')

def listar_tarefas():
    if not tarefas:
        print('nenhuma tarefa cadastrada.')
        return

    print('=== LISTA DE TAREFAS ===')
    for i, tarefa in enumerate(tarefas):
        print(f"\nID: {i}")
        print(f"Nome: {tarefa['nome']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Categoria: {tarefa['categoria']}")
        print(f"Concluída: {tarefa['concluida']}")
    print()

def listar_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente.")
        return

    print("=== TAREFAS PENDENTES ===")
    for i, tarefa in enumerate(pendentes):
        print(f"Nome: {tarefa['nome']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Categoria: {tarefa['categoria']}")
        print(f"Concluída: {tarefa['concluida']}")
        print()

def marcar_concluida():
    listar_tarefas()

    tarefa_id = int(input("Digite o ID da tarefa concluída: "))
    tarefas[tarefa_id]["concluida"] = True
    print("Tarefa marcada como concluída!")

def listar_por_prioridade():
    prioridade = input('prioridade (baixa/media/alta): ')
    print(f'tarefas com prioridade {prioridade}:')

    for t in tarefas:
        if t["prioridade"] == prioridade:
            print(t['nome'])

    print()

def listar_por_categoria():
    categoria = input('categoria: ')
    print(f'tarefas na categoria {categoria}:')

    for t in tarefas:
        if t["categoria"] == categoria:
            print(t['nome'])
    
    print()

while True:
        print("\n========== GERENCIADOR DE TAREFAS ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Listar tarefas pendentes")
        print("4 - Marcar tarefa como concluída")
        print("5 - Listar por prioridade")
        print("6 - Listar por categoria")
        print("0 - Sair")
        print("=============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando o programa...")
            break
        elif opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            listar_pendentes()
        elif opcao == '4':
            marcar_concluida()
        elif opcao == '5':
            listar_por_prioridade()
        elif opcao == '6':
            listar_por_categoria()
        else:
            print("Opção inválida! Tente novamente.\n")