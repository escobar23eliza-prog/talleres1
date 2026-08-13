import csv
from pathlib import Path

from tramites import validar_cedula, validar_fecha, clasificar_tiempo


def procesar_carpeta():

    # Sube un nivel desde "Ejercicios en clase" hasta "talleres1"
    base_dir = Path(__file__).resolve().parent

    # Carpeta donde están los CSV
    carpeta = base_dir / "datos"

    print("Buscando archivos en:")
    print(carpeta)

    if not carpeta.exists():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta}")

    archivos = list(carpeta.glob("*.csv"))

    if len(archivos) == 0:
        raise FileNotFoundError(f"No hay archivos CSV en: {carpeta}")

    total_validas = 0
    total_descartadas = 0
    suma_minutos = 0

    categorias = {
        "Ágil": 0,
        "Normal": 0,
        "Demorada": 0
    }

    for archivo in archivos:

        print(f"Leyendo: {archivo.name}")

        with archivo.open("r", encoding="utf-8", newline="") as f:

            lector = csv.DictReader(f)

            for fila in lector:

                cedula = fila["cedula"].strip()
                fecha = fila["fecha"].strip()
                minutos_txt = fila["minutos"].strip()

                if not validar_cedula(cedula):
                    total_descartadas += 1
                    continue

                if not validar_fecha(fecha):
                    total_descartadas += 1
                    continue

                try:
                    minutos = int(minutos_txt)
                except:
                    total_descartadas += 1
                    continue

                if minutos < 0:
                    total_descartadas += 1
                    continue

                total_validas += 1
                suma_minutos += minutos

                categoria = clasificar_tiempo(minutos)
                categorias[categoria] += 1

    if total_validas > 0:
        promedio = round(suma_minutos / total_validas, 2)
    else:
        promedio = 0

    resumen = {
        "total": total_validas,
        "descartados": total_descartadas,
        "promedio": promedio,
        "categorias": categorias
    }

    salida = Path(__file__).parent / "resumen.csv"

    with salida.open("w", encoding="utf-8", newline="") as f:

        escritor = csv.writer(f)

        escritor.writerow([
            "total_validas",
            "total_descartadas",
            "promedio",
            "agil",
            "normal",
            "demorada"
        ])

        escritor.writerow([
            resumen["total"],
            resumen["descartados"],
            resumen["promedio"],
            categorias["Ágil"],
            categorias["Normal"],
            categorias["Demorada"]
        ])

    return resumen


if __name__ == "__main__":

    resumen = procesar_carpeta()

    print("\n========== RESUMEN ==========")
    print(f"Filas válidas: {resumen['total']}")
    print(f"Filas descartadas: {resumen['descartados']}")
    print(f"Promedio: {resumen['promedio']}")
    print(f"Ágil: {resumen['categorias']['Ágil']}")
    print(f"Normal: {resumen['categorias']['Normal']}")
    print(f"Demorada: {resumen['categorias']['Demorada']}")