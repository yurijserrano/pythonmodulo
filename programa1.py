# -*- coding: UTF-8 -*-


"""

Utilização do módulo random


Ele é utilizado para o sorteio de números e strings

Utilizando o choice do módulo random escolhemos um elemento
aleatório.

"""


# Alternativa de import

# import random

# random.choice

from random import choice

elemento1 = input("Digite o primeiro elemento:")
elemento2 = input("Digite o segundo elemento:")
elemento3 = input("Digite o terceiro elemento:")



lista = [elemento1,elemento2,elemento3]
sorteio = choice(lista)


print "O elemento sorteado foi: ", sorteio 