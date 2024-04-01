from typing import Union

from interfaces.cliente_interface import ICliente
from historico import Historico

class Conta:
    def __init__(self, numero: int, agencia: str, cliete: Union[ICliente], saldo: float = 0) -> None:
        self._saldo: float = saldo
        self._numero: int = numero
        self._agencia: str = agencia
        self._cliente: Union[ICliente] = cliete
        self._historico: Historico

    @property
    def saldo(self) -> float:
        return self._saldo or 0
    
    @staticmethod
    def nova_conta(cliente: ICliente, numero: int, agencia: str):
        return Conta(cliete = cliente, numero = numero, agencia = agencia)

    @saldo.setter
    def sacar(self, valor: float) -> str:
        if valor > self._saldo:
            print("O valor a ser sacado não pode ser maior do que o saldo!!!\n")
            print(f"SALDO: {float(self._saldo):.2f}\n")
    
        elif valor <= 0:
            print("Valores iguais a zero ou negativos não podem ser sacados!!!\n")

        else:
            self._saldo -= valor

        return f'Saque bem sucedido! Seu saldo atual é de {self._saldo}.'
    
    @saldo.setter
    def depositar(self, valor: float) -> float: 
        if valor <= 0:
            print("Não se pode depositar valores iguais ou menores do que zero")
 
        else:
            self._saldo += valor
            return self._saldo