"""
PROGRAMAS — programas usados nos testes e na demonstração
AOC 2026.2
"""

#programa do enunciado: 5 + 8 -> MEM[15] = 13
PROGRAMA_EXEMPLO = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT",
]

#usa LOAD, STORE, ADD, SUB, AND, OR, XOR.

PROGRAMA_PROPRIO = [
    "LOAD R0, 12",     # 00: R0 = 12  (00001100)
    "LOAD R1, 10",     # 01: R1 = 10  (00001010)
    "LOAD R2, 12",     # 02: R2 = 12  (cópia de R0)
    "ADD R0, R1",      # 03: R0 = 12 + 10 = 22
    "SUB R2, R1",      # 04: R2 = 12 - 10 = 2
    "STORE R0, 14",    # 05: MEM[14] = 22
    "LOAD R3, 12",     # 06: R3 = 12
    "AND R3, R1",      # 07: R3 = 12 AND 10 = 8
    "XOR R1, R3",      # 08: R1 = 10 XOR 8 = 2
    "STORE R3, 15",    # 09: MEM[15] = 8
    "HALT",            # 10
]
#final esperado: R0=22, R1=2, R2=2, R3=8, MEM[14]=22, MEM[15]=8