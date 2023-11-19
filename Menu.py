import Cadastro_de_livros
import Atualizar_livros
import Funcoes
import os

while True:
    os.system('cls') 

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
        Funcoes.visualizar_livros()
    elif escolha == "3":
        Atualizar_livros.atualizar_livro()
    elif escolha == "4":
        Funcoes.excluir_livro()
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
