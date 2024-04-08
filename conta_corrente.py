from conta import Conta

class ContaCorrente(Conta):
    def __init__(
        self, 
        numero: int, 
        agencia: str, 
        limite: float = 1000,
        limite_saques: int = 3,
        saldo: float = 0
    ) -> None:
        super().__init__(numero, agencia, saldo)
        self._limite: float = limite
        self._limite_saques: int = limite_saques
        self._saques: int

    @property
    def saques(self):
        return self._saques
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def saldo(self):
        return self._saldo

    @saques.getter
    def adicionar_saque(self):
        self._saques += 1


    @Conta.saldo.setter
    def sacar(self, valor: float) -> str:
        if valor > self._saldo:
            print("O valor a ser sacado não pode ser maior do que o saldo!!!\n")
            print(f"SALDO: {float(self._saldo):.2f}\n")
            return
        if valor <= 0:
            print("Valores iguais a zero ou negativos não podem ser sacados!!!\n")
            return
        if self._saques < self._limite_saques:
            print('O limite de saques já foi atingido! Tente denovo amanhã.')
            return
        if valor > self.limite:
            print('O valor não pode ser maior do que seu limite, que é de R${self.limite}!')
            return
        
        self._saldo -= valor
        self.adicionar_saque
        self.historico.adicionar_transacao(valor, 'saque')

        print(f'Saque bem sucedido! Seu saldo atual é de {self._saldo:.2f}.')
        return self._limite_saques > self.saques