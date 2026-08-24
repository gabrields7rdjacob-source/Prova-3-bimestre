import json
import datetime

def carregar_conta():
    try:
        with open("conta.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def salvar_conta(conta):
    try:
        with open("conta.json", "w", encoding="utf-8") as f:
            json.dump(conta, f, ensure_ascii=False, indent=2)
        print("✔️ Conta guardada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao guardar: {e}")

def depositar(conta, valor):
    if valor <= 0:
        print("❌ O valor deve ser positivo.")
        return
    conta["saldo"] += valor
    conta["historico"].append(f"Depósito de R$ {valor:.2f}")
    print(f"✔️ Depósito realizado, seu saldo atual é: R$ {conta['saldo']:.2f}")

def sacar(conta, valor):
    if valor <= 0:
        print("❌ O valor deve ser positivo")
        return
    if valor > conta["saldo"]:
        print("❌ Saldo insuficiente")
        return
    conta["saldo"] -= valor
    conta["historico"].append(f"Levantamento de R$ {valor:.2f}")
    print(f"✔️ Levantamento realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def extrato(conta):
    print(f"\n--- EXTRATO DE {conta['titular'].upper()} ---")
    if not conta["historico"]:
        print("Nenhuma movimentação por enquanto")
    else:
        for movimentacao in conta["historico"]:
            print(f"  {movimentacao}")
    print(f"--- Saldo atual: R$ {conta['saldo']:.2f}")

print("--- Pybank ---")
conta = carregar_conta()

if conta is None:
    print("--- Cadastro ---")
    nome_input = input("Digite o seu nome: ")
    cpf_input = int(input("Digite seu CPF: "))
    print("--- Informações para Contato ---")
    cell_inp = int(input("Digite seu Número de Telefone: "))
    email_inp = input("Digite seu Email: ")
    endereco_inp = input("Digitre seu endereço: ")
    print("--- Informações Pessoais ---")
    idade_inp = int(input("Digite  sua Idade: "))
    civil_inp = input("Estado Civil: ")
    conta = {
        "titular": nome_input,
        "cpf": cpf_input,
        "telefone": cell_inp,
        "email": email_inp,
        "endereço": endereco_inp,
        "idade": idade_inp,
        "estado civil": civil_inp,
        "saldo": 0.0,
        "historico": []
    }
else:
    print(f"Bem-vindo {conta['titular']}!")

while True:
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    opcao = input("[1] Depositar | [2] Levantar | [3] Extrato | [4] Guardar e Sair: ")
    
    if opcao == "1" or opcao == "2":
        try:
            valor = float(input("Valor: R$ "))
        except ValueError:
            print("❌ Digite um número válido")
            continue
        if opcao == "1":
            depositar(conta, valor)
        else:
            sacar(conta, valor)
            
    elif opcao == "3":
        extrato(conta)
        
    elif opcao == "4":
        salvar_conta(conta)
        break
        
    else:
        print("❌ Opção inválida")
