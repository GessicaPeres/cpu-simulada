"""
CPU SIMULADA
AOC 2026.2

CPU de 8 bits:
- 4 registradores: R0, R1, R2, R3
- memória com 16 posições
- PC (Program Counter)
- ULA
- instruções LOAD, STORE, ADD, SUB, AND, OR, XOR, JMP e HALT

No código-base, LOAD, JMP e HALT já estão implementados.
As demais instruções possuem partes para implementação.
"""

from ula import ula, limitar_8bits


class CPU:

    def __init__(self):
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # 16 posições de memória (instruções como texto ou dados como inteiros)
        self.memoria = [0] * 16

        # Program Counter
        self.pc = 0

        # Estado da CPU
        self.halted = False

  #funções auxiliares
    def _registrador(self, nome):
        """Valida o nome do registrador."""
        if nome not in self.registradores: #exemplo: "R0" in {"R0", "R1", "R2", "R3"} -> True
            raise ValueError(f"Registrador inválido: {nome}")
        return nome

    def _endereco(self, endereco):
        """valida um endereço de memória (0 a 15)"""
        if endereco < 0 or endereco >= len(self.memoria):
            raise ValueError(f"Endereço de memória inválido: {endereco}")
        return endereco

    def _operacao_ula(self, operacao, partes): #exemplo: operacao="ADD", partes=["ADD", "R0", "R1"]
        """OP Rd, Rs  ->  Rd <- Rd OP Rs (calculado pela ULA)."""
        destino = self._registrador(partes[1]) 
        origem = self._registrador(partes[2])

        a = self.registradores[destino]
        b = self.registradores[origem]

        self.registradores[destino] = ula(operacao, a, b)

        self.pc += 1


    def executar_instrucao(self, instrucao):

        partes = instrucao.replace(",", "").split() #exemplo: "LOAD R0, 5" -> ["LOAD", "R0", "5"]
        operacao = partes[0]

        # LOAD R0, 5  ->  R0 <- 5
        if operacao == "LOAD":
            registrador = self._registrador(partes[1]) #acessa o registrador, por exemplo "R0"
            valor = int(partes[2]) #int("5") -> 5
            self.registradores[registrador] = limitar_8bits(valor) #atualiza a entrada do registrador com o valor limitado a 8 bits
            self.pc += 1

        # STORE R0, 15  ->  MEM[15] <- R0
        elif operacao == "STORE":
            registrador = self._registrador(partes[1])
            endereco = self._endereco(int(partes[2]))
            self.memoria[endereco] = self.registradores[registrador] #lê o valor do registrador e armazena na memória no endereço especificado
            self.pc += 1

        # ADD / SUB / AND / OR / XOR  Rd, Rs  ->  Rd <- Rd OP Rs
        elif operacao in ("ADD", "SUB", "AND", "OR", "XOR"):
            self._operacao_ula(operacao, partes)

        # JMP 8  ->  PC <- 8
        elif operacao == "JMP":
            endereco = int(partes[1]) #endereço de destino do salto
            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de salto inválido")
            self.pc = endereco #substitui o valor do PC pelo endereço de salto

        # HALT  ->  encerra a execução
        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    #ciclo fetch-decode-execute
    def ciclo(self): #executa um ciclo completo da CPU: FETCH -> DECODE -> EXECUTE

        if self.halted:
            return

        #FETCH
        if self.pc < 0 or self.pc >= len(self.memoria):
            raise RuntimeError(f"PC fora da memória: {self.pc}")

        instrucao = self.memoria[self.pc]

        if not isinstance(instrucao, str):
            raise RuntimeError(
                f"MEM[{self.pc}] = {instrucao} não é uma instrução válida "
                "(o programa terminou sem HALT?)"
            )

        print()
        print("--------------------------------")
        print("FETCH")
        print(f"PC: {self.pc:02d}")
        print("Instrução:", instrucao)

        #DECODE + EXECUTE
        print("DECODE + EXECUTE")
        self.executar_instrucao(instrucao)

        #ESTADO
        self.mostrar_estado()

    def executar(self, max_ciclos=100):
        ciclos = 0
        while not self.halted:
            if ciclos >= max_ciclos:
                raise RuntimeError(
                    "Número máximo de ciclos atingido. "
                    "Verifique se existe um loop infinito."
                )
            self.ciclo()
            ciclos += 1

    def executar_passo_a_passo(self, max_ciclos=100):
        """Executa um ciclo por vez, esperando ENTER entre eles."""
        ciclos = 0
        while not self.halted:
            if ciclos >= max_ciclos:
                raise RuntimeError("Número máximo de ciclos atingido.")
            input("\n[ENTER] para executar o próximo ciclo...")
            self.ciclo()
            ciclos += 1

#utilitários para carregar programas e mostrar estado/memória
    def carregar_programa(self, programa):
        """Carrega uma lista de instruções a partir da posição 0."""
        if len(programa) > len(self.memoria):
            raise ValueError("Programa maior que a memória (16 posições)")
        for i, instrucao in enumerate(programa):
            self.memoria[i] = instrucao

    def mostrar_estado(self):
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")
        print(f"PC (próxima instrução): {self.pc:02d}")

    def mostrar_memoria(self):
        print("Memória:")
        for i, valor in enumerate(self.memoria):
            print(f"  [{i:02d}] {valor}")