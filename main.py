"""
MAIN — execução e visualização passo a passo
AOC 2026.2

Uso:
    python main.py              -> programa do enunciado (5 + 8)
    python main.py proprio      -> programa próprio (10 instruções)
    python main.py passo        -> programa próprio, um ciclo por ENTER
"""

import sys
from cpu import CPU
from programas import PROGRAMA_EXEMPLO, PROGRAMA_PROPRIO

modo = sys.argv[1] if len(sys.argv) > 1 else "exemplo"

cpu = CPU()
cpu.carregar_programa(PROGRAMA_EXEMPLO if modo == "exemplo" else PROGRAMA_PROPRIO)

print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

if modo == "passo":
    cpu.executar_passo_a_passo()
else:
    cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")
cpu.mostrar_estado()
print()
if modo == "exemplo":
    print("MEM[15] =", cpu.memoria[15])
else:
    print("MEM[14] =", cpu.memoria[14])
    print("MEM[15] =", cpu.memoria[15])