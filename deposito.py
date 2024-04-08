from datetime import date, datetime
from typing import Literal
from interfaces.transacao_interface import ITransacao


class Deposito(ITransacao):
    def __init__(self, valor: float) -> None:
        self._data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self._valor = valor
        self._tipo = 'deposito'
    @property
    def data(self) -> date:
        return self._data
    
    @property
    def valor(self) -> float:
        return self._valor
    
    @classmethod
    def registrar(cls, data: date, valor: float):
        return cls(data, valor)