"""Funciones de validación para números y cadenas."""

from __future__ import annotations


def es_primo(numero: int) -> bool:
    """Determina si un número entero es primo.

    Args:
        numero: Entero a evaluar.

    Returns:
        True si el número es primo, False en caso contrario.

    Raises:
        TypeError: Si el valor no es un entero.
    """
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")

    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = int(numero ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False
    return True


def validar_longitud(cadena: str, longitud_minima: int) -> bool:
    """Valida que una cadena tenga al menos una longitud mínima.

    Args:
        cadena: Texto a validar.
        longitud_minima: Número mínimo de caracteres que debe tener la cadena.

    Returns:
        True si la cadena cumple la longitud mínima, False en caso contrario.

    Raises:
        TypeError: Si los argumentos no son del tipo esperado.
        ValueError: Si la longitud mínima es negativa.
    """
    if not isinstance(cadena, str):
        raise TypeError("La cadena debe ser un texto.")
    if not isinstance(longitud_minima, int):
        raise TypeError("La longitud mínima debe ser un entero.")
    if longitud_minima < 0:
        raise ValueError("La longitud mínima no puede ser negativa.")

    return len(cadena) >= longitud_minima


__all__ = ["es_primo", "validar_longitud"]

