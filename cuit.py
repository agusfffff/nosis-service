# -*- coding: utf-8 -*-
import re

_COEFICIENTES_CUIT = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

#  los cuits se esperan como: 20389273407.

def normalizar_cuit(valor):
    """solo acepta cuit si son 11 digitos asccii, o si es un float que es un entero. Devuelve None si no es un cuit valido."""
    if valor is None or isinstance(valor, bool):
        return None
    if isinstance(valor, float):
        if not valor.is_integer():
            return None
        valor = int(valor)
    texto = str(valor).strip()
    return texto if len(texto) == 11 and texto.isascii() and texto.isdigit() else None


def cuit_checksum_valido(cuit):
    """True si el CUIT/CUIL (en cualquier formato que acepte
    normalizar_cuit) tiene un digito verificador matematicamente correcto -
    algoritmo modulo 11 estandar (coeficientes 5,4,3,2,7,6,5,4,3,2 sobre los
    primeros 10 digitos). False si no normaliza a 11 digitos, o si el
    verificador no coincide."""

    limpio = normalizar_cuit(cuit)
    if limpio is None:
        return False
    digitos = [int(c) for c in limpio]
    suma = sum(d * c for d, c in zip(digitos[:10], _COEFICIENTES_CUIT))
    resto = suma % 11
    verificador = 0 if resto == 0 else 11 - resto
    if verificador == 10:
        return False
    return verificador == digitos[10]
