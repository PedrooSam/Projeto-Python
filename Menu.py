import Cadastro_de_livros
import Atualizar_livros
import Visualizar_livros
import Excluir_livros
import Tratamento_de_Erros
import Recomendacao
from time import sleep

while True:


    print("-----MENU-----\n")
    print("1. Adicionar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Excluir Livro")
    print ("5. Recomendação")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        Cadastro_de_livros.adicionar_livro()

    elif escolha == "2":
        if Tratamento_de_Erros.library_confirm():
                
                while True:
                    print("-----VIZUALIZAR-----")
                    print("\nEscolha o tipo de categoria:")
                    print("Geral [0]")
                    print("Categoria [1]")
                    print("Autor [2]")
                    
                    tipo_view = input("Digite o número da opção desejada: ")


                    if tipo_view == '0':
                        Visualizar_livros.visualizacao_geral()
                        voltar = str(input('Clique "Enter" para voltar.'))

                        break

                    elif tipo_view == '1':
                        print("- Fantasia\n- Ficção Científica\n- Distopia\n- Ação e Aventura\n- Ficção Policial\n- Horror\n- Thriller e Suspense\n- Ficção Histórica\n- Romance\n- Novela\n- Ficção Feminina\n- LGBT\n- Ficção Comtemporânea\n- Realismo Mágico\n- Graphic Novel\n- Conto\n- Jovem Adulto\n- Novo Adulto\n- Infantil")
                        categoria = input("Digite a categoria desejada: ").upper()
                        Visualizar_livros.visualizacao_por_categoria(categoria)
                        voltar = str(input('Clique "Enter" para voltar.'))

                        break

                    elif tipo_view == '2':
                        autor = input("Digite o autor desejado: ")
                        Visualizar_livros.visualizacao_por_autor(autor)
                        voltar = str(input('Clique "Enter" para voltar.'))

                        break

                    else:
                        print ('Escolha uma opção válida!')
                        continue

        else:
            print ('Ainda não há livros cadastrados!')
            continue
    
    elif escolha == "3":

        if Tratamento_de_Erros.library_confirm():
            Atualizar_livros.atualizar_livro()

        else:
            print ('Ainda não há livros cadastrados!')
            continue

    elif escolha == "4":

        if Tratamento_de_Erros.library_confirm():
            Excluir_livros.excluir_livro()

        else:
            print ('Ainda não há livros cadastrados')
            continue
    
    elif escolha == '5':

        if Tratamento_de_Erros.library_confirm():
            Recomendacao.recomendacao()
            voltar = str(input('Clique "Enter" para voltar.'))
            
        else:
            print ('Ainda não há livros cadastrados')

    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        sleep(1.5)
        break

    else:
        print("Opção inválida. Tente novamente.")
