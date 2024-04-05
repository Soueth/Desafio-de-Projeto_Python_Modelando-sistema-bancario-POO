from typing import List, TypeVar, Union

from interfaces.transacao_interface import ITransacao


from conta import Conta
class Cliente():
    def __init__(self, endereco: str):
        self._endereco: str = endereco

        self._contas: List[Union[Conta]]

    @property
    def endereco(self):
        return self._endereco or None
    
    @endereco.setter
    def mudar_endereco(self, endereco):
        self._endereco = endereco or ''

    @property
    def contas(self) :
        return self._contas or []
    
    @contas.setter
    def criar_conta(
        self, 
        numero: int, 
        agencia: str, 
        limite: float = None, 
        limite_saques: int = None, 
        saldo: int = None
    ):
        self.contas.append(Conta(numero, agencia, limite, limite_saques, saldo))

    def realizar_transacao(conta: Union['Conta'], transacao: ITransacao):
        pass

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)