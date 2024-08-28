from time import sleep

def escolha_valida(msg):
    while True:
        try:
            esc = int(input(msg))
            if esc != 1 and esc != 2 and esc != 3:
                print('\033[0;31mERRO! Opção invalida.\033[m')
                print('')
                sleep(1)
                continue
        except:
            print('\033[0;31mERRO! Opção invalida.\033[m')
            print('')
            sleep(1)
        else:
            return esc
        

def mostra_lista():
    if len(pessoas_cadastradas) == 0:
        print('-='*20)
        print('\033[0;33mNão a nenhuma pessoa cadastrada.\033[m')
        print('-='*20)
        print('')
        sleep(1)
    else:
        print('')
        print('-='*20)
        print(f'{ 'Nome ':<35}{'Idade'}')
        print('-='*20)
        for pessoa in pessoas_cadastradas:
            print(f'{pessoa[0]:<35}{pessoa[1]:>5}')
            sleep(0.3)
        print('-'*40)
        print('')
        sleep(1)
        
           
    
def add_lista():
    print('')
    print('-='*20)
    pessoa = []
    while True:
        try:
            nome = str(input('Nome: ')).strip().title()
        except:
             print('\033[0;31mERRO! Dado invalido.\033[m')
             continue
        else:
            pessoa.append(nome)
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
             print('\033[0;31mERRO! Dado invalido.\033[m')
             continue
        else:
            pessoa.append(idade)
            break
    pessoas_cadastradas.append(pessoa[:])
    pessoa.clear()
    sleep(1)
    print('-='*20)
    print('\033[0;33mCadastro bem sucedido.\033[m')
    print('-='*20)
    print('')
    sleep(1)


pessoas_cadastradas = []
