

def erro(txt):
    print(f'\n\033[0;31mERRO! {txt}\033[m'.center(130), '\n')


def sucesso(txt):
    print(f'\033[0;33m{txt}\033[m'.center(130), '\n')
    

def cabeçalho(txt):
    print('='*130,'\n')
    print(f'\033[0;32m{txt}\033[m'.center(130), '\n')
    print('='*130,'\n')


def leia_int(finalidade_do_numero):
    txt = input(finalidade_do_numero)
    num = txt.isnumeric()
    if num:
        return int(txt)
    else:
        erro('Digite um numero.')
        leia_int(finalidade_do_numero)


def modificar_nome_para_arquivo_txt(nome_do_arquivo):
    nome = nome_do_arquivo.strip().replace(' ', '_')
    return nome + '.txt'


def modificar_arquivo_txt_pra_nome(nome_do_arquivo):
    nome = nome_do_arquivo.strip().replace('_', ' ')
    return nome.replace('.txt', '')


def sair():
    print('-'*130)
    print('Pressione "Enter" para reiniciar.\n'
          'Digite "Esc" para sair.')
    print('-'*130)
    escolha = input('--> ').strip().lower()
    if escolha == 'esc':
        return True           # Sair
    elif escolha == '':
        return False          # Continua
    else:
        erro('Escolha invalida')
        sair()