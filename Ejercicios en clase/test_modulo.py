import pytest
from tramites import (
    validar_cedula,
    validar_fecha,
    clasificar_tiempo,
    calcular_promedio,
    resumen_diario,
)
from datetime import datetime
#CASOS DE PRUEBA PARA LA FUNCION validar_cedula
# Verifica que una cédula de exactamente 10 dígitos numéricos sea válida
def test_cedula_valida_retorna_true():
    assert validar_cedula("1234567890") is True

# Verifica que una cédula con longitud incorrecta sea inválida
def test_cedula_invalida_retorna_false():
    assert validar_cedula("12345") is False
    assert validar_cedula("12345678901") is False

# Verifica que una cédula con caracteres no numéricos sea inválida
def test_cedula_con_caracteres_no_numericos_retorna_false():
    assert validar_cedula("123456789a") is False

# Verifica que una cédula con menos de 10 dígitos sea inválida
def test_cedula_corta_retorna_false():
    assert validar_cedula("123456789") is False

# CASOS DE PRUEBA PARA LA FUNCION validar_fecha

# Verifica que una fecha con formato incorrecto sea inválida
def test_fecha_invalida_retorna_false():
    assert validar_fecha("01-01-2023") is False
    assert validar_fecha("01/01/23") is False

# CASOS DE PRUEBA PARA LA FUNCION clasificar_tiempo
# Verifica que exactamente 10 minutos se clasifique como Ágil
def test_clasificar_tiempo_diez_minutos_es_agil():
    assert clasificar_tiempo(10) == "Ágil"

# Verifica que exactamente 30 minutos se clasifique como Normal
def test_clasificar_tiempo_treinta_minutos_es_normal():
    assert clasificar_tiempo(30) == "Normal"

# Verifica que exactamente 31 minutos se clasifique como Demorada
def test_clasificar_tiempo_treinta_uno_minutos_es_demorada():
    assert clasificar_tiempo(31) == "Demorada"

# Verifica que un tiempo negativo produzca ValueError
def test_clasificar_tiempo_negativo_lanza_error():
    with pytest.raises(ValueError):
        clasificar_tiempo(-5)   

#CASOS DE PRUEBA PARA LA FUNCION calcular_promedio
# Verifica el promedio de una lista de tiempos
def test_calcular_promedio_lista_valida():
    assert calcular_promedio([10, 20, 30]) == 20.0

# Verifica el promedio de una lista vacía
def test_calcular_promedio_lista_vacia():
    assert calcular_promedio([]) == 0.0 

# Prueba varios casos de cédulas válidas e inválidas usando parametrización
@pytest.mark.parametrize("cedula, esperado", [
    ("1234567890", True),
    ("12345", False),
    ("12345678901", False),
    ("123456789a", False),
    ("123456789", False)
])
def test_validar_cedula_parametrizado(cedula, esperado):          
    assert validar_cedula(cedula) == esperado  

# Prueba fechas válidas, fechas inexistentes y formatos incorrectos
# Sugerencia de Copilot aceptada:
# Se mantiene la prueba parametrizada porque agrupa varios escenarios
# y evita duplicación de código
@pytest.mark.parametrize("fecha, esperado", [
    ("01/01/2023", True),   
    ("31/02/2023", False),  # Fecha inexistente
    ("01-01-2023", False),  # Formato incorrecto
    ("01/01/23", False)     # Formato incorrecto    
])
def test_validar_fecha_parametrizado(fecha, esperado):
    assert validar_fecha(fecha) == esperado

# Prueba la clasificación de tiempos incluyendo los valores límite de 10 y 30 minutos
@pytest.mark.parametrize("minutos, esperado", [
    (10, "Ágil"),
    (30, "Normal"),
    (31, "Demorada")
])
def test_clasificar_tiempo_parametrizado(minutos, esperado):
    assert clasificar_tiempo(minutos) == esperado  

# Prueba el cálculo del promedio con diferentes listas de tiempos
@pytest.mark.parametrize("tiempos, esperado", [
    ([10, 20, 30], 20.0),   
    ([], 0.0),              
    ([5, 15, 25, 35], 20.0) 
])
def test_calcular_promedio_parametrizado(tiempos, esperado):
    assert calcular_promedio(tiempos) == esperado
