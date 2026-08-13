# 📌 API de Marcaciones

## 📖 Descripción

Proyecto desarrollado como **Caso Integrador Final del curso GitHub Copilot para Desarrollo y Aseguramiento de la Calidad**.

La aplicación consiste en una API REST ficticia desarrollada en Python con Flask, orientada al registro de marcaciones y consulta de información básica de personas y horarios. Para el desarrollo se utilizaron únicamente datos simulados, sin información institucional real.

El proyecto integra prácticas de desarrollo asistido por GitHub Copilot, pruebas automatizadas con pytest, generación de reportes con Allure, análisis de calidad mediante SonarQube for IDE y control de versiones con Git y GitHub.

---

## 🎯 Objetivo

Desarrollar una API sencilla que permita registrar y consultar información ficticia de marcaciones, incorporando validaciones de datos, pruebas automatizadas y herramientas de análisis de calidad que permitan verificar el correcto funcionamiento y mantenibilidad del código.

### Validaciones implementadas

```text
[✔] Validación de cédula
[✔] Validación de fecha
[✔] Validación de hora
[✔] Validación de código de reloj
[✔] Validación de tipo de marcación
[✔] Validación de solicitudes JSON
```

---

## 🚀 Funcionalidades

La API permite:

- Consultar información de una persona mediante su cédula.
- Consultar horarios asociados a una persona.
- Registrar marcaciones mediante solicitudes POST.
- Validar los datos recibidos antes de registrar una marcación.
- Rechazar solicitudes con información incorrecta.
- Retornar códigos HTTP y mensajes de error claros.
- Ejecutar pruebas automatizadas mediante pytest.
- Generar reportes visuales de pruebas mediante Allure.
- Analizar la calidad y seguridad del código mediante SonarQube for IDE.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- pytest
- Allure Report
- GitHub Copilot
- SonarQube for IDE
- Git
- GitHub

---

## 🧭 Endpoints

### 1. Consultar persona

```http
GET /personas/<cedula>
```

Ejemplo:

```text
/personas/0123456789
```

Respuesta satisfactoria:

```json
{
  "ok": true,
  "persona": {
    "cedula": "0123456789",
    "nombre": "Ana Gómez",
    "departamento": "Administración"
  }
}
```

---

### 2. Consultar horarios

```http
GET /horarios/<cedula>
```

Ejemplo:

```text
/horarios/0123456789
```

La API retorna los horarios ficticios asociados a la persona consultada.

---

### 3. Registrar marcación

```http
POST /marcaciones
```

Ejemplo de cuerpo JSON:

```json
{
  "cedula": "0123456789",
  "tipo": 1,
  "codigo_reloj": "RELOJ001",
  "fecha": "2026-08-11",
  "hora": "08:15"
}
```

Respuesta satisfactoria:

```json
{
  "ok": true,
  "mensaje": "Marcación registrada.",
  "marcacion": {
    "cedula": "0123456789",
    "tipo": 1,
    "codigo_reloj": "RELOJ001",
    "fecha": "2026-08-11",
    "hora": "08:15"
  }
}
```

---

## 🔎 Validaciones implementadas

### Cédula

La cédula debe contener exactamente **10 dígitos numéricos**.

Ejemplo válido:

```text
0123456789
```

### Fecha

La fecha debe cumplir estrictamente el formato:

```text
YYYY-MM-DD
```

Además, debe corresponder a una fecha real.

### Hora

La hora debe cumplir el formato de 24 horas:

```text
HH:MM
```

Por ejemplo:

```text
08:15
```

### Código de reloj

El código de reloj es un campo obligatorio y no puede enviarse vacío.

### Tipo de marcación

El tipo de marcación debe corresponder a un valor numérico permitido entre:

```text
1, 2, 3, 4
```

---

## ❌ Manejo de errores

La API devuelve respuestas JSON controladas cuando la información recibida no cumple las validaciones.

Ejemplo:

```json
{
  "ok": false,
  "error": "Tipo de marcación inválido: debe ser un número entre 1 y 4."
}
```

También se utilizan códigos HTTP según el resultado de la solicitud, entre ellos:

- `200 OK`: consulta realizada correctamente.
- `201 CREATED`: marcación registrada correctamente.
- `400 BAD REQUEST`: datos o formato de solicitud inválidos.
- `404 NOT FOUND`: persona u horario no encontrado.

---

## 🧪 Pruebas automatizadas con pytest

Se desarrolló una batería de pruebas automatizadas para verificar los principales escenarios funcionales y de validación de la API.

Para ejecutar las pruebas:

```bash
python -m pytest -v
```

### Resultado final

```text
12 passed
```

Se ejecutaron **12 casos de prueba**, obteniendo:

| Resultado | Cantidad |
|---|---:|
| ✅ Aprobadas | 12 |
| ❌ Fallidas | 0 |
| 📊 Total | 12 |

