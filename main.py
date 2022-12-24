# -*- coding: utf8 -*-

from random import randint


def gerar_numero_qualquer(inicio: int = 0, fim: int = 10) -> int:
    """Gerar um valor númerico aleatório."""
    random_number: int = randint(a=inicio, b=fim)
    return random_number


number: int = gerar_numero_qualquer()
print(number)
