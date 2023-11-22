import os
from time import sleep

def recomendacao():
    os.system("cls")
    cont1  = 0
    cont2  = 0
    cont3  = 0
    cont4  = 0
    cont5  = 0
    cont6  = 0
    cont7  = 0
    cont8  = 0
    cont9  = 0
    cont10 = 0
    cont11 = 0
    cont12 = 0
    cont13 = 0
    cont14 = 0
    cont15 = 0
    cont16 = 0
    cont17 = 0
    cont18 = 0
    cont19 = 0

    with open("livros.txt", "r", encoding='utf-8') as livros:
        linhas = livros.readlines()
        
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(";")

            if dados[2] == "FANTASIA":
                cont1 += 1
            if dados[2] == "FICÇÃO CIENTÍFICA":
                cont2 += 1
            if dados[2] == "DISTOPIA":
                cont3 += 1
            if dados[2] == "AÇÃO E AVENTURA":
                cont4 += 1
            if dados[2] == "FICÇÃO POLICIAL":
                cont5 += 1
            if dados[2] == "HORROR":
                cont6 += 1
            if dados[2] == "THRILLER E SUSPENSE":
                cont7 += 1
            if dados[2] == "FICÇÃO HISTÓRICA":
                cont8 += 1
            if dados[2] == "ROMANCE":
                cont9 += 1
            if dados[2] == "NOVELA":
                cont10 += 1
            if dados[2] == "FICÇÃO FEMININA":
                cont11 += 1
            if dados[2] == "LGBT":
                cont12 += 1
            if dados[2] == "FICÇÃO CONTEMPORÂNEA":
                cont13 += 1
            if dados[2] == "REALISMO MÁGICO":
                cont14 += 1
            if dados[2] == "GRAPHIC NOVEL":
                cont15 += 1
            if dados[2] == "CONTO":
                cont16 += 1
            if dados[2] == "JOVEM ADULTO":
                cont17 += 1
            if dados[2] == "NOVO ADULTO":
                cont18 += 1
            if dados[2] == "INFANTIL":
                cont19 += 1
        genero_preferido = "1"
        if cont1 < cont2:
            genero_preferido = "2"
        if cont2 < cont3:
            genero_preferido = "3"
        if cont3 < cont4:
            genero_preferido = "4"
        if cont4 < cont5:
            genero_preferido = "5"
        if cont5 < cont6:
            genero_preferido = "6"
        if cont6 < cont7:
            genero_preferido = "7"
        if cont7 < cont8:
            genero_preferido = "8"
        if cont8 < cont9:
            genero_preferido = "9"
        if cont9 < cont10:
            genero_preferido = "10"
        if cont10 < cont11:
            genero_preferido = "11"
        if cont11 < cont12:
            genero_preferido = "12"
        if cont12 < cont13:
            genero_preferido = "13"
        if cont13 < cont14:
            genero_preferido = "14"
        if cont14 < cont15:
            genero_preferido = "15"
        if cont15 < cont16:
            genero_preferido = "16"
        if cont16 < cont17:
            genero_preferido = "17"
        if cont17 < cont18:
            genero_preferido = "18"
        if cont18 < cont19:
            genero_preferido = "19"
        

        if genero_preferido == "1":
            print("Baseado nas suas leituras indicamos o livro Carmilla: A Vampira De Karnstein")
        if genero_preferido == "2":
            print("Baseado nas suas leituras indicamos o livro Duna")
        if genero_preferido == "3":
            print("Baseado nas suas leituras indicamos o livro O Conto da Aia")
        if genero_preferido == "4":
            print("Baseado nas suas leituras indicamos o livro O Guia do Mochileiro das Galáxias")
        if genero_preferido == "5":
            print("Baseado nas suas leituras indicamos o livro A espiã da realeza")
        if genero_preferido == "6":
            print("Baseado nas suas leituras indicamos o livro O chamado de Cthulhu e outros contos.")
        if genero_preferido == "7":
            print("Baseado nas suas leituras indicamos o livro O Iluminado")
        if genero_preferido == "8":
            print("Baseado nas suas leituras indicamos o livro Cronicas saxonicas: O ultimo reino")
        if genero_preferido == "9":
            print("Baseado nas suas leituras indicamos o livro Me chame pelo seu nome")
        if genero_preferido == "10":
            print("Baseado nas suas leituras indicamos o livro Orgulho e Paixão")
        if genero_preferido == "11":
            print("Baseado nas suas leituras indicamos o livro A hora da estrela")
        if genero_preferido == "12":
            print("Baseado nas suas leituras indicamos o livro Um Milhão de Finais Felizes")
        if genero_preferido == "13":
            print("Baseado nas suas leituras indicamos o livro O último sábado de julho amanhece quieto")
        if genero_preferido == "14":
            print("Baseado nas suas leituras indicamos o livro A terra inteira e o céu infinito")
        if genero_preferido == "15":
            print("Baseado nas suas leituras indicamos o livro V de vingança")
        if genero_preferido == "16":
            print("Baseado nas suas leituras indicamos o livro O filho de mil homens")
        if genero_preferido == "17":
            print("Baseado nas suas leituras indicamos o livro A Rainha Vermelha")
        if genero_preferido == "18":
            print("Baseado nas suas leituras indicamos o livro Vermelho, Branco e Sangue Azul")
        if genero_preferido == "19":
            print("Baseado nas suas leituras indicamos o livro A parte que falta")