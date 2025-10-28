qtd_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(qtd_alunos):
    print(f" Aluno {i + 1}")
    nome = input("Nome do aluno: ")

    notas = []
    for j in range(3):
        nota = float(input(f"Digite a {j + 1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / 3

    soma_medias += media

    if media >= 7.0:
        situacao = "Aprovado ✅"
    else:
        situacao = "Reprovado ❌"

    print(" Resultado ")
    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

media_geral = soma_medias / qtd_alunos
print(f"Média geral da turma: {media_geral:.2f}")