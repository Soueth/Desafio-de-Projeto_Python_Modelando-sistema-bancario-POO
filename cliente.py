from typing import List, TypeVar, Union

from interfaces.transacao_interface import ITransacao

from conta_corrente import ContaCorrente
class Cliente():
    def __init__(self, endereco: str):
        self._endereco: str = endereco
        self._contas: List[ContaCorrente] = []

    @property
    def endereco(self):
        return self._endereco or None
    
    @endereco.setter
    def mudar_endereco(self, endereco):
        self._endereco = endereco or ''

    @property
    def contas(self) :
        return self._contas
    
    def criar_conta(
        self, 
        numero: int, 
        agencia: str, 
        limite: float = None, 
        limite_saques: int = None, 
        saldo: int = None
    ):
        conta = ContaCorrente(numero, agencia, limite, limite_saques, saldo)
        print(f"Conta criada!!!\n{conta}")
        self._contas.append(conta)