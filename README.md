# CPU Simulada de 8 bits

Trabalho prático de Arquitetura de Computadores (AOC 2026.2) — UFC Sobral.

## Arquitetura

- Largura dos dados: 8 bits (0 a 255)
- Registradores: R0, R1, R2 e R3
- Memória: 16 posições (endereços 0 a 15)
- PC: Contador de programa (4 bits)
- ULA: ADD, SUB, AND, OR e XOR
- Ciclo: Fetch → Decode → Execute

A memória é uma só(Arquitetura de Von Neumann): cada posição guarda ou uma instrução (string) ou um dado (número). O Fetch lê MEM[PC] como instrução, o STORE mexe nas posições como dados.

### Instruções

- LOAD — `LOAD R0, 5` — valor imediato → registrador
- STORE — `STORE R0, 15` — registrador → memória
- ADD — `ADD R0, R1` — `R0 ← R0 + R1`
- SUB — `SUB R0, R1` — `R0 ← R0 − R1`
- AND — `AND R0, R1` — `R0 ← R0 AND R1`
- OR — `OR R0, R1` — `R0 ← R0 OR R1`
- XOR — `XOR R0, R1` — `R0 ← R0 XOR R1`
- JMP — `JMP 8` — `PC ← 8`
- HALT — `HALT` — encerra a execução

## Execução

Requisito: Python 3.8+. Sem dependências externas.

```bash
python main.py            #programa do enunciado (5 + 8 → MEM[15] = 13)
python testes.py          #12 testes automatizados