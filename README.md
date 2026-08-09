# Ejemplo de Clase: Validación en Python

Este proyecto contiene funciones de validación sencillas en Python para:

- comprobar si un número es primo,
- verificar si una cadena cumple una longitud mínima.

## Archivos

- `validacion.py`: funciones reutilizables para validar números y cadenas.

## Funciones disponibles

### `es_primo(numero)`
Comprueba si `numero` es un número entero primo.

- Retorna `True` si el número es primo.
- Retorna `False` si el número es menor que 2 o tiene divisores.
- Lanza `TypeError` si el argumento no es un entero.

### `validar_longitud(cadena, longitud_minima)`
Comprueba si una cadena tiene al menos `longitud_minima` caracteres.

- Retorna `True` si la cadena cumple la longitud mínima.
- Retorna `False` si la cadena es más corta.
- Lanza `TypeError` si los argumentos no son del tipo correcto.
- Lanza `ValueError` si la longitud mínima es negativa.

## Ejemplos de uso

```python
from validacion import es_primo, validar_longitud

print(es_primo(11))            # True
print(es_primo(20))            # False
print(validar_longitud("Hola", 3))   # True
print(validar_longitud("Hi", 3))     # False
```

## Cómo ejecutar

Para usar las funciones desde otro script, importa el módulo `validacion`:

```python
from validacion import es_primo, validar_longitud
```

Luego llama a las funciones con tus datos de entrada.

## Por qué es útil

Este proyecto es ideal para aprender conceptos básicos de programación en Python,
como:

- estructuras de control (`if`, `for`),
- validación de tipos,
- buenas prácticas de documentación con docstrings.

## Contribuciones

Si deseas mejorar este proyecto, puedes agregar:

- más funciones de validación (`email`, `contraseña`, `fecha`),
- pruebas unitarias con `pytest`,
- ejemplos en un script independiente.
