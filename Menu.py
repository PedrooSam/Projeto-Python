import Cadastro_de_livros
import Atualizar_livros
import Visualizar_livros
import Funcoes

while True:

    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Excluir Livro")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        Cadastro_de_livros.adicionar_livro()
    elif escolha == "2":
        print("\nEscolha o tipo de categoria:")
        print("Geral [0]")
        print("Categoria [1]")
        print("Autor [2]")
        
        tipo_view = input("Digite o número da opção desejada: ")

        if tipo_view == '0':
            print(Visualizar_livros.visualizacao_geral())
        elif tipo_view == '1':
            categoria = input("Digite a categoria desejada: ")
            print(Visualizar_livros.visualizacao_por_categoria(categoria))
        elif tipo_view == '2':
            autor = input("Digite o autor desejado: ")
            print(Visualizar_livros.visualizacao_por_autor(autor))
    
    elif escolha == "3":
        Atualizar_livros.atualizar_livro()
    elif escolha == "4":
        Funcoes.excluir_livro()
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
