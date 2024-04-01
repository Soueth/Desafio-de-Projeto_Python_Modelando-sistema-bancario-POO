from typing import List
from datetime import datetime

from interfaces.cliente_interface import ICLiente
from pessoa_fisica import PessoaFisica

menu = """Escolha uma opção:
    1 - Depositar
    2 - Sacar
    3 - Visualizar extrato
    4 - Nova conta
    5 - Listar contas
    6 - Cadastrar novo usuário
    0 - Sair/Finalizar
"""  

clientes: List[ICLiente] = []

while True:
    opcao_cadastro = int(input("""
    Bem-vindo(a) ao nosso banco!!!
    
    |Digite - 1| = Se já tem um cadastro e deseja fazer login.
    |Digite - 2| = Se ainda não tem um e gostaria de fazer o cadastro.
    |Digite - 0| = Se gostaria de sair.
    """))

    if opcao_cadastro == 1:
        acesso = autenticar(usuarios)

    elif opcao_cadastro == 2:
        fazer_cadastro(usuarios, usuario)
        print(usuarios)

    if (opcao_cadastro == 0) or (Acesso == 1):
        break

    if Acesso == 1:
        opcao_operacao = int(input("""
        |Digite - 1| = Se gostaria de fazer uma operação
        |Digite - 2| = Se gostaria de criar uma nova conta
        |Digite - 0| = Se gostaria de sair.
                                
    """))

        if opcao_operacao == 1:
            while True:
                opcao = int(input(menu))

                if opcao == 1:
                    valor = float(input("Qual o valor a ser depositado?\n"))
                    extrato_deposito = float()
                    extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

                elif opcao == 2:
                    while True:
                        valor = float(input("Qual o valor a sar sacado?\n"))
                        saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
                        print(f"Seu saldo é de R$ {float(saldo):.2f}")

                        if numero_saques >= limite_saques:
                            break
                        
                        print("Gostaria de fazer outro saque?\n")
                        print("     | 0 - NÃO |\n")
                        outro_saque = int(input("     | 1 - SIM |\n"))

                        if outro_saque == 0:
                            break

                elif opcao == 3:
                    print("===========EXTRATO===========\n")
                    vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

                else:
                    break 

        elif opcao_operacao == 2:
            criar_conta(usuario)
            print("Conta criada!!!")

    print("Obrigado por usar nosso serviço!!!")

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
    
    else:
        print("Você já está cadastrado!!!")

    return CPF

def verifica_CPF(CPF: str) -> bool: 
    for user in clientes:
        if user._cpf == CPF:
            return True
