import ferramentas


while True:
    print('')
    print('='*40)
    print(f'\033[0;32m{'MENU PRINCIPAL':^40}\033[m')
    print('='*40)
    print('1 - Ver pessoas cadastradas.\n'
        '2 - Cadastrar uma pessoa.\n'
        '3 - Sair do sistema.')
    print('-'*40)
    print('')


    escolha = ferramentas.escolha_valida('Qual é a sua escolha? ')


    if escolha == 1:
        ferramentas.mostra_lista() 
    
    elif escolha == 2:
        ferramentas.add_lista()

    elif escolha == 3:
        print('='*40)
        print(f'{'FINALIZANDO...':^40}')
        print('='*40)
        break
