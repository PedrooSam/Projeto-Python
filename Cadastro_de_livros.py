import os
from time import sleep

def adicionar_livro():
    os.system("cls")
    print("Carregando...")
    sleep(1.5)
    os.system("cls")

    print("-----ADICIONAR LIVRO-----\n")

    livro=[]

    livro.append(input("Título: ").title())
    livro.append(input("Autor: ").title())
    livro.append(input("Categoria: ").title())
    livro.append(float(input("Preço: ")))

    livro[3]="{:.2f}".format(livro[3])

    livros2=livre=";".join(livro)

    livros=open("livros.txt", "a", encoding='utf-8')
    livros.write(livre+"\n")
    livros.close()

    print("\nLivro Adicionado!")
    sleep(1.5)
