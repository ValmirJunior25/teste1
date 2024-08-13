from time import sleep


def leiaint(msg):
    while True:
        try:
            esc = int(input(msg))
        except:
            print('\033[0;31mERRO! Opção invalida.\033[m')
            print('')
            sleep(1)
        else:
            return esc
        
        
def cabeçalho(nome):
    print('')
    print('='*40)
    print(f'\033[0;32m{nome.center(40)}\033[m')
    print('='*40)


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('='*40)
    escolha = leiaint('Digite sua escolha: ')
    return escolha

