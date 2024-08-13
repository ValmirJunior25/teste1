import ferramentas
import arquivo

arq = 'lista_de_pessoas.txt'

if not arquivo.arquivo_existe(arq):
    arquivo.criar_arquivo(arq)


while True:
    escolha = ferramentas.menu(['Lista de cadastrados','Cadastrar pessoa','Sair do programa'])
    if escolha == 1:
        arquivo.ler_arquivo(arq)
    elif escolha == 2:
        ferramentas.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = ferramentas.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif escolha == 3:
        print('FINALIZANDO...')
        break
    else:
        print('\033[0;31mERRO! Opção invalida.\033[m')

