
INTO = """
================ BANCO DIO =================

Seja bem-vindo ao Banco DIO! Como podemos te ajudar hoje?

[c] Criar conta
[l] Login
[q] Sair

============================================

=> """


MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

NOME = ""
CPF = ""
CC = 0
SALDO = float(0.00)
LIMITE = float(500.00)
EXTRATO = []
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3
 

def depositar():
    global SALDO, EXTRATO
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        SALDO += valor
        EXTRATO.append(f"Depósito: R$ {valor}")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar():
    global SALDO, EXTRATO, NUMERO_SAQUES
    valor = float(input("Informe o valor do saque: "))
    if valor > SALDO:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > LIMITE:
        print("Operação falhou! O valor do saque excede o limite.")
    elif NUMERO_SAQUES >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        SALDO -= valor
        EXTRATO.append(f"Saque: R$ {valor:.2f}")
        NUMERO_SAQUES += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def extrato():
    global NOME, CPF, CC, SALDO, EXTRATO
    print("\n================ EXTRATO ================")
    if not EXTRATO:
        print("Não foram realizadas movimentações.")
    else:
        print("\n".join(EXTRATO))
        print(f"\nNome: {NOME}")
        print(f"\nCPF: {CPF}")
        print(f"\nConta Corrente: {CC}")
        print(f"\nAgência: 0001")
        print(f"\n")
        print(f"\nSaldo: R$ {SALDO:.2f}")
        print("==========================================")

def criar_conta():
    global NOME, CPF, SALDO, LIMITE, EXTRATO, CC
    NOME = input("Informe o seu nome: ")
    CPF = input("Informe o seu CPF: ")
    SALDO = float(input("Informe o saldo inicial: "))
    LIMITE = float(input("Informe o limite de saque: "))
    EXTRATO = []
    #CC += 123
    print("Conta criada com sucesso!")
    
def login():
    global NOME, CPF, SALDO, LIMITE, EXTRATO, CC
    NOME2 = input("Informe o seu nome: ")
    CPF2 = input("Informe o seu CPF: ")
    if NOME2 == NOME and CPF2 == CPF:
        print("Login efetuado com sucesso!")
    else:
        print("Login falhou! Usuário ou senha inválidos.")
    opcao = input(INTO)

def sair():
    return False

OPCOES = {
    "d": depositar,
    "s": sacar,
    "q": sair,
    "e": extrato,
    "c": criar_conta,
    "l": login
}

while True:
    if CC > 0:
        opcao = input(MENU)
        if opcao in OPCOES:
            if OPCOES[opcao]() == False:
                break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    else:
        opcao = input(INTO)
        if opcao in OPCOES:
            if OPCOES[opcao]() == False:
                break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        CC += 1