Las pruebas incluyen escenarios relacionados con:

- consulta válida de personas;
- cédula inválida;
- persona inexistente;
- consulta de horarios;
- horarios inexistentes;
- registro válido de marcación;
- tipo de marcación inválido;
- código de reloj obligatorio;
- fecha inválida;
- hora inválida.

---

## 📊 Reporte de pruebas con Allure

Para complementar la ejecución de pytest se integró **Allure Report**, permitiendo visualizar gráficamente los resultados de las pruebas automatizadas.

Los resultados de pytest se generan mediante:

```bash
python -m pytest -v --alluredir=allure-results --clean-alluredir
```

Posteriormente, el reporte puede visualizarse mediante:

```bash
allure serve allure-results
```

### Resultado obtenido

```text
Total de pruebas: 12
Aprobadas:        12
Fallidas:          0
```

El reporte Allure permite consultar individualmente cada caso de prueba, su estado y tiempo de ejecución.

> **Resultado final:** 100 % de los casos de prueba ejecutados finalizaron satisfactoriamente.

---

## 🔍 Análisis de calidad con SonarQube for IDE

El código fuente fue analizado mediante **SonarQube for IDE** con el propósito de identificar oportunidades de mejora relacionadas con calidad, mantenibilidad y seguridad.

Durante el análisis se identificaron observaciones en `app.py`, entre ellas:

- duplicación de mensajes utilizados en las validaciones;
- configuración del modo debug;
- aspectos relacionados con la configuración de seguridad;
- oportunidades de mejora en la mantenibilidad del código.

Las observaciones correspondientes al código desarrollado fueron revisadas y corregidas.

Después de realizar los cambios se ejecutó nuevamente la batería de pruebas:

```text
12 passed
```

Esto permitió comprobar que las mejoras de calidad no afectaron el comportamiento funcional de la API.

En la revisión final no se visualizaron hallazgos pendientes correspondientes a `app.py`. El hallazgo restante observado pertenecía a `globals.py`, archivo correspondiente a una dependencia externa de Flask ubicada en `site-packages`, por lo que no se modificó código de terceros.

---

## 🤖 Uso de GitHub Copilot

GitHub Copilot se utilizó como herramienta de apoyo durante el desarrollo del proyecto para:

- generar la estructura inicial de la API;
- apoyar la implementación de validaciones;
- generar y revisar casos de prueba;
- analizar fallos encontrados durante las pruebas;
- apoyar la revisión de hallazgos de SonarQube;
- mejorar comentarios y documentación.

Se registraron tres sesiones principales de trabajo en Copilot Chat:

1. **API para registro de marcaciones**
2. **Revisar tests en app.py**
3. **Solucionar hallazgos SonarQube**

Las sugerencias generadas fueron revisadas antes de incorporarlas al proyecto y posteriormente verificadas mediante pruebas automatizadas.

**Solicitudes premium utilizadas: 0.**

---

## 📁 Estructura del proyecto

```text
api_marcaciones/
│
├── app.py
├── README.md
├── requerimientos.txt
├── pruebas_api.http
├── .gitignore
│
├── tests/
│   └── test_api.py
│
├── allure-results/
│
└── .git/
```

> Las carpetas temporales generadas por Python y pytest se excluyen del repositorio mediante `.gitignore`.

---

## ▶️ Ejecución del proyecto

### 1. Instalar dependencias

```bash
python -m pip install -r requerimientos.txt
```

### 2. Ejecutar la API

```bash
python app.py
```

Por defecto, la aplicación se ejecuta localmente en:

```text
http://127.0.0.1:5000
```

### 3. Ejecutar las pruebas

```bash
python -m pytest -v
```

### 4. Generar resultados para Allure

```bash
python -m pytest -v --alluredir=allure-results --clean-alluredir
```

---

## 🔀 Gestión del código

El proyecto se gestionó mediante Git y GitHub utilizando una rama específica para el desarrollo:

```text
feature/api-marcaciones
```

El flujo de trabajo contempla:

```text
Desarrollo
    ↓
Pruebas automatizadas
    ↓
Análisis SonarQube
    ↓
Correcciones
    ↓
Verificación final
    ↓
Documentación
    ↓
Pull Request hacia main
```

---

## ✅ Resultado final

La API ficticia de marcaciones fue desarrollada y validada satisfactoriamente.

```text
✔ API funcional
✔ Validaciones implementadas
✔ 12 pruebas automatizadas aprobadas
✔ 0 pruebas fallidas
✔ Reporte Allure generado
✔ Análisis de calidad con SonarQube realizado
✔ Código documentado
✔ Gestión mediante Git y GitHub
```

El proyecto permitió integrar desarrollo asistido por GitHub Copilot, automatización de pruebas y análisis de calidad dentro de un flujo de trabajo controlado.