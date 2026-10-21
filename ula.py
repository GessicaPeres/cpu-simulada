"""
ULA — Unidade Lógica e Aritmética (8 bits)
AOC 2026.2
"""

"""
aqui, a ula será tradada como uma função pura que não altera nenhum estado, 
apenas recebe os parâmetros e retorna o resultado. Quem guardará o resultado
é o registrador destino em cpu.py
"""

def limitar_8bits(valor):
    return valor & 0xFF #AND bit a bit com 0xFF (11111111) para manter apenas os 8 bits menos significativos


def ula(operacao, a, b=0): #executa uma operação de ULA sobre dois valores de 8 bits
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    if operacao == "ADD":
        resultado = a + b
    elif operacao == "SUB":
        resultado = a - b      # negativo vira complemento de 2 no limitar
    elif operacao == "AND":
        resultado = a & b
    elif operacao == "OR":
        resultado = a | b
    elif operacao == "XOR":
        resultado = a ^ b
    else:
        raise ValueError(f"Operação inválida: {operacao}")

    return limitar_8bits(resultado) #o resultado passa pelo limitar_8bits para garantir que seja um valor de 8 bits 

