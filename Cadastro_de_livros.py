import os
from time import sleep

def adicionar_livro():
    os.system("cls")
    print("Carregando...")
    sleep(1.5)
    os.system("cls")

    print("-----ADICIONAR LIVRO-----\n")

    livro=[]

    titulo=input("Título: ").title()
    autor=input("Autor: ").title()
    categoria=input("Categoria: ").title()
    preco=float(input("Preço: "))

    livro.append(titulo)
    livro.append(autor)
    livro.append(categoria)
    livro.append(preco)

    livros=open("livros.txt", "a", encoding='utf-8')
    livros.write(livro[0]+";")
    livros.write(livro[1]+";")
    livros.write(livro[2]+";")
    livros.write(str(livro[3])+"\n")

    livros.close()

    print("\nLivro Adicionado!")
    sleep(1.5)

adicionar_livro()