def library_confirm ():
    try:
        file = open('livros.txt', 'r', encoding='utf-8')
    except:
        FileNotFoundError
        return False
    else:
        return True
    
def numeric_confirm (valor):
    try:
        float(valor)
    except:
        ValueError
        return False
    if float(valor) < 0:
        return False
    else:
        return True
