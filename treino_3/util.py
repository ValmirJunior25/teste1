

def erro(txt):
    print(f'\n\033[0;31mERRO! {txt}\033[m'.center(140), '\n')


def sucesso(txt):
    print(f'\033[0;33m{txt}\033[m'.center(140), '\n')
    

def cabeçalho(txt):
    print('='*140,'\n')
    print(f'\033[0;32m{txt}\033[m'.center(140), '\n')
    print('='*140,'\n')


def leia_int(txt):
    n = txt.isnumeric()
    if n == True:
        return int(txt)
    else:
        return txt


def modificar_nome_para_arquivo_txt(nome_do_arquivo):
    nome = nome_do_arquivo.strip().replace(' ', '_')
    return nome + '.txt'


def modificar_arquivo_txt_pra_nome(nome_do_arquivo):
    nome = nome_do_arquivo.strip().replace('_', ' ')
    return nome.replace('.txt', '')
