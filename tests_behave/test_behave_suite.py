import json
import subprocess
import sys
from html import escape
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT_DIR / "reports"



def generar_reporte_html(datos, destino, tag):
    """Genera un reporte HTML profesional a partir del JSON de Behave."""

    escenarios = []

    for feature in datos:
        nombre_feature = feature.get("name", "Característica")

        for escenario in feature.get("elements", []):
            if escenario.get("type") != "scenario":
                continue

            nombre = escenario.get("name", "Sin nombre")
            estado = escenario.get("status", "unknown")

            pasos = escenario.get("steps", [])
            total_pasos = len(pasos)
            pasos_ok = sum(
                1 for paso in pasos
                if paso.get("result", {}).get("status") == "passed"
            )

            escenarios.append({
                "feature": nombre_feature,
                "name": nombre,
                "status": estado,
                "steps": total_pasos,
                "steps_ok": pasos_ok,
                "location": escenario.get("location", "")
            })

    total = len(escenarios)
    aprobados = sum(1 for e in escenarios if e["status"] == "passed")
    fallidos = sum(1 for e in escenarios if e["status"] == "failed")
    omitidos = sum(
        1 for e in escenarios
        if e["status"] in ("skipped", "undefined", "untested")
    )

    porcentaje = (aprobados / total * 100) if total else 0

    if fallidos:
        resultado_general = "FAILED"
    elif total and aprobados == total:
        resultado_general = "PASSED"
    else:
        resultado_general = "INCOMPLETE"

    filas = []

    for e in escenarios:
        estado = e["status"].upper()

        filas.append(
            f"<tr>"
            f"<td>{escape(e['feature'])}</td>"
            f"<td>{escape(e['name'])}</td>"
            f"<td><span class='status {escape(e['status'])}'>"
            f"{escape(estado)}</span></td>"
            f"<td>{e['steps_ok']} / {e['steps']}</td>"
            f"<td>{escape(e['location'])}</td>"
            f"</tr>"
        )

    contenido = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QA Automation - {escape(tag)}</title>

<style>
* {{ box-sizing: border-box; }}

body {{
    font-family: Arial, sans-serif;
    background: #f4f6fa;
    color: #263238;
    margin: 0;
    padding: 30px;
}}

.container {{
    max-width: 1100px;
    margin: auto;
}}

header {{
    background: #172554;
    color: white;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
}}

header h1 {{ margin: 0 0 10px; }}

.cards {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 15px;
    margin-bottom: 25px;
}}

.card {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px #0000000d;
}}

.card h2 {{
    font-size: 30px;
    margin: 8px 0;
}}

.approved {{ color: #15803d; }}
.failed {{ color: #dc2626; }}
.skipped {{ color: #d97706; }}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 10px;
    overflow: hidden;
}}

th, td {{
    padding: 13px;
    text-align: left;
    border-bottom: 1px solid #e5e7eb;
}}

th {{
    background: #e8edf5;
}}

.status {{
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
}}

.status.passed {{
    background: #dcfce7;
    color: #166534;
}}

.status.failed {{
    background: #fee2e2;
    color: #991b1b;
}}

.status.skipped, .status.undefined, .status.untested {{
    background: #fef3c7;
    color: #92400e;
}}

.status.unknown {{
    background: #e5e7eb;
    color: #374151;
}}

footer {{
    margin-top: 25px;
    color: #64748b;
    font-size: 12px;
}}

@media (max-width: 700px) {{
    body {{ padding: 12px; }}
    table {{ font-size: 12px; }}
    th, td {{ padding: 8px; }}
}}
</style>
</head>

<body>
<div class="container">

<header>
    <h1>QA Automation</h1>
    <p>Reporte de pruebas BDD - Behave</p>
    <p>Suite ejecutada: {escape(tag)}</p>
    <p>Resultado general: <strong>{resultado_general}</strong></p>
</header>

<section class="cards">

<div class="card">
    <p>Total de escenarios</p>
    <h2>{total}</h2>
</div>

<div class="card">
    <p>Escenarios aprobados</p>
    <h2 class="approved">{aprobados}</h2>
</div>

<div class="card">
    <p>Escenarios fallidos</p>
    <h2 class="failed">{fallidos}</h2>
</div>

<div class="card">
    <p>Escenarios omitidos</p>
    <h2 class="skipped">{omitidos}</h2>
</div>

<div class="card">
    <p>Porcentaje de aprobación</p>
    <h2>{porcentaje:.1f}%</h2>
</div>

</section>

<h2>Detalle de escenarios</h2>

<table>
<thead>
<tr>
    <th>Característica</th>
    <th>Escenario</th>
    <th>Estado</th>
    <th>Pasos aprobados</th>
    <th>Ubicación</th>
</tr>
</thead>

<tbody>
{''.join(filas) if filas else '<tr><td colspan="5">No se encontraron escenarios.</td></tr>'}
</tbody>
</table>

<footer>
    <p>Proyecto: QA Automation</p>
    <p>Herramienta: Behave + Pytest + Selenium</p>
    <p>Reporte generado automáticamente.</p>
</footer>

</div>
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