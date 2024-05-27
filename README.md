# Sistema Bancário Simples

Este é um programa Python simples que simula algumas operações bancárias básicas. O usuário pode depositar dinheiro, sacar dinheiro e ver o extrato da conta.

## Variáveis Globais

- `SALDO`: Armazena o saldo atual da conta.
- `LIMITE`: Define o limite de saque.
- `EXTRATO`: Armazena o histórico de transações.
- `NUMERO_SAQUES`: Conta o número de saques realizados.
- `LIMITE_SAQUES`: Define o número máximo de saques permitidos.

## Funções

- `depositar()`: Solicita ao usuário que informe o valor do depósito. Se o valor for maior que 0, ele é adicionado ao saldo e registrado no extrato. Se o valor for 0 ou negativo, a função informa que a operação falhou.

- `sacar()`: Solicita ao usuário que informe o valor do saque. Verifica se o valor excede o saldo ou o limite de saque. Se qualquer uma dessas condições for verdadeira, a função informa que a operação falhou. Se o valor for maior que 0 e nenhuma das condições acima for verdadeira, o valor é subtraído do saldo, registrado no extrato e o número de saques é incrementado.

## Como usar

Execute o script Python e siga as instruções na tela para realizar operações bancárias.
