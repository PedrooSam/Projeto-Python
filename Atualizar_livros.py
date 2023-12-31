import os
import Tratamento_de_Erros
from time import sleep


def atualizar_livro():

    print("-----ATUALIZAR LIVRO-----\n")

    arquivo = open('livros.txt', 'r', encoding='utf-8')
    info = arquivo.readlines()
    arquivo.close()

    for linha in range(len(info)):
        livro = info[linha].split(';')
        print(f"- {livro[0]}")

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

            print("1. Fantasia\n2. Ficção Científica\n3. Distopia\n4. Ação e Aventura\n5. Ficção Policial\n6. Horror\n7. Thriller e Suspense\n8. Ficção Histórica\n9. Romance\n10. Novela\n11. Ficção Feminina\n12. LGBT\n13. Ficção Comtemporânea\n14. Realismo Mágico\n15. Graphic Novel\n16. Conto\n17. Jovem Adulto\n18. Novo Adulto\n19. Infantil")
            
            while True:

                categoria = input("Categoria (número entre 1 e 19): ")

                if categoria.isdigit() and 1 <= int(categoria) <= 19:

                    if categoria == '1':
                        nova_categoria ="FANTASIA"
                        break

                    if categoria == '2':
                        nova_categoria =("FICÇÃO CIENTÍFICA")
                        break

                    if categoria == '3':
                        nova_categoria =("DISTOPIA")
                        break

                    if categoria == '4':
                        nova_categoria =("AÇÃO E AVENTURA")
                        break

                    if categoria == '5':
                        nova_categoria =("FICÇÃO POLICIAL")
                        break

                    if categoria == '6':
                        nova_categoria =("HORROR")
                        break

                    if categoria == '7':
                        nova_categoria =("THRILLER E SUSPENSE")
                        break

                    if categoria == '8':
                        nova_categoria =("FICÇÃO HISTÓRICA")
                        break

                    if categoria == '9':
                        nova_categoria =("ROMANCE")
                        break

                    if categoria == '10':
                        nova_categoria =("NOVELA")
                        break

                    if categoria == '11':
                        nova_categoria =("FICÇÃO FEMININA")
                        break

                    if categoria == '12':
                        nova_categoria =("LGBT")
                        break

                    if categoria == '13':
                        nova_categoria =("FICÇÃO CONTEMPORÂNEA")
                        break

                    if categoria == '14':
                        nova_categoria =("REALISMO MÁGICO")
                        break

                    if categoria == '15':
                        nova_categoria =("GRAPHIC NOVEL")
                        break

                    if categoria == '16':
                        nova_categoria =("CONTO")
                        break

                    if categoria == '17':
                        nova_categoria =("JOVEM ADULTO")
                        break

                    if categoria == '18':
                        nova_categoria =("NOVO ADULTO")
                        break

                    if categoria == '19':
                        nova_categoria =("INFANTIL")
                        break

                else:
                    print("Entrada inválida. Tente novamente.")

            
            while True:
                
                novo_preco = input("Novo Preço: ")

                if Tratamento_de_Erros.numeric_confirm(novo_preco):
                    novo_preco = float(novo_preco)
                    break
                
                else:
                    print ('Digite um preço válido!')
                    continue

            linhas[i] = f"{novo_titulo};{novo_autor};{nova_categoria};{novo_preco}\n"

            print("\nLivro Atualizado!")
            sleep(1.5)
            break

    if not encontrado:
        print("\nLivro não encontrado. Verifique o título e tente novamente.")
        sleep(2)

    with open("livros.txt", "w", encoding='utf-8') as livros:
        livros.writelines(linhas)
