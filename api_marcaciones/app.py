import os
import re
from flask import Flask, request, jsonify
from datetime import datetime

# Configuración del entorno de ejecución.
# El modo debug solo se activa cuando la aplicación se ejecuta en entorno de desarrollo.
APP_ENV = os.environ.get("APP_ENV", "development").strip().lower()
DEBUG_MODE = APP_ENV == "development" and os.environ.get("FLASK_DEBUG", "false").strip().lower() in {"1", "true", "yes", "on"}

# API REST stateless que recibe JSON; no hay formularios HTML ni sesiones con CSRF.
# Inicializa la API Flask.
# La aplicación trabaja únicamente con JSON y no utiliza formularios ni sesiones web.
app = Flask(__name__)  # NOSONAR - la API no expone formularios web ni estado de sesión.
app.config.update(
    JSON_SORT_KEYS=False,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    PROPAGATE_EXCEPTIONS=not DEBUG_MODE,
    TESTING=False,
)
# Mensaje reutilizable para evitar duplicación de texto en las validaciones de cédula.
CEDULA_INVALIDA_MSG = "Cédula inválida: debe tener exactamente 10 dígitos numéricos."

# Datos ficticios de personas utilizados para simular las consultas de la API.
PERSONAS = {
    "0123456789": {
        "cedula": "0123456789",
        "nombre": "Ana Gómez",
        "departamento": "Administración"
    },
    "9876543210": {
        "cedula": "9876543210",
        "nombre": "Luis Torres",
        "departamento": "Operaciones"
    }
}


# Horarios ficticios asociados a cada persona registrada.
HORARIOS = {
    "0123456789": [
        {"dia": "Lunes", "entrada": "08:00", "salida": "17:00"},
        {"dia": "Martes", "entrada": "08:00", "salida": "17:00"}
    ],
    "9876543210": [
        {"dia": "Miércoles", "entrada": "09:00", "salida": "18:00"}
    ]
}

# Lista en memoria donde se almacenan temporalmente las marcaciones registradas.
MARCACIONES = []

# Tipos de marcación permitidos por la API.
VALID_TIPOS = {1, 2, 3, 4}


def validar_cedula(cedula):
    """Valida que la cédula sea una cadena de exactamente 10 dígitos numéricos."""
    return isinstance(cedula, str) and cedula.isdigit() and len(cedula) == 10


def validar_tipo(tipo):
    """Valida que el tipo de marcación corresponda a un valor permitido entre 1 y 4."""
    if isinstance(tipo, int):
        return tipo in VALID_TIPOS
    if isinstance(tipo, str) and tipo.isdigit():
        return int(tipo) in VALID_TIPOS
    return False


def validar_fecha(fecha_texto):
    """Valida que la fecha cumpla el formato YYYY-MM-DD y que exista realmente."""
    if not isinstance(fecha_texto, str):
        return False
    if not re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", fecha_texto):
        return False
    try:
        datetime.strptime(fecha_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_hora(hora_texto):
    """Valida que la hora cumpla estrictamente el formato HH:MM en formato de 24 horas."""
    if not isinstance(hora_texto, str):
        return False
    if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", hora_texto):
        return False
    try:
        datetime.strptime(hora_texto, "%H:%M")
        return True
    except ValueError:
        return False


def respuesta_error(mensaje, codigo=400):
    """Genera una respuesta JSON uniforme para los errores de validación de la API."""
    return jsonify({"ok": False, "error": mensaje}), codigo


@app.route("/personas/<cedula>", methods=["GET"])
def obtener_persona(cedula):
    """Consulta una persona ficticia mediante su número de cédula."""
    if not validar_cedula(cedula):
        return respuesta_error(CEDULA_INVALIDA_MSG)
    persona = PERSONAS.get(cedula)
    if not persona:
        return respuesta_error("Persona no encontrada.", 404)
    return jsonify({"ok": True, "persona": persona})


@app.route("/horarios/<cedula>", methods=["GET"])
def obtener_horarios(cedula):
    """Consulta los horarios ficticios asociados a una persona."""
    if not validar_cedula(cedula):
        return respuesta_error(CEDULA_INVALIDA_MSG)
    horarios = HORARIOS.get(cedula)
    if horarios is None:
        return respuesta_error("Horarios no encontrados para la cédula indicada.", 404)
    return jsonify({"ok": True, "horarios": horarios})


@app.route("/marcaciones", methods=["POST"])
def crear_marcacion():
    """Registra una marcación después de validar los datos recibidos en formato JSON."""
    if not request.is_json:
        return respuesta_error("El cuerpo debe ser JSON válido.")

    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return respuesta_error("El cuerpo debe ser un objeto JSON válido.")

    cedula = datos.get("cedula")
    tipo = datos.get("tipo")
    codigo_reloj = datos.get("codigo_reloj")
    fecha = datos.get("fecha")
    hora = datos.get("hora")

    if not validar_cedula(cedula):
        return respuesta_error(CEDULA_INVALIDA_MSG)

    if codigo_reloj in (None, ""):
        return respuesta_error("Código de reloj obligatorio.")

    if not validar_tipo(tipo):
        return respuesta_error("Tipo de marcación inválido: debe ser un número entre 1 y 4.")

    if not validar_fecha(fecha):
        return respuesta_error("Fecha inválida: use el formato YYYY-MM-DD.")

    if not validar_hora(hora):
        return respuesta_error("Hora inválida: use el formato HH:MM en 24 horas.")

    registro = {
        "cedula": cedula,
        "tipo": int(tipo),
        "codigo_reloj": codigo_reloj,
        "fecha": fecha,
        "hora": hora
    }
    MARCACIONES.append(registro)
    return jsonify({"ok": True, "mensaje": "Marcación registrada.", "marcacion": registro}), 201

# Inicia el servidor Flask.
# El modo debug depende de las variables de entorno configuradas.
if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=5000)
