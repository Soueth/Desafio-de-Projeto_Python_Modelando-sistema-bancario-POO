from abc import ABC, abstractmethod
from datetime import date
from typing import Literal

class ITransacao(ABC):
    @abstractmethod
    def __init__(self, data: date, valor: float, tipo: Literal['deposito', 'saldo']) -> None:
        self._data: date = date
        self._valor: float = valor
        self._tipo: Literal['deposito','saldo'] = tipo

    @classmethod
    def registrar(cls, data: date, valor: float, tipo: Literal['deposito', 'saldo']):
        pass

    @property
    def data(self) -> date:
        return self._data
    
    @property
    def valor(self) -> float:
        return self._valor
    
    @property
    def tipo(self) -> Literal['deposito', 'saldo']:
        return self._tipo