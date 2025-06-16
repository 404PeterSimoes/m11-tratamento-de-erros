# Tratamento de Erros em Python com Programação Orientada a Objetos - Pedro Simões

import os

class ListaDeNumeros:
    def __init__(self, lista: list):
        self.lista = lista


    def obter_elemento(self, posicao):

        try:
            resultado = self.lista[posicao]

        except IndexError:
            print('Erro! Esse valor da lista não pôde ser acedido.')

        else:
            print(f'O valor da lista na posição {posicao} é {resultado}.')


    def dividir_elemento(self, posicao, dividor):
        
        try:
            resultado = self.lista[posicao] / dividor
        
        except ZeroDivisionError:
            print('Erro! Divisão por 0')
        
        else:
            print(f'{resultado:.2f}')


def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


limpar()

lista = ListaDeNumeros([1, 2, 3, 4, 5, 6])

print('----- Valor do elemento da lista: -----')
posicao = int(input('Introduz uma posição da lista: '))
lista.obter_elemento(posicao)

print('----- Divisão do elemento da lista -----')
lista.dividir_elemento(2, 1)

#falta aqui