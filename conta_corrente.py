from cliente import ICliente
from conta import Conta

class ContaCorrente(Conta):
    def __init__(
        self, 
        numero: int, 
        agencia: str, 
        cliete: ICliente,
        limite: float = 1000,
        limite_saques: int = 3,
        saldo: float = 0
    ) -> None:
        super().__init__(numero, agencia, cliete, saldo)
        self._limite: float = limite
        self._limite_saques: int = limite_saques

    