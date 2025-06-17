# Tratamento de Erros em Python com Programação Orientada a Objetos - Pedro Simões

import os

class ListaDeNumeros:
    def __init__(self, lista: list):
        self.lista = lista


    def obter_elemento(self, posicao):

        try:
            resultado = self.lista[posicao]

        except IndexError:
            print('\nErro! Esse valor da lista não existe ou não pôde ser acedido.')
            return False

        else:
            print(f'\nO valor da lista na posição {posicao} é {resultado}.\n')
            return True


    def dividir_elemento(self, posicao, dividor):
        
        try:
            resultado = self.lista[posicao] / dividor
        
        except ZeroDivisionError:
            print('\nErro! Divisão por 0.')
        
        else:
            print(f'\nO resultado da divisão de {self.lista[posicao]} por {divisor} é {resultado:.2f}.')


def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


limpar()

lista = ListaDeNumeros([1, 2, 3, 4, 5, 6])


verificacao = False

while verificacao == False:
    try:
        print('----- Valor do elemento da lista: -----')

        posicao = int(input('Introduz uma posição da lista: '))
        if not lista.obter_elemento(posicao):
            raise
    except:
        print('Tenta novamente.\n')
    else:
        verificacao = True


verificacao = False

while verificacao == False:
    try:
        print('\n----- Divisão do elemento da lista -----')

        posicao = int(input('Introduz uma posição da lista: '))
        if lista.obter_elemento(posicao):

            divisor = int(input(f'Introduz um valor para {lista.lista[posicao]} ser dividido: '))
            lista.dividir_elemento(posicao, divisor)
        else:
            raise
    except:
        print('Tenta novamente.\n')
    else:
        verificacao = True

print()