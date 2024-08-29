
def sair():
    print('-'*100)
    print('Digite "Esc" para sair.\n'
          'E pressione "Enter" para continuar.')
    print('-'*100)
    escolha = input('--> ').strip().lower()
    if escolha == 'esc':
        return True           # Sair
    elif escolha == '':
        return False          # Continua
    else:
        erro('Escolha invalida')
        sair()


def erro(txt):
    print('~'*100)
    print(f'\031[0;33mERRO! {txt}\033[m')
    print('~'*100)


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 - n2