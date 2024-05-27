MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

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
        EXTRATO.append("Depósito: R$ {valor}")
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
    print("\n================ EXTRATO ================")
    if not EXTRATO:
        print("Não foram realizadas movimentações.")
    else:
        print("\n".join(EXTRATO))
    print(f"\nSaldo: R$ {SALDO:.2f}")
    print("==========================================")

def sair():
    return False

OPCOES = {
    "d": depositar,
    "s": sacar,
    "e": extrato,
    "q": sair
}

while True:
    opcao = input(MENU)
    if opcao in OPCOES:
        if OPCOES[opcao]() == False:
            break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
