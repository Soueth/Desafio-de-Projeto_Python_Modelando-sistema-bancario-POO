from typing import List

from transacao import Transacao
from conta import Conta

class Historico:
    def __init__(self, conta: Conta) -> None:
        self._transacoes: List[Transacao]
        self._conta: Conta = conta

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)