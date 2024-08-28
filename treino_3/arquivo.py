from util import *


def verificar_arquivo(nome_do_arquivo):
    try:
        arquivo = open(nome_do_arquivo, 'rt')
        arquivo.close()
    except:
        return False
    else:
        return True
    

def criar_arquivo(nome_do_arquivo):
    try:
        arquivo = open(nome_do_arquivo, 'wt+')
        arquivo.close()
    except:
        erro('Na criação do arquivo.')
    else:
        sucesso('Arquivo criado com sucesso.')


def adicionar_tarefas(nome_do_arquivo, tarefa):
    try:
        arquivo = open(nome_do_arquivo, 'at')
    except:
        erro('Ao escrever o arquivo.')
    else:
        try:
            arquivo.write(f'{tarefa}\n')
        except:
            erro('Ao escrever na lista de tarefas.')
    finally:
        arquivo.close()


def mostrar_tarefas(nome_do_arquivo):
    try:
        arquivo = open(nome_do_arquivo, 'rt')
    except:
        erro('Ao abrir o arquivo para exibir a lista de tarefas')
    else:
        try:
            print('-'*140)
            cont = 0
            for tarefa in arquivo:
                cont += 1
                print(f'[ {cont} ] - {tarefa}')
            print('-'*140)
           
        except:
            erro('Ao exibir a lista de tarefas')
    finally:
        arquivo.close()


def numero_de_tarefas(nome_do_arquivo):
    try:
        arquivo = open(nome_do_arquivo, 'rt')
    except:
        erro('Ao abrir o arquivo para contar o número de tarefas')
    else:
        try:
            cont = 0
            for tarefa in arquivo:
                cont += 1
        except:
            erro('Ao contar o número de tarefas')
    finally:
        arquivo.close()
        return cont


def marcar_tarefas(nome_do_arquivo, num_da_tarefa):
    pass
