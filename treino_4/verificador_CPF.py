from os import system
# 746.822.891-70   - invalido 
# 111.111.111-11   - invalido
# 112.528.860-47   - valido   ( https://www.4devs.com.br/gerador_de_cpf ) - para gerar CPF 

while True:
    system('cls')

    print('='*40)
    print('Verificador de CPF'.center(40))
    print('='*40)
    cpf = input('CPF: ').strip().replace('.', '').replace('-', '')
    nove_digitos = cpf[:9]
    verificador = cpf[9:]
    
    if cpf == cpf[0] * len(cpf):
        print('-'*40)
        print('CPF invalido!'.center(40))
    else:       
        soma_1 = 0
        contador_1 = 10
        for i in nove_digitos:
            soma_1 += (int(i) * contador_1)
            contador_1 -= 1
        primeiro_digito = ((soma_1 * 10) % 11) if ((soma_1 * 10) % 11) <= 9 else 0

        soma_2 = 0
        contador_2 = 11
        for i in (nove_digitos + str(primeiro_digito)):
            soma_2 += (int(i) * contador_2)
            contador_2 -= 1
        segundo_digito = ((soma_2 * 10) % 11) if ((soma_2 * 10) % 11) <= 9 else 0

        ultimos_digitos = str(primeiro_digito) + str(segundo_digito)
        print('-'*40)
        print('CPF valido!'.center(40)) if verificador == ultimos_digitos else print('CPF invalido!'.center(40))
        
    
    def sair():
        print('-'*40)
        print('Pressione "Enter" para continuar.\n'
            'Digite "Sair" para sair.')
        print('-'*40)
        escolha = input('--> ').strip().lower()
        if escolha == 'sair':
            return True           # Sair
        elif escolha == '':
            return False          # Continua
        else:
            print('Escolha invalida')
            sair()
    if sair():
        break
    else:
        continue