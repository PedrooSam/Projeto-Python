livro=[]

titulo=input("Título: ").title()
autor=input("Autor: ").title()
categoria=input("Categoria: ").title()
preco=float(input("Preço: "))

livro.append(titulo)
livro.append(autor)
livro.append(categoria)
livro.append(preco)

livros=open("livros.txt", "a")
livros.write(livro[0]+"\n")
livros.write(livro[1]+"\n")
livros.write(livro[2]+"\n")
livros.write(str(livro[3])+"\n")
livros.close()

