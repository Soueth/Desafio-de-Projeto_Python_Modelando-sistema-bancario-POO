from abc import ABC, abstractmethod
from datetime import date

from ..conta import Conta

class ITransacao(ABC):
    @abstractmethod
    def __init__(self, data: date, valor: float, conta: Conta) -> None:
        self._conta = Conta
        self._data: date = date
        self._valor: float = valor

    @abstractmethod
    def registrar(conta: Conta):
        pass