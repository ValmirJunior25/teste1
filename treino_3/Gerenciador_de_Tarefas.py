from arquivo import *

while True:
    cabeçalho('Gerenciador de tarefas')   
    nome_lista_txt = modificar_nome_para_arquivo_txt(input('Nome da lista de tarefas: '))
    nome_lista = modificar_arquivo_txt_pra_nome(nome_lista_txt)
    print(f'\033[0;33mArquivo: \033[m\033[0;32m{nome_lista_txt}\033[m')
    sucesso('Lista de tarefas encontrada') if verificar_arquivo(nome_lista_txt) else criar_arquivo(nome_lista_txt)


    while True:
        cabeçalho(nome_lista)
        mostrar_tarefas(nome_lista_txt)
        print('( 1 ) - Inserir tarefas na lista.\n'
              '( 2 ) - Marcar tarefas com feita.\n'
            f'( 3 ) - Sair da lista ( {nome_lista} )')
        print('-='*70)
        escolha = leia_int(input('digite aqui: ').strip())


        if escolha == 1:
            cont = None
            while True:
                adicionar_tarefas(nome_lista_txt, input('Adicionar nova tarefa: '))
                cont = input('Deseja adicionar mais? ').strip().lower()[0]
                if cont in 'n':
                    break
                elif cont in 's':
                    continue
                else:
                    erro('Opção invalida')

        elif escolha == 2:
            quantidade = numero_de_tarefas(nome_lista_txt)
            while True:
                numero = input('Número da tarefa concluída: ')
                if leia_int(numero):
                    break
                else:
                    erro('Opção invalida')
            marcar_tarefas(nome_lista_txt, numero)

        elif escolha == 3:
            break
        else:
            erro('Opção invalida')


    desejo = None
    while desejo not in [1, 2]:
        print('-='*70)
        print('( 1 ) - Selecionar outra lista de tarefas.\n'
            '( 2 ) - Sair do aplicativo.')
        print('-='*70)
        desejo = leia_int(input('Digite aqui: ').strip())
        if desejo not in [1, 2]:
            erro('Opção invalida')
    if desejo == 1:
        continue
    elif desejo == 2:
        print('Aplicativo finalizando')
        break 
        