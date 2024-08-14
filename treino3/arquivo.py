from ferramentas import *

def criar_arquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        erro('Na criação do arquivo.')
    else:
        print('\033[0;33mArquivo criado com sucesso.\033[m')
    

def verificar_arquivo(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def cadastrar(arq, nome='desconhecido', idade=0 , sexo='não informado', cidade='desconhecido'):
    try:
        arquivo = open(arq, 'wt')
    except:
        erro('No cadastro.')
    else:
        try:
            arquivo.write(f'{nome};{idade};{sexo};{cidade}\n')
        except:
            erro('Na passagem de dados para o arquivo')
        else:
            confirmação(f'Cadastro de {nome} feito com susesso.')   
            arquivo.close


def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        erro('Na leitura do arquivo.')
    else:
        nome.replace('_', ' ')
        nome.replace('.txt', '.')
        cabeçalho(nome)
        print(f'{'NOME':^70}{'IDADE':^10}{'SEXO':^10}{'CIDADE':^50}')
        for item in arquivo:
            print(f'{item} - {arquivo[item]}')


