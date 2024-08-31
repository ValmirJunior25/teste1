from arquivo import *

while True:
    cabeçalho('Gerenciador de tarefas')   
    nome_lista_arquivo = modificar_nome_para_arquivo_txt(input('Nome da lista de tarefas: '))
    nome_lista = modificar_arquivo_txt_pra_nome(nome_lista_arquivo)
    print(f'\033[0;33mArquivo: \033[m\033[0;32m{nome_lista_arquivo}\033[m')
    sucesso('Lista de tarefas encontrada') if verificar_arquivo(nome_lista_arquivo) else criar_arquivo(nome_lista_arquivo)


    while verificar_arquivo(nome_lista_arquivo):
        cabeçalho(nome_lista)
        mostrar_tarefas(nome_lista_arquivo)
        print('( 1 ) - Inserir tarefas na lista.\n'
              '( 2 ) - Marcar tarefas com feita.\n'
             f'( 3 ) - Apagar lista ( {nome_lista} )\n'
             f'( 4 ) - Sair da lista ( {nome_lista} )')
        print('-='*65)
        escolha = leia_int('Opção: ')


        if escolha == 1:
            cont = None
            while True:
                adicionar_tarefas(nome_lista_arquivo, input('Adicionar nova tarefa: '))
                cont = input('Deseja adicionar mais? ').strip().lower()[0]
                if cont in 'n':
                    break
                elif cont in 's':
                    continue
                else:
                    erro('Opção invalida')

        elif escolha == 2:
            quantidade = numero_de_tarefas(nome_lista_arquivo)
            numero = leia_int('Numero da tarefa: ')
            marcar_tarefas(nome_lista_arquivo, numero)

        elif escolha == 3:
            while True:
                print(f'Deseja apagar o arquivo "{nome_lista_arquivo}" ?')
                resposta = input(' [S/N] --> ').lower()[0]
                if resposta == 's':
                    deletar_arquivo(nome_lista_arquivo)
                    break
                else:
                    break
                
        elif escolha == 4:
            break
        else:
            erro('Opção invalida')


    escolha = sair()
    if escolha:
        break
    else:
        pass
        