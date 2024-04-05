from typing import List, Union
from datetime import date, datetime
from abc import ABC, abstractmethod

from pessoa_fisica import PessoaFisica
from cliente import ICliente
from transacao import Transacao

class Cliente():
    def __init__(self, endereco: str):
        self._endereco: str = endereco

        self._contas: List[Conta]

    @property
    def endereco(self):
        return self._endereco or None
    
    @endereco.setter
    def mudar_endereco(self, endereco):
        self._endereco = endereco or ''

    @property
    def contas(self):
        return self._contas or []

    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)
         
class PessoaFisica(ICliente):
    def __init__(
        self, 
        endereco: str,  
        cpf: str, 
        nome: str, 
        data_nascimento: date,
        senha: str
    ):
        super().__init__(endereco)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
        self._senha = senha

class Conta:
    def __init__(self, numero: int, agencia: str, cliete, saldo: float = 0) -> None:
        self._saldo: float = saldo
        self._numero: int = numero
        self._agencia: str = agencia
        self._cliente = cliete
        self._historico: Historico

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> float:
        return self._numero
    
    @property
    def agencia(self) -> float:
        return self._agencia
    
    @property
    def cliente(self) -> float:
        return self._cliente
    
    @property
    def historico(self) -> float:
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero: int, agencia: str):
        return cls(cliete = cliente, numero = numero, agencia = agencia)

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
        
class ContaCorrente(Conta):
    def __init__(
        self, 
        numero: int, 
        agencia: str, 
        cliete,
        limite: float = 500,
        limite_saques: int = 3,
    ) -> None:
        super().__init__(numero, agencia, cliete)
        self._limite: float = limite
        self._limite_saques: int = limite_saques

    def sacar(self, valor):
        numerosaques = len(transacao for transacao in self.historico.transacoes if transacao["valor"] < 0)

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class ITransacao(ABC):
    @abstractmethod
    def __init__(self, data: date, valor: float, conta: Conta) -> None:
        self._conta = Conta
        self._data: date = date
        self._valor: float = valor

    @abstractmethod
    def registrar(conta: Conta):
        pass

def fazer_cadastro():
    CPF = int(input("Qual o seu CPF (Apenas os números)?\n"))

    if not verifica_CPF(CPF): 
        valores = {}

        name = input("Informe seu nome completo\n")
        valores["Nome"] = name
        
        dia = int(input("O dia do seu nascimento:  "))
        mes = int(input("O mês:  "))
        ano = int(input("Do ano:  "))
        valores["Data de Nascimento"] = datetime(ano, mes, dia)
        
        print("Nos informe seu endereço para concluir o cadastro")
        logradouro = str(input("O logradouro:  "))
        numero_residencia = str(input("O nº da residência:  "))
        bairro = str(input("O bairro:  "))
        cidade = str(input("A cidade:  "))
        sigla_estado = str(input("A sigla do Estado:  "))
        endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
        valores["Endereço"] = endereco
        
        print("Cadastrado!!!")
      
        senha = input("Crie uma senha:\n")
        valores["Senha"] = senha
        pessoa_fisica = PessoaFisica(**valores)
        clientes.append(pessoa_fisica)
    else:
        print("Você já está cadastrado!!!")

    return CPF

def verifica_CPF(CPF: str) -> bool: 
    for user in clientes:
        if user._cpf == CPF:
            return True

menu = """Escolha uma opção:
    1 - Depositar
    2 - Sacar
    3 - Visualizar extrato
    4 - Nova conta
    5 - Listar contas
    6 - Cadastrar novo usuário
    0 - Sair/Finalizar
"""  

clientes: List[ICliente] = []

while True:
    opcao_cadastro = int(input("""
    Bem-vindo(a) ao nosso banco!!!
    
    |Digite - 1| = Se já tem um cadastro e deseja fazer login.
    |Digite - 2| = Se ainda não tem um e gostaria de fazer o cadastro.
    |Digite - 0| = Se gostaria de sair.
    """))

    # if opcao_cadastro == 1:
    #     acesso = autenticar(usuarios)

    if opcao_cadastro == 2:
        fazer_cadastro()
        
    # if Acesso == 1:
    #     opcao_operacao = int(input("""
    #     |Digite - 1| = Se gostaria de fazer uma operação
    #     |Digite - 2| = Se gostaria de criar uma nova conta
    #     |Digite - 0| = Se gostaria de sair.
                                
    # """))

    #     if opcao_operacao == 1:
    #         while True:
    #             opcao = int(input(menu))

    #             if opcao == 1:
    #                 valor = float(input("Qual o valor a ser depositado?\n"))
    #                 extrato_deposito = float()
    #                 extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

    #             elif opcao == 2:
    #                 while True:
    #                     valor = float(input("Qual o valor a sar sacado?\n"))
    #                     saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
    #                     print(f"Seu saldo é de R$ {float(saldo):.2f}")

    #                     if numero_saques >= limite_saques:
    #                         break
                        
    #                     print("Gostaria de fazer outro saque?\n")
    #                     print("     | 0 - NÃO |\n")
    #                     outro_saque = int(input("     | 1 - SIM |\n"))

    #                     if outro_saque == 0:
    #                         break

    #             elif opcao == 3:
    #                 print("===========EXTRATO===========\n")
    #                 vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

    #             else:
    #                 break 

    #     elif opcao_operacao == 2:
    #         criar_conta(usuario)
    #         print("Conta criada!!!")
        print(clientes)

    # if (opcao_cadastro == 0) or (Acesso == 1):
    #     break

    # if Acesso == 1:
    #     opcao_operacao = int(input("""
    #     |Digite - 1| = Se gostaria de fazer uma operação
    #     |Digite - 2| = Se gostaria de criar uma nova conta
    #     |Digite - 0| = Se gostaria de sair.
                                
    # """))

    #     if opcao_operacao == 1:
    #         while True:
    #             opcao = int(input(menu))

    #             if opcao == 1:
    #                 valor = float(input("Qual o valor a ser depositado?\n"))
    #                 extrato_deposito = float()
    #                 extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

    #             elif opcao == 2:
    #                 while True:
    #                     valor = float(input("Qual o valor a sar sacado?\n"))
    #                     saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
    #                     print(f"Seu saldo é de R$ {float(saldo):.2f}")

    #                     if numero_saques >= limite_saques:
    #                         break
                        
    #                     print("Gostaria de fazer outro saque?\n")
    #                     print("     | 0 - NÃO |\n")
    #                     outro_saque = int(input("     | 1 - SIM |\n"))

    #                     if outro_saque == 0:
    #                         break

    #             elif opcao == 3:
    #                 print("===========EXTRATO===========\n")
    #                 vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

    #             else:
    #                 break 

    #     elif opcao_operacao == 2:
    #         criar_conta(usuario)
    #         print("Conta criada!!!")

    print("Obrigado por usar nosso serviço!!!")


