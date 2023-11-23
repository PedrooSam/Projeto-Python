from time import sleep

def excluir_livro():

    arquivo = open('livros.txt', 'r', encoding='utf-8')
    info = arquivo.readlines()
    arquivo.close()

    for linha in range(len(info)):
        livro = info[linha].split(';')
        print(f"({linha}) {livro[0]}")

    livro_excluido = int(input("Digite o número do livro que você gostaria de excluir: "))

    if 0 <= livro_excluido < len(info):
        info.pop(livro_excluido)

        arquivo = open('livros.txt', 'w', encoding='utf-8')
        arquivo.writelines(info)
        arquivo.close()

        print("\nLivro excluído!")
        sleep(1.5)

    else:
        print("Número inválido. Nenhum livro foi excluído.")
