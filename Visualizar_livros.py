def visualizacao_geral ():
    arquivo = open('livros.txt', 'r', encoding='utf-8')

    info = arquivo.readlines()

    arquivo.close()

    livros = []
    quant_livros = 0
    total_gasto = 0

    for linha in range (len(info)):
        livro = info[linha]
        livro = livro.split(';')

        valor = float(livro[3])

        livro = f'''_______________________________________________________________________________

Livro: {livro[0]}

Autor: {livro[1]}
Categoria: {livro[2]}
Valor: R${livro[3]}'''

        quant_livros += 1
        total_gasto += valor
        livros.append(livro)
    
    print (f'''_______________________________________________________________________________

Total de livros cadastrados: {quant_livros}    Total gasto: R${total_gasto :.2f}''')

    for c in range (len(livros)):
        print (livros[c])
    
    livros = []
    return ''


#=======================================================================================================================================


def visualizacao_por_categoria (categoria):
        arquivo = open('livros.txt', 'r', encoding='utf-8')

        info = arquivo.readlines()

        arquivo.close()

        livros = []
        quant_livros = 0
        total_gasto = 0

        for linha in range (len(info)):
            livro = info[linha]
            livro = livro.split(';')

            if livro[2] == categoria:
                valor = float(livro[3])

                livro = f'''_______________________________________________________________________________

Livro: {livro[0]}

Autor: {livro[1]}
Categoria: {livro[2]}
Valor: R${livro[3]}'''
                
                quant_livros += 1
                total_gasto += valor
                livros.append(livro)

        if livros != []:

            print (f'''_______________________________________________________________________________

Nº de livros encontrados na categoria: {quant_livros}    Total gasto na categoria: R${total_gasto :.2f}''')

            for c in range (len(livros)):
                print (livros[c])
        else:
            print ('Não há livros cadastrados nessa categoria!')
        return ''
      

#=======================================================================================================================================


def visualizacao_por_autor (autor):
        arquivo = open('livros.txt', 'r', encoding='utf-8')

        info = arquivo.readlines()

        arquivo.close()

        livros = []
        quant_livros = 0
        total_gasto = 0

        for linha in range (len(info)):
            livro = info[linha]
            livro = livro.split(';')

            if livro[1] == autor:
                valor = float(livro[3])

                livro = f'''_______________________________________________________________________________

Livro: {livro[0]}

Autor: {livro[1]}
Categoria: {livro[2]}
Valor: R${livro[3]}'''
                

                quant_livros += 1
                total_gasto += valor
                livros.append(livro)

        if livros != []:

            print (f'''_______________________________________________________________________________

Nº de livros encontrados do autor: {quant_livros}    Total gasto com o autor: R${total_gasto :.2f}''')

            for c in range (len(livros)):
                print (livros[c])
        else:
            print ('Não há livros cadastrados nessa autoria!')
        return ''
