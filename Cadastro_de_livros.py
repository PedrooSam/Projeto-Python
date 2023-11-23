import Tratamento_de_Erros
from time import sleep

def adicionar_livro():
    print("-----ADICIONAR LIVRO-----\n")

    livro=[]

    livro.append(input("Título: ").title())
    livro.append(input("Autor: ").title())

    print("1. Fantasia\n2. Ficção Científica\n3. Distopia\n4. Ação e Aventura\n5. Ficção Policial\n6. Horror\n7. Thriller e Suspense\n8. Ficção Histórica\n9. Romance\n10. Novela\n11. Ficção Feminina\n12. LGBT\n13. Ficção Comtemporânea\n14. Realismo Mágico\n15. Graphic Novel\n16. Conto\n17. Jovem Adulto\n18. Novo Adulto\n19. Infantil")
    
    while True:

        categoria = input("Categoria (número entre 1 e 19): ")

        if categoria.isdigit() and 1 <= int(categoria) <= 19:

            if categoria == '1':
                livro.append("FANTASIA")
                break

            if categoria == '2':
                livro.append("FICÇÃO CIENTÍFICA")
                break

            if categoria == '3':
                livro.append("DISTOPIA")
                break

            if categoria == '4':
                livro.append("AÇÃO E AVENTURA")
                break

            if categoria == '5':
                livro.append("FICÇÃO POLICIAL")
                break

            if categoria == '6':
                livro.append("HORROR")
                break

            if categoria == '7':
                livro.append("THRILLER E SUSPENSE")
                break

            if categoria == '8':
                livro.append("FICÇÃO HISTÓRICA")
                break

            if categoria == '9':
                livro.append("ROMANCE")
                break

            if categoria == '10':
                livro.append("NOVELA")
                break

            if categoria == '11':
                livro.append("FICÇÃO FEMININA")
                break

            if categoria == '12':
                livro.append("LGBT")
                break

            if categoria == '13':
                livro.append("FICÇÃO CONTEMPORÂNEA")
                break

            if categoria == '14':
                livro.append("REALISMO MÁGICO")
                break

            if categoria == '15':
                livro.append("GRAPHIC NOVEL")
                break

            if categoria == '16':
                livro.append("CONTO")
                break

            if categoria == '17':
                livro.append("JOVEM ADULTO")
                break

            if categoria == '18':
                livro.append("NOVO ADULTO")
                break

            if categoria == '19':
                livro.append("INFANTIL")
                break

        else:
            print("Entrada inválida. Tente novamente.")
    
    while True:
    
        preco = input('Preço: ')

        if Tratamento_de_Erros.numeric_confirm(preco):
            livro.append(float(preco))
            break

        else:
            print ('Insira um preço válido!')
            continue

    livro[3]="{:.2f}".format(livro[3])

    livros2=livre=";".join(livro)

    livros=open("livros.txt", "a", encoding='utf-8')
    livros.write(livre+"\n")
    livros.close()

    print("\nLivro Adicionado!")
    sleep(1.5)
