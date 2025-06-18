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

        if valor < 0:
            raise ValorInvalidoError

        self.saldo += valor

    def levantar(self, valor):

        if self.saldo < valor:
            raise SaldoInsuficienteError

        self.saldo -= valor

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

contas = [
    conta_manuel := ContaBancaria('Manuel Josefandro', 545),
    conta_joaquina := ContaBancaria('Joaquina Garcia', 734)
]


limpar()
print('   Menu de Contas:\n---------------------')
for i in range(0, len(contas)):
    print(f'{i + 1} - {contas[i].titular}')

verificacao = False
while not verificacao:
    try:
        n = int(input('\nIntroduza o número de uma conta: '))
        n -= 1

    # Caso o valor introduzido não seja um inteiro
    except:
        print('Tenta novamente.')

    # Se for inteiro
    else:
        limpar()
        try:
            contaselecionada = contas[n]
        
        # Caso o valor introduzido não seja um índice válido da lista de contas
        except IndexError:
            print('O número de conta introduzido não existe')

        # Se for um índice válido, sair do ciclo
        else:
            verificacao = True

print(f'Conta selecionada:\n\n'
      f'{n} - {contaselecionada.titular}\n'
      f'Saldo - {contaselecionada.saldo}€')

verificacao = False
while not verificacao:
    try:
        acao = int(input('\nQue ação pretende realizar?'
                        '\n1 - Depositar'
                        '\n2 - Levantar\n'))
        
        if not (acao == 1 or acao == 2):
            raise
        
    # Caso o valor introduzido não seja um inteiro
    except:
        print('Tenta novamente.')

    # Se for inteiro, sair do ciclo
    else:
        verificacao = True


verificacao = False
while not verificacao:
    try:
        if acao == 1:
            valor = int(input(('Qual o valor que pretende depositar?\n')))

        # adicionar aqui?

        elif acao == 2:
            valor = int(input(('Qual o valor que pretende levantar?\n')))

    except:
        print('Tenta novamente.')

    else:
        verificacao = True


verificacao = False

if acao == 1:

    while not verificacao:
        try:
            contaselecionada.depositar(valor)
        
        except SaldoInsuficienteError:
            print('O valor que pretende depositar não é válido.')

        except:
            print('Tenta novamente.')

        else:
            print(f'Valor de {valor}€ depositado na conta de nome {contaselecionada.titular}!\n'
                  f'Novo Saldo - {contaselecionada.saldo}€')

elif acao == 2:

    while not verificacao:
        try:
            contaselecionada.levantar(valor)


        except ValorInvalidoError:
            print('Não possui saldo suficiente para esse levantamento.')

        except:
            print('Tenta novamente.')

        else:
            print(f'Valor de {valor}€ depositado na conta de nome {contaselecionada.titular}!\n'
                f'Novo Saldo - {contaselecionada.saldo}€')