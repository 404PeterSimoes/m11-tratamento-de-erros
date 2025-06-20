# Tratamento de Erros em Python com Exceções Personalizadas - Pedro Simões

import os

class ValorInvalidoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):

        # Verificar se o valor introduzido é igual ou menor que 0
        if valor <= 0:
            raise ValorInvalidoError

        self.saldo += valor

    def levantar(self, valor):

        # Verificar se o valor introduzido é igual ou menor que 0
        if valor <= 0:
            raise ValorInvalidoError

        # Verificar se o saldo atual é inferior ao que se pretende levantar
        if self.saldo < valor:
            raise SaldoInsuficienteError

        self.saldo -= valor

# Limpar o terminal
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Lista com as Contas Bancárias
contas = [
    ContaBancaria('Manuel Josefandro', 545),
    ContaBancaria('Joaquina Garcia', 734),
    ContaBancaria('Pedro Miguel', 1000)
]

# Ciclo infinito
while True:
    limpar()

    verificacao = False
    while not verificacao:
        try:

            # Imprimir o menu de contas

            print('Menu:\n------------------------')
            for i in range(0, len(contas)):
                print(f'{i + 1} - {contas[i].titular}')

            print('------------------------\n0 - Sair')

            n = int(input('\nIntroduza uma opção: '))

            # Terminar o programa
            if n == 0:
                exit()

            n -= 1
                
        # Caso o valor introduzido não seja um inteiro
        except ValueError:
            print('Tente novamente.\n')

        # Se for inteiro
        else:
            try:

                if n < 0:
                    raise IndexError

                # Forçar verificação de índice válido
                contaselecionada = contas[n]
            
            # Caso o valor introduzido não seja um índice válido da lista de contas
            except IndexError:
                print('O número de conta introduzido não existe.\n')

            # Se for um índice válido, sair do ciclo
            else:
                limpar()
                verificacao = True

    # Imprimir atributos da conta selecionada
    print(f'Conta selecionada:\n\n'
        f'{n + 1} - {contaselecionada.titular}\n'
        f'Saldo - {contaselecionada.saldo}€\n')

    verificacao = False
    while not verificacao:
        try:
            acao = int(input('Que ação pretende realizar?'
                        '\n1 - Depositar'
                        '\n2 - Levantar\n'))
            
            if not (acao == 1 or acao == 2):
                raise ValueError
            
        # Caso o valor introduzido não seja um inteiro
        except ValueError:
            print('Tente novamente.\n')

        # Se for inteiro, sair do ciclo
        else:
            verificacao = True


    verificacao = False

    # DEPOSITAR
    if acao == 1:

        while not verificacao:
            try:
                valor = int(input('\nQual o valor que pretende depositar?\n'))

                contaselecionada.depositar(valor)
            
            # Caso o valor introduzido seja inferior a 0
            except ValorInvalidoError:
                print('Não é possível depositar valores iguais ou inferiores a 0.')

            # Caso o valor introduzido não seja um inteiro
            except ValueError:
                print('Tente novamente.')

            # Se houver sucesso na operação
            else:
                print(f'\nValor de {valor}€ depositado na conta de nome {contaselecionada.titular}!\n'
                    f'Novo Saldo - {contaselecionada.saldo}€\n')
                
                os.system("pause")
                verificacao = True

    # LEVANTAR
    elif acao == 2:

        while not verificacao:
            try:
                valor = int(input('\nQual o valor que pretende levantar?\n'))

                contaselecionada.levantar(valor)

            # Caso o valor introduzido seja igual ou inferior a 0
            except ValorInvalidoError:
                print('Não é possível levantar valores iguais ou inferiores a 0.')

            # Verificar se há saldo suficiente para fazer o levantamento
            except SaldoInsuficienteError:
                print('Não possui saldo suficiente para esse levantamento.')

            # Caso o valor intruduzido não seja um inteiro
            except ValueError:
                print('Tente novamente.')

            # Se houver sucesso na operação
            else:
                print(f'\nValor de {valor}€ levantado da conta de nome {contaselecionada.titular}!\n'
                    f'Novo Saldo - {contaselecionada.saldo}€\n')
                
                os.system("pause")
                verificacao = True