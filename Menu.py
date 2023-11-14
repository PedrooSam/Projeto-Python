livros = {}

def adicionar_livro():
    livro_id = input("Digite o ID do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")

    livros[livro_id] = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }
    print(f'O livro "{titulo}" foi adicionado com sucesso!')

def visualizar_livros():
    print("Lista de Livros:")
    for livro_id, livro_info in livros.items():
        print(f"ID: {livro_id}, Título: {livro_info['titulo']}, Autor: {livro_info['autor']}, Ano: {livro_info['ano']}")

def atualizar_livro():
    livro_id = input("Digite o ID do livro que deseja atualizar: ")
    if livro_id in livros:
        print(f"Atualizando livro {livros[livro_id]['titulo']}:")
        novo_titulo = input("Novo título (deixe em branco para manter o atual): ")
        novo_autor = input("Novo autor (deixe em branco para manter o atual): ")
        novo_ano = input("Novo ano de publicação (deixe em branco para manter o atual): ")

        if novo_titulo:
            livros[livro_id]['titulo'] = novo_titulo
        if novo_autor:
            livros[livro_id]['autor'] = novo_autor
        if novo_ano:
            livros[livro_id]['ano'] = novo_ano

        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.")

def excluir_livro():
    livro_id = input("Digite o ID do livro que deseja excluir: ")
    if livro_id in livros:
        titulo = livros[livro_id]['titulo']
        del livros[livro_id]
        print(f'O livro "{titulo}" foi excluído com sucesso!')
    else:
        print("Livro não encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Excluir Livro")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        adicionar_livro()
    elif escolha == "2":
        visualizar_livros()
    elif escolha == "3":
        atualizar_livro()
    elif escolha == "4":
        excluir_livro()
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
