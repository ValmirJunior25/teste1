from ferramentas import *
from arquivo import *


nome_arquivo = ' '

while True:
    cabeçalho('Escolha uma opção para salvar os dados.')
    print('1 - Arquivo já existente.\n'
          '2 - Criar um novo arquivo.\n')
    escolha = leia_int(input('Opção: ').strip())
    if escolha == 1:
        while True:
            nome = (input('Nome do arquivo: ').strip().replace(' ', '_')+ '.txt')
            if verificar_arquivo(nome):
                nome_arquivo = nome
                print('\033[0;33mArquivo encontrado: \033[m', end='')
                break
            else:
                erro('Esse arquivo não existe.')
                break
    elif escolha == 2:
        while True:
            nome = (input('Nome do arquivo: ').strip().replace(' ', '_')+ '.txt')
            if continuar(f'Deseja usar "\033[0;33m{nome}\033[m" como o nome do arquivo?'):
                criar_arquivo(nome)
                nome_arquivo = nome
                print('\033[0;33mNome do arquivo: \033[m', end='')
                break
            else:
                cabeçalho('Digite outro nome')
    else:
        erro('Opção invalida')
        
    if len(nome_arquivo) > 4:
        print(f'\033[0;32m{nome_arquivo}\033[m')
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
                      input('Nome: ').strip(),
                      input('Idade: ').strip(),
                      input('Sexo: ').strip(),
                      input('Ciade: ').strip())
            if continuar('Deseja continar cadastrando?'):
                continue
            else:
                break
    elif escolha == 3:
        print('fanalizando')
        break
    else:
        erro('Opção invalida')

