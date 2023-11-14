from Pedro import adicionar_livro
from Pedro import visualizar_livros
from Pedro import atualizar_livro
from Pedro import excluir_livro

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
