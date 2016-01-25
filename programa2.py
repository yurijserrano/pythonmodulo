# -*- coding: UTF-8 -*-


"""

Utilização do módulo random


Ele é utilizado para o sorteio de números e strings

Utilizando o choice do módulo random escolhemos um elemento
aleatório.

Obs: Com raw_input

"""


# Alternativa de import

# import random

# random.choice

from random import choice

elemento1 = raw_input("Digite o primeiro elemento:")
elemento2 = raw_input("Digite o segundo elemento:")
elemento3 = raw_input("Digite o terceiro elemento:")



lista = [elemento1,elemento2,elemento3]
sorteio = choice(lista)


print "O elemento sorteado foi: ", sorteio 