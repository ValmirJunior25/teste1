import ferramentas


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[0;31mERRO na criação do arquivo!\033[m')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[0;31mERRO ao ler o arquivo!\033[m')
    else:
        ferramentas.cabeçalho('PESSOAS CADASTRADAS')
        print(f'{ 'Nome ':<35}{'Idade'}')
        print('-'*40)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<37}{dado[1]:>3}')
        print('-'*40)
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'\033[0;31mERRO na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[0;31mERRO na passagem de dados para o arquivo.\033[m')
        else:
            print('-'*40)
            print(f'\033[0;33mCadastro de {nome} feito com sucesso.\033[m')
            print('-'*40)
            a.close
