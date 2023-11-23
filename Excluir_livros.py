from time import sleep
import Tratamento_de_Erros

def excluir_livro():

    arquivo = open('livros.txt', 'r', encoding='utf-8')
    info = arquivo.readlines()
    arquivo.close()

    for linha in range(len(info)):
        livro = info[linha].split(';')
        print(f"({linha}) {livro[0]}")

    while True:

        livro_excluido = input("Digite o número do livro que você gostaria de excluir: ")

        if Tratamento_de_Erros.numeric_confirm (livro_excluido):
            livro_excluido = int(livro_excluido)
            break
        else:
            print ('Entrada inválida, tente novamente!')

    if 0 <= livro_excluido < len(info):
        info.pop(livro_excluido)

        arquivo = open('livros.txt', 'w', encoding='utf-8')
        arquivo.writelines(info)
        arquivo.close()

        print("\nLivro excluído!")
        sleep(1.5)

    else:
        print("Número inválido. Nenhum livro foi excluído.")
