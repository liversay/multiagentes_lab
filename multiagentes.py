import asyncio
import subprocess
import sys
from pathlib import Path

from mcp import Client
from mcp.types import TextContent
from mcp_requisitos import mcp
from ollama import chat

MODELO = "qwen2.5-coder:3b"
EVID = Path("evidencias")
EVID.mkdir(exist_ok=True)

async def leer_requisito():
    async with Client(mcp) as cliente:
        resultado = await cliente.call_tool(
            "requisito_prioridad", {}
        )
        if resultado.is_error:
            raise RuntimeError("Falló la herramienta MCP")
        return "\n".join(
            x.text for x in resultado.content
            if isinstance(x, TextContent)
        )

def consultar(rol, instruccion, datos):
    respuesta = chat(
        model=MODELO,
        messages=[
            {"role": "system", "content": instruccion},
            {"role": "user", "content": datos},
        ],
    )
    return respuesta.message.content or ""

async def proponer():
    req = await leer_requisito()
    base = Path("tareas.py").read_text(encoding="utf-8")
    plan = consultar(
        "planificador",
        "Eres planificador. Responde solo en texto, sin bloques de "
        "código ni ejemplos en Python. No inventes requisitos ni "
        "funciones que el REQUISITO MCP no pida. Usa estas secciones: "
        "1) Contrato de API, incluyendo lo que se conserva. "
        "2) Prioridades permitidas. 3) Valor por defecto. "
        "4) Rechazo de valores inválidos. 5) Pasos. "
        "6) Criterios de aceptación y pruebas.",
        "REQUISITO MCP:\n" + req + "\nCÓDIGO:\n" + base,
    )
    (EVID / "01_plan.md").write_text(plan, encoding="utf-8")
    propuesta = consultar(
        "implementador",
        "Eres implementador. Propón tareas.py y tests completos. "
        "Conserva API antigua; no uses paquetes externos.",
        "REQUISITO:\n" + req + "\nPLAN:\n" + plan
        + "\nCÓDIGO ACTUAL:\n" + base,
    )
    (EVID / "02_propuesta.md").write_text(
        propuesta, encoding="utf-8"
    )
    print("Revise 01_plan.md y 02_propuesta.md.")

async def revisar():
    req = await leer_requisito()
    pruebas = subprocess.run(
        [sys.executable, "-m", "unittest", "discover",
         "-s", "tests", "-v"],
        capture_output=True, text=True, timeout=30,
    )
    evidencia = ("REQUISITO:\n" + req
        + "\nCÓDIGO:\n" + Path("tareas.py").read_text()
        + "\nTESTS:\n" + Path("tests/test_tareas.py").read_text()
        + "\nRESULTADO:\n" + pruebas.stdout + pruebas.stderr)
    informe = consultar(
        "revisor",
        "Evalúa requisito, seguridad y pruebas. Señala faltantes; "
        "no afirmes que todo pasa si no hay evidencia.",
        evidencia,
    )
    (EVID / "03_revision.md").write_text(
        informe, encoding="utf-8"
    )
    print("Exit code pruebas:", pruebas.returncode)
    print("Revise evidencias/03_revision.md")

if __name__ == "__main__":
    modo = input("Modo (proponer/revisar): ").strip()
    asyncio.run(revisar() if modo == "revisar" else proponer())
