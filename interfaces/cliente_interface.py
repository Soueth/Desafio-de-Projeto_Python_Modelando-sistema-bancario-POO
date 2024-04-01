from abc import ABC
from typing import List
from ..conta import Conta
from transacao_interface import ITransacao

class ICliente(ABC):
    def __init__(self, endereco: str, conta: Conta):
        self._endereco: str = endereco

        self._contas: List[Conta]
        self._contas.append(conta)

    @property
    def endereco(self):
        return self._endereco or None
    
    @endereco.setter
    def mudar_endereco(self, endereco):
        self._endereco = endereco or ''

    @property
    def contas(self):
        return self._contas or []

    def realizar_transacao(conta: Conta, transacao: ITransacao):
        pass

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)