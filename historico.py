from typing import List, Literal
from datetime import date

from deposito import Deposito
from interfaces.transacao_interface import ITransacao
from saque import Saque
# from conta import Conta

class Historico:
    pass
    def __init__(self) -> None:
        self._transacoes: List[ITransacao] = []

    def adicionar_transacao(self, valor, tipo: Literal['deposito', 'saque']):
        if tipo == 'saque':
            self._transacoes.append(Saque(valor))
        elif (tipo == 'deposito'):
            self._transacoes.append(Deposito(valor))

    def __str__(self) -> str:
        transacoes: str = ''

        for t in self._transacoes:
            transacoes += f'{t.tipo}: R${t.valor:.2f} às {t.data}\n'

        return transacoes