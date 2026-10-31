import json
import subprocess
import sys
from html import escape
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT_DIR / "reports"


def generar_reporte_html(datos, destino, tag):
    """Genera un reporte HTML a partir del JSON de Behave."""

    filas = []

    for feature in datos:
        nombre_feature = feature.get("name", "Característica")

        for scenario in feature.get("elements", []):
            nombre = scenario.get("name")

            if not nombre:
                continue

            estado = scenario.get("status", "desconocido")

            filas.append(
                f"<tr><td>{escape(nombre_feature)}</td>"
                f"<td>{escape(nombre)}</td>"
                f"<td>{escape(estado)}</td></tr>"
            )

    contenido = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Reporte Behave {escape(tag)}</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 30px; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
th {{ background: #eeeeee; }}
</style>
</head>
<body>
<h1>Reporte de pruebas Behave</h1>
<p>Filtro ejecutado: {escape(tag)}</p>
<table>
<tr><th>Característica</th><th>Escenario</th><th>Estado</th></tr>
{''.join(filas)}
</table>
</body>
</html>"""

    destino.write_text(contenido, encoding="utf-8")



@pytest.mark.behave
@pytest.mark.parametrize("tag", ["@smoke", "@regression"])
def test_ejecutar_suite_behave(tag):
    """Ejecuta Behave desde Pytest y genera reportes."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    nombre = tag.replace("@", "")

    reporte_json = REPORTS_DIR / f"behave_{nombre}.json"
    reporte_pretty = REPORTS_DIR / f"behave_{nombre}_pretty.txt"
    reporte_html = REPORTS_DIR / f"behave_{nombre}.html"

    comandos = [
        ("json", reporte_json),
        ("pretty", reporte_pretty),
    ]

    for formato, archivo in comandos:
        comando = [
            sys.executable,
            "-m",
            "behave",
            "--tags",
            tag,
            "--format",
            formato,
            "--outfile",
            str(archivo),
        ]

        resultado = subprocess.run(
            comando,
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        assert resultado.returncode == 0, (
            f"Falló Behave con {tag} y formato {formato}.\n"
            f"Salida:\n{resultado.stdout}\n"
            f"Error:\n{resultado.stderr}"
        )

        assert archivo.exists(), (
            f"No se generó el reporte: {archivo}"
        )

    datos = json.loads(reporte_json.read_text(encoding="utf-8"))
    generar_reporte_html(datos, reporte_html, tag)

    assert reporte_html.exists(), (
        f"No se generó el reporte HTML: {reporte_html}"
    )