from datetime import datetime
from typing import List, Union, TypeVar
from abc import ABC

from interfaces.transacao_interface import ITransacao
from pessoa_fisica import PessoaFisica

Conta = TypeVar('Conta')
Cliente = TypeVar('Cliente')
class App(ABC):
    clientes: List[Union['Cliente']] = []

    def __init__(self) -> None:
        self._acesso: int

    @property
    def acesso(self) -> int:
        return self._acesso
    
    @acesso.setter
    def acesso(self, acesso: int) -> None:
        self._acesso = acesso

    def main(self):
        menu = """Escolha uma opção:
            1 - Depositar
            2 - Sacar
            3 - Visualizar extrato
            0 - Sair/Finalizar
        """      

        cliente: Union['Cliente'] 

        while True:
            opcao_cadastro = int(input("""
                Bem-vindo(a) ao nosso banco!!!
                
                |Digite - 1| = Se já tem um cadastro e deseja fazer login.
                |Digite - 2| = Se gostaria de criar um novo usuário.
                |Digite - 3| = Se gostaria de listar todos os usuarios.
                |Digite - 0| = Se gostaria de sair.
            """))

            if opcao_cadastro == 1:
                self.acesso, cliente = autenticar(self.clientes)

            if opcao_cadastro == 2:
                # self.clientes.append(fazer_cadastro(self.clientes))
                cliente = fazer_cadastro(self.clientes)
                if cliente:
                    self.clientes.append(cliente)

            if opcao_cadastro == 3:
                for cliente in self.clientes:
                    print(cliente)

            if (opcao_cadastro == 0) or (self.acesso == 1):
                break

        if self.acesso == 1:
            opcao_operacao = int(input("""
                |Digite - 1| = Se gostaria de fazer uma operação.
                |Digite - 2| = Se gostaria de criar uma nova conta.
                |Digite - 3| = Se gostaria de listar suas contas.
                |Digite - 0| = Se gostaria de sair.                       
            """))

            if opcao_operacao == 1:
                conta: Union['Conta']
                while True:
                    conta = logar_conta(self.clientes)
                    if conta:
                        break

                while (conta):
                    opcao = int(input(menu))

                    if opcao == 1:
                        valor = float(input("Qual o valor a ser depositado?\n"))
                        extrato_deposito = float()
                        extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

                    # if opcao == 1:
                    #     valor = float(input("Qual o valor a ser depositado?\n"))
                    #     extrato_deposito = float()
                    #     extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

                    # elif opcao == 2:
                    #     while True:
                    #         valor = float(input("Qual o valor a sar sacado?\n"))
                    #         saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
                    #         print(f"Seu saldo é de R$ {float(saldo):.2f}")

                    #         if numero_saques >= limite_saques:
                    #             break
                            
                    #         print("Gostaria de fazer outro saque?\n")
                    #         print("     | 0 - NÃO |\n")
                    #         outro_saque = int(input("     | 1 - SIM |\n"))

                    #         if outro_saque == 0:
                    #             break

                    # elif opcao == 3:
                    #     print("===========EXTRATO===========\n")
                    #     vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

                    # else:
                    #     break 

            elif opcao_operacao == 2:
                criar_conta()
                print("Conta criada!!!")
        
        print("Obrigado por usar nosso serviço!!!")

def fazer_cadastro(clientes: List[Union['Cliente']]):
    cpf = str(input('Qual seu CPF (apenas os números)?'))

    if not verifica_CPF(cpf, clientes): 
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
        return pessoa_fisica
    else:
        print("Você já está cadastrado!!!")

def criar_conta(cliente: Union['Cliente']):
    agencia = str(input('Qual a agência?'))

    limite_mudar = int(input('Seu limite pré-aprovado é de R$ 1000,00! Se gostaria de mudá-lo | Digite 1 |'))
    if limite_mudar == 1:
        limite = float(input('Qual o valor do limite que gostaria de ter?'))

    numero = cliente.contas.length

    return ()


def verifica_CPF(CPF: str, contas: List[Union['Conta']]) -> bool: 
    for conta in contas:
        if conta._cpf == CPF:
            return True
        
def verifica_nome(nome: str, clientes: List[Union['Cliente']]):
    for cliente in clientes:
        if cliente._nome == nome:
            return True

        
def autenticar(clientes: List[Union['Cliente']]):
    Acesso_concedido = 0
    cpf = str(input("Insira o seu CPF (Apenas os números) "))
    senha = int(input("insira uma senha "))
    
    for cliente in clientes:
        if cliente._cpf == cpf:
            true_key = int(cliente.get("Senha"))
            print(true_key)

            if true_key == senha:
                return 1, cliente

            else:
                print("Senha Incorreta!!\n")

        else: 
            print("Usuário Incorreto ou não existe!!")

def logar_conta(contas: List[Union['Conta']]):
    Acesso_concedido = 0
    agencia = str(input("Insira a agência"))
    numero = int(input("O número da conta"))
    
    for conta in contas:
        if conta.agencia == agencia & conta.numero == numero:
            return conta
        
        else:
            print("Conta não existente!!\n")

    # if agencia in contas:
    #     true_key = int(usuarios.get(username).get("Senha"))
    #     print(true_key)

    #     if true_key == senha:
    #         Acesso_concedido = 1

    #     else:
    #         print("Senha Incorreta!!\n")

    

    return Acesso_concedido
# def fazer_cadastro():
#     CPF = int(input("Qual o seu CPF (Apenas os números)?\n"))

#     if not verifica_CPF(CPF): 
#         valores = {}

#         name = input("Informe seu nome completo\n")
#         valores["Nome"] = name
        
#         dia = int(input("O dia do seu nascimento:  "))
#         mes = int(input("O mês:  "))
#         ano = int(input("Do ano:  "))
#         valores["Data de Nascimento"] = datetime(ano, mes, dia)
        
#         print("Nos informe seu endereço para concluir o cadastro")
#         logradouro = str(input("O logradouro:  "))
#         numero_residencia = str(input("O nº da residência:  "))
#         bairro = str(input("O bairro:  "))
#         cidade = str(input("A cidade:  "))
#         sigla_estado = str(input("A sigla do Estado:  "))
#         endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
#         valores["Endereço"] = endereco
        
#         print("Cadastrado!!!")
      
#         senha = input("Crie uma senha:\n")
#         valores["Senha"] = senha
#         pessoa_fisica = PessoaFisica(**valores)
#         clientes.append(pessoa_fisica)
#     else:
#         print("Você já está cadastrado!!!")

#     return CPF

# def verifica_CPF(CPF: str) -> bool: 
#     for user in clientes:
#         if user._cpf == CPF:
#             return True