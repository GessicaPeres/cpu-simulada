"""
TESTES — AOC 2026.2
Execute: python testes.py
"""

import contextlib #pra redirecionar a saída para não poluir os testes
import io #para criar um arquivo de saída em memória (StringIO)

from cpu import CPU
from ula import ula
from programas import PROGRAMA_EXEMPLO, PROGRAMA_PROPRIO

def rodar(programa):
    """roda um programa sem poluir a saída com o passo a passo"""
    cpu = CPU()
    cpu.carregar_programa(programa)
    with contextlib.redirect_stdout(io.StringIO()):
        cpu.executar()
    return cpu


#ULA
def teste_ula():
    assert ula("ADD", 5, 8) == 13
    assert ula("ADD", 250, 10) == 4          #overflow -> 8 bits
    assert ula("SUB", 8, 5) == 3
    assert ula("SUB", 5, 8) == 253           #negativo -> complemento de 2
    assert ula("AND", 0b1100, 0b1010) == 0b1000
    assert ula("OR", 0b1100, 0b1010) == 0b1110
    assert ula("XOR", 0b1100, 0b1010) == 0b0110
    try:
        ula("MUL", 1, 2)
        assert False
    except ValueError:
        pass
    print("[OK] ULA")


#instruções de teste: LOAD, STORE, ADD, SUB, AND, OR, XOR, JMP e HALT
def teste_load():
    cpu = rodar(["LOAD R0, 25", "HALT"])
    assert cpu.registradores["R0"] == 25
    assert rodar(["LOAD R1, 300", "HALT"]).registradores["R1"] == 44  #300 & 0xFF
    print("[OK] LOAD")


def teste_store():
    cpu = rodar(["LOAD R2, 77", "STORE R2, 15", "HALT"])
    assert cpu.memoria[15] == 77
    print("[OK] STORE")


def teste_add():
    cpu = rodar(["LOAD R0, 5", "LOAD R1, 8", "ADD R0, R1", "HALT"])
    assert cpu.registradores["R0"] == 13
    assert cpu.registradores["R1"] == 8
    cpu = rodar(["LOAD R0, 200", "LOAD R1, 100", "ADD R0, R1", "HALT"])
    assert cpu.registradores["R0"] == 44    #300 -> 8 bits
    print("[OK] ADD")


def teste_sub():
    cpu = rodar(["LOAD R0, 8", "LOAD R1, 5", "SUB R0, R1", "HALT"])
    assert cpu.registradores["R0"] == 3
    cpu = rodar(["LOAD R0, 5", "LOAD R1, 8", "SUB R0, R1", "HALT"])
    assert cpu.registradores["R0"] == 253
    print("[OK] SUB")


def teste_logicas():
    base = ["LOAD R0, 12", "LOAD R1, 10"]
    assert rodar(base + ["AND R0, R1", "HALT"]).registradores["R0"] == 8
    assert rodar(base + ["OR R0, R1", "HALT"]).registradores["R0"] == 14
    assert rodar(base + ["XOR R0, R1", "HALT"]).registradores["R0"] == 6
    print("[OK] AND / OR / XOR")


def teste_pc():
    cpu = CPU()
    cpu.carregar_programa(["LOAD R0, 1", "LOAD R1, 2", "HALT"])
    with contextlib.redirect_stdout(io.StringIO()):
        cpu.ciclo()
        assert cpu.pc == 1
        cpu.ciclo()
        assert cpu.pc == 2
    print("[OK] PC avança")


def teste_jmp():
    cpu = rodar(["LOAD R0, 10", "JMP 4", "LOAD R0, 99", "HALT",
                 "LOAD R1, 20", "HALT"])
    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20
    print("[OK] JMP")


def teste_halt():
    cpu = rodar(["HALT"])
    assert cpu.halted is True
    cpu = rodar(["LOAD R0, 1", "HALT", "LOAD R0, 2"])
    assert cpu.registradores["R0"] == 1     #nada dps de HALT executa
    print("[OK] HALT")


def teste_programa_exemplo():
    cpu = rodar(PROGRAMA_EXEMPLO)
    assert cpu.memoria[15] == 13
    print("[OK] Programa de exemplo (MEM[15] = 13)")


def teste_programa_proprio():
    cpu = rodar(PROGRAMA_PROPRIO)
    r = cpu.registradores
    assert (r["R0"], r["R1"], r["R2"], r["R3"]) == (22, 2, 2, 8)
    assert cpu.memoria[14] == 22 and cpu.memoria[15] == 8
    print("[OK] Programa próprio")


def teste_erros():
    for prog in (["LOAD R9, 1"], ["STORE R0, 16"], ["FOO R0, R1"], ["JMP 20"]):
        try:
            rodar(prog)
            assert False, prog
        except ValueError:
            pass
    print("[OK] Erros tratados")


if __name__ == "__main__":
    print("Executando testes...\n")
    teste_ula()
    teste_load()
    teste_store()
    teste_add()
    teste_sub()
    teste_logicas()
    teste_pc()
    teste_jmp()
    teste_halt()
    teste_programa_exemplo()
    teste_programa_proprio()
    teste_erros()
    print("\nTodos os testes foram aprovados.")