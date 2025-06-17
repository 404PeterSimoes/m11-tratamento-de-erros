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
        n = int(input('\nIntroduz o número de uma conta: '))

        

    except:
        pass
    else:
        verificacao = True