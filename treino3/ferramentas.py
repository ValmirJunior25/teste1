

def cabeçalho(txt):
    print('='*140,'\n')
    print(f'\033[0;32m{txt}\033[m'.center(140),'\n')
    print('='*140,'\n')


def erro(descrição):
    print('='*140,'\n')
    print(f'\033[0;31mERRO! {descrição}\033[m'.center(140),'\n')
    print('='*140,'\n')


def confirmação(txt):
    print('='*140,'\n')
    print(f'\033[0;33m{txt}\033[m'.center(140),'\n')
    print('='*140,'\n')


def leia_int(txt):
    n = txt.isnumeric()
    if n == True:
        return int(txt)
    else:
        return txt
    
def continuar(txt):
    if txt in 's':
        return True
    else:
        return False
