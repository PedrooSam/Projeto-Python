import os
from time import sleep

def atualizar_livro():
    os.system("cls")
    print("-----ATUALIZAR LIVRO-----\n")

    titulo_atualizar = input("Digite o título do livro que deseja atualizar: ").title()

    with open("livros.txt", "r", encoding='utf-8') as livros:
        linhas = livros.readlines()

    encontrado = False
    for i, linha in enumerate(linhas):
        dados = linha.strip().split(";")
        if dados[0] == titulo_atualizar:
            encontrado = True
            print(f"\nLivro encontrado: {dados[0]} - {dados[1]} - {dados[2]} - R${dados[3]}")
            
            novo_titulo = input("Novo Título: ").title()
            novo_autor = input("Novo Autor: ").title()
            nova_categoria = input("Nova Categoria: ").title()
            novo_preco = float(input("Novo Preço: "))

            linhas[i] = f"{novo_titulo};{novo_autor};{nova_categoria};{novo_preco}\n"

            print("\nLivro Atualizado!")
            sleep(1.5)
            break

    if not encontrado:
        print("\nLivro não encontrado. Verifique o título e tente novamente.")
        sleep(2)

    with open("livros.txt", "w", encoding='utf-8') as livros:
        livros.writelines(linhas)
