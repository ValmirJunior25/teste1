from ferramentas import *
from arquivo import *


nome_arquivo = ' '

while True:
    cabeçalho('Escolha uma opção para salvar os dados.')
    print('1 - Arquivo já existe.\n'
          '2 - Criar um novo arquivo.\n')
    escolha = leia_int(input('Opção: ').strip())
    if escolha == 1:
        while True:
            nome = (input('Nome do arquivo: ').strip().replace(' ', '_')+ '.txt')
            if verificar_arquivo(nome):
                nome_arquivo = nome
                break
            else:
                erro('Esse arquivo não existe.')
                break
    elif escolha == 2:
        while True:
            nome = (input('Nome do arquivo: ').strip().replace(' ', '_')+ '.txt')
            if continuar(input(f'Deseja usar "\033[0;33m{nome}"\033[m como o nome do arquivo? ').strip().lower()[0]):
                criar_arquivo(nome)
                nome_arquivo = nome
                break
            else:
                cabeçalho('Digite outro nome')
    if len(nome_arquivo) > 4:
        print(f'Arquivo: \033[0;32m{nome_arquivo}\033[m')
        break


while True:
    cabeçalho('MENU')
    print('1 - Mostrar lista de pessoas\n'
          '2 - Cadastrar\n'
          '3 - Finalizar')

    escolha = leia_int(input('Opção: ').strip())
    if escolha == 1:
        ler_arquivo(nome_arquivo)
    elif escolha == 2:
        while True:
            cadastrar(nome_arquivo,
                      input('Nome: '),
                      input('Idade: '),
                      input('Sexo: '),
                      input('Ciade: '))
            if continuar(input(f'Deseja continuar cadastrando? ').strip().lower()[0]):
                continue
            else:
                break
    elif escolha == 3:
        print('fanalizando')
        break
    else:
        erro('Opção invalida')

