# -*- coding: utf8 -*-

import random


def gerar_numero_qualquer(inicio: int = 0, fim: int = 10):
    """Gerar um valor númerico aleatório."""
    numero_qualquer = random.randint(a=inicio, b=fim)
    return numero_qualquer
