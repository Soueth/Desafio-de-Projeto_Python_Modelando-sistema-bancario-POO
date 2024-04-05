from typing import List

from interfaces.transacao_interface import ITransacao
# from conta import Conta

class Historico:
    pass
    def __init__(self) -> None:
        self._transacoes: List[ITransacao]

    def adicionar_transacao(self, valor, tipo):
        self._transacoes.append(ITransacao.registrar(valor, tipo))