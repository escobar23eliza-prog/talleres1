# Módulo de gestión de trámites de atención ciudadana.
# Usa solo la librería estándar de Python.
# Valida que una cédula tenga exactamente 10 dígitos numéricos.
# Recibe str y devuelve bool.
# Devuelve False si es None, si está vacía o si contiene letras.
from datetime import datetime
def validar_cedula(cedula: str) -> bool:
    """Valida que una cédula tenga exactamente 10 dígitos numéricos.

    Args:
        cedula: Cédula a validar.

    Returns:
        True si la cédula es válida, False en caso contrario.
    """
    if not isinstance(cedula, str) or len(cedula) != 10 or not cedula.isdigit():
        return False
    return True

# Valida una fecha en formato dd/mm/aaaa que exista realmente.
# Rechaza 31/02/2026 y los meses fuera del rango 1 a 12.

def validar_fecha(texto: str) -> bool:
    if not isinstance(texto, str):
        return False
    try:
        datetime.strptime(texto, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Clasifica el tiempo de atención de un trámite.
# Ágil: hasta 10 minutos, inclusive. Normal: de 11 a 30.
# Demorada: más de 30. Lanza ValueError si es negativo.
# Ejemplos: 10 -> "Ágil" 11 -> "Normal" 31 -> "Demorada"

def clasificar_tiempo(minutos: int) -> str:
    """Clasifica el tiempo de atención de un trámite.

    Args:
        minutos: Tiempo en minutos.

    Returns:
        Una cadena que indica la clasificación del tiempo.

    Raises:
        ValueError: Si el tiempo es negativo.
    """
    if minutos < 0:
        raise ValueError("El tiempo no puede ser negativo.")
    if minutos <= 10:
        return "Ágil"
    elif minutos <= 30:
        return "Normal"
    else:
        return "Demorada"


# Calcula el promedio de minutos, redondeado a dos decimales.
# Para una lista vacía devuelve 0.0, sin lanzar excepción.
def calcular_promedio(tiempos: list) -> float:
    if not tiempos:
        return 0.0
    return round(sum(tiempos) / len(tiempos), 2)

# Consolida una lista de registros con cedula, fecha y minutos.
# Descarta los registros inválidos sin detener el proceso.
# Devuelve un diccionario con total, descartados, promedio
# y el conteo por categoría.
def resumen_diario(registros: list) -> dict:
    resumen = {
        "total": 0,
        "descartados": 0,
        "promedio": 0.0,
        "clasificacion": {"Ágil": 0, "Normal": 0, "Demorada": 0},
    }
    tiempos_validos = []

    for registro in registros:
        cedula = registro.get("cedula")
        fecha = registro.get("fecha")
        minutos = registro.get("minutos")

        if validar_cedula(cedula) and validar_fecha(fecha) and isinstance(minutos, int) and minutos >= 0:
            resumen["total"] += 1
            tiempos_validos.append(minutos)
            categoria = clasificar_tiempo(minutos)
            resumen["clasificacion"][categoria] += 1
        else:
            resumen["descartados"] += 1

    resumen["promedio"] = calcular_promedio(tiempos_validos)
    return resumen