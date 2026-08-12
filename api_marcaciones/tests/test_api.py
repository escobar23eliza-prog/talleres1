import json
import pytest

from app import app, MARCACIONES, validar_tipo


@pytest.fixture
def cliente():
    app.config["TESTING"] = True

    with app.test_client() as cliente:
        yield cliente


def test_obtener_persona_valida(cliente):
    respuesta = cliente.get("/personas/0123456789")
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 200
    assert datos["ok"] is True
    assert datos["persona"]["nombre"] == "Ana Gómez"


def test_obtener_persona_cedula_invalida(cliente):
    respuesta = cliente.get("/personas/123")
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Cédula inválida" in datos["error"]


def test_obtener_persona_inexistente(cliente):
    respuesta = cliente.get("/personas/0000000000")
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 404
    assert datos["ok"] is False
    assert "Persona no encontrada" in datos["error"]


def test_obtener_horarios_valido(cliente):
    respuesta = cliente.get("/horarios/9876543210")
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 200
    assert datos["ok"] is True
    assert isinstance(datos["horarios"], list)


def test_obtener_horarios_no_encontrado(cliente):
    respuesta = cliente.get("/horarios/0000000000")
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 404
    assert datos["ok"] is False


def test_crear_marcacion_valida(cliente):
    MARCACIONES.clear()
    payload = {
        "cedula": "0123456789",
        "tipo": 2,
        "codigo_reloj": "R1",
        "fecha": "2026-08-11",
        "hora": "09:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 201
    assert datos["ok"] is True
    assert datos["marcacion"]["cedula"] == payload["cedula"]
    assert len(MARCACIONES) == 1


def test_validar_tipo_invalido():
    assert validar_tipo(0) is False
    assert validar_tipo(5) is False
    assert validar_tipo(1) is True
    assert validar_tipo(4) is True


def test_crear_marcacion_cedula_invalida(cliente):
    payload = {
        "cedula": "12345",
        "tipo": 2,
        "codigo_reloj": "R1",
        "fecha": "2026-08-11",
        "hora": "09:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Cédula inválida" in datos["error"]


def test_crear_marcacion_tipo_invalido(cliente):
    payload = {
        "cedula": "0123456789",
        "tipo": 5,
        "codigo_reloj": "R1",
        "fecha": "2026-08-11",
        "hora": "09:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Tipo de marcación inválido" in datos["error"]


def test_crear_marcacion_sin_codigo_reloj(cliente):
    payload = {
        "cedula": "0123456789",
        "tipo": 1,
        "fecha": "2026-08-11",
        "hora": "09:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Código de reloj obligatorio" in datos["error"]


def test_crear_marcacion_fecha_invalida(cliente):
    payload = {
        "cedula": "0123456789",
        "tipo": 1,
        "codigo_reloj": "R1",
        "fecha": "11-08-2026",
        "hora": "09:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Fecha inválida" in datos["error"]


def test_crear_marcacion_hora_invalida(cliente):
    payload = {
        "cedula": "0123456789",
        "tipo": 1,
        "codigo_reloj": "R1",
        "fecha": "2026-08-11",
        "hora": "9:30"
    }

    respuesta = cliente.post("/marcaciones", json=payload)
    datos = json.loads(respuesta.data)

    assert respuesta.status_code == 400
    assert datos["ok"] is False
    assert "Hora inválida" in datos["error"]

