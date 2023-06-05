#Definição de variáveis globais
qtdCedulasCem = 100
qtdCedulasCinquenta = 100
qtdCedulasVinte = 100
qtdCedulasDez = 100
qtdCedulasCinco = 100
qtdcedulasDois = 100
qtdCedulasUm = 100

# Saldo inicial do Terminal
saldoTerminal = ((100 * qtdCedulasCem) + (50 * qtdCedulasCinquenta) 
+ (20 * qtdCedulasVinte) + (10 * qtdCedulasDez) + (5 * qtdCedulasCinco) 
+ (2 * qtdcedulasDois) + (1 * qtdCedulasUm))

extratoDeposito = 0
extratoSaque = 0
historicoDeposito = []
historicoSaque = []

def saldoTerminalBancario():
    print()
    print("---- Iniciando consulta no Terminal Bancário ----")

    global qtdCedulasCem
    global qtdCedulasCinquenta
    global qtdCedulasVinte
    global qtdCedulasDez
    global qtdCedulasCinco
    global qtdcedulasDois
    global qtdCedulasUm

    global saldoTerminal

    saldoTerminal = ((100 * qtdCedulasCem) + (50 * qtdCedulasCinquenta) 
    + (20 * qtdCedulasVinte) + (10 * qtdCedulasDez) + (5 * qtdCedulasCinco) 
    + (2 * qtdcedulasDois) + (1 * qtdCedulasUm))

    print()
    print(f"Saldo atual do terminal: R${saldoTerminal}")
    print()
    print(f"Histório de depósitos realizados no terminal:\n {historicoDeposito}")
    print()
    print(f"Histório de saques realizados no terminal:\n {historicoSaque}")

    print()
    print("---- Quantidade de cédulas disponíveis no terminal: ----")
    print(f"Cédulas de R$100: {qtdCedulasCem}")
    print(f"Cédulas de R$50: {qtdCedulasCinquenta}")
    print(f"Cédulas de R$20: {qtdCedulasVinte}")
    print(f"Cédulas de R$10: {qtdCedulasDez}")
    print(f"Cédulas de R$5: {qtdCedulasCinco}")
    print(f"Cédulas de R$2: {qtdcedulasDois}")
    print(f"Cédulas de R$1: {qtdCedulasUm}")

    print()
    print("---- Operação Finalizada ----")
    print()

    return main()

def deposito():
    print()
    global qtdCedulasCem
    global qtdCedulasCinquenta
    global qtdCedulasVinte
    global qtdCedulasDez
    global qtdCedulasCinco
    global qtdcedulasDois
    global qtdCedulasUm
    global extratoDeposito
    global historicoDeposito

    qtdCedulasCemDepositados = 0
    qtdCedulasCinquentaDepositados = 0
    qtdCedulasVinteDepositados = 0
    qtdCedulasDezDepositados = 0
    qtdCedulasCincoDepositados = 0
    qtdCedulasDoisDepositados = 0
    qtdCedulasUmDepositados = 0

    var_temp = 0

    print("--- Iniciando a operação de depósito ----")
    print()
    valor_pretendido = int(input("Qual o valor total do depósito? "))

    while var_temp < valor_pretendido:
        print("Apenas depósitos de cédulas inteiras, por vez: ")
        print("R$100, R$50, R$20, R$10, R$5, R$2, R$1")
        print()
        cedula_escolhida = int(input("Escolha a cédula para a operação de depósito: "))
        qtdCedulas = int(input("Insira a quantidade de cédulas: "))

        if cedula_escolhida == 100:
            qtdCedulasCemDepositados += qtdCedulas

        if cedula_escolhida == 50:
            qtdCedulasCinquentaDepositados += qtdCedulas

        if cedula_escolhida == 20:  
            qtdCedulasVinteDepositados += qtdCedulas

        if cedula_escolhida == 10:
            qtdCedulasDezDepositados += qtdCedulas

        if cedula_escolhida == 5:
            qtdCedulasCincoDepositados += qtdCedulas

        if cedula_escolhida == 2:
            qtdCedulasDoisDepositados += qtdCedulas

        if cedula_escolhida == 1:
            qtdCedulasUmDepositados += qtdCedulas

        var_temp += cedula_escolhida * qtdCedulas
        extratoDeposito = ((100 * qtdCedulasCemDepositados) + (50 * qtdCedulasCinquentaDepositados) 
        + (20 * qtdCedulasVinteDepositados) + (10 * qtdCedulasDezDepositados) + (5 * qtdCedulasCincoDepositados) 
        + (2 * qtdCedulasDoisDepositados) + (1 * qtdCedulasUmDepositados))

        print(f"Depósito temporário: R${extratoDeposito}\n")
        
    extratoDeposito = ((100 * qtdCedulasCemDepositados) + (50 * qtdCedulasCinquentaDepositados) 
    + (20 * qtdCedulasVinteDepositados) + (10 * qtdCedulasDezDepositados) + (5 * qtdCedulasCincoDepositados) 
    + (2 * qtdCedulasDoisDepositados) + (1 * qtdCedulasUmDepositados))

    historicoDeposito.append(extratoDeposito)

    print("Finalizado o depósito de cédulas para o valor desejado.")
    print()
    print(f"Valor total do depósito: R${extratoDeposito}")
    
    qtdCedulasCem += qtdCedulasCemDepositados
    qtdCedulasCinquenta += qtdCedulasCinquentaDepositados
    qtdCedulasVinte += qtdCedulasVinteDepositados
    qtdCedulasDez += qtdCedulasDezDepositados
    qtdCedulasCinco += qtdCedulasCincoDepositados
    qtdcedulasDois += qtdCedulasDoisDepositados
    qtdCedulasUm += qtdCedulasUmDepositados

    print()
    print("---- Operação Finalizada ----")
    print()

    return main()

def saque():
    print()
    global qtdCedulasCem
    global qtdCedulasCinquenta
    global qtdCedulasVinte
    global qtdCedulasDez
    global qtdCedulasCinco
    global qtdcedulasDois
    global qtdCedulasUm
    global extratoSaque
    global historicoSaque

    qtdCedulasCemSacados = 0
    qtdCedulasCinquentaSacados = 0
    qtdCedulasVinteSacados = 0
    qtdCedulasDezSacados = 0
    qtdCedulasCincoSacados = 0
    qtdCedulasDoisSacados = 0
    qtdCedulasUmSacados = 0
    op_saque = 0

    valor_flutuante = 0

    print("---- Iniciando a operação de saque! ----")
    print()
    valorParaSacar = int(input("Insira o valor desejado para realizar a operação: "))
    
    valor_flutuante = valorParaSacar

    qtd_cem = 0
    qtd_cinquenta = 0
    qtd_vinte = 0
    qtd_dez = 0
    qtd_cinco = 0
    qtd_dois =0
    qtd_um = 0

    if (valorParaSacar <= saldoTerminal):

        while valor_flutuante >= 100:
            valor_flutuante -= 100
            qtd_cem += 1

        while valor_flutuante >= 50: 
            qtd_cinquenta += 1
            valor_flutuante -= 50 
 
        while valor_flutuante >= 20:
            valor_flutuante -= 20 
            qtd_vinte += 1
        
        while valor_flutuante >= 10:
            valor_flutuante -= 10
            qtd_dez += 1
    
        while valor_flutuante >= 5:
            valor_flutuante -= 5
            qtd_cinco += 1
    
        while valor_flutuante >= 2:
            valor_flutuante -= 2
            qtd_dois += 1
    
        while valor_flutuante >= 1:
            valor_flutuante -= 1
            qtd_um += 1

        if qtd_cem >0:
            print(f' Total de {qtd_cem} cédulas de R$ 100 ')
            qtdCedulasCemSacados += qtd_cem

        if qtd_cinquenta >0:
            print(f' Total de {qtd_cinquenta} cédulas R$ 50 ')
            qtdCedulasCinquentaSacados += qtd_cinquenta

        if qtd_vinte >0:
            print(f' Total de {qtd_vinte} cédulas de R$20 ')
            qtdCedulasVinteSacados += qtd_vinte

        if qtd_dez>0:
            print(f' Total de {qtd_dez} cédulas R$ 10 ')
            qtdCedulasDezSacados += qtd_dez

        if qtd_cinco >0:
            print(f' Total de {qtd_cinco} cédulas de R$5 ')
            qtdCedulasCincoSacados += qtd_cinco

        if qtd_dois>0:
            print(f' Total de {qtd_dois} cédulas de R$2 ')
            qtdCedulasDoisSacados += qtd_dois

        if qtd_um >0:
            print(f' Total de {qtd_um} cédulas de R$1 ')
            qtdCedulasUmSacados += qtd_um


    extratoSaque = ((100 * qtdCedulasCemSacados) + (50 * qtdCedulasCinquentaSacados) 
    + (20 * qtdCedulasVinteSacados) + (10 * qtdCedulasDezSacados) + (5 * qtdCedulasCincoSacados) 
    + (2 * qtdCedulasDoisSacados) + (1 * qtdCedulasUmSacados)) * (-1)

    historicoSaque.append(extratoSaque)

    print(f" Saque efetuado nesta operação: R${extratoSaque}\n")

    qtdCedulasCem -= qtdCedulasCemSacados
    qtdCedulasCinquenta -= qtdCedulasCinquentaSacados
    qtdCedulasVinte -= qtdCedulasVinteSacados
    qtdCedulasDez -= qtdCedulasDezSacados
    qtdCedulasCinco -= qtdCedulasCincoSacados
    qtdcedulasDois -= qtdCedulasDoisSacados
    qtdCedulasUm -= qtdCedulasUmSacados

    print()

    return main()

def main():
    print("--- Terminal Bancário ---")
    print()
    print(f'PARA REALIZAR UM DEPÓSITO, DIGITE 1' ) 
    print(f'PARA REALIZAR UM SAQUE, DIGITE 2')
    print(f'PARA CONSULTAR SALDO E HISTÓRICOS, DIGITE 3')
    print(f'PARA ENCERRAR OPERAÇÕES, DIGITE 4')
    print()
    pergunta = int(input("O que deseja fazer? "))

    if pergunta == 1:
        return deposito()
      
    if pergunta == 2:
        return saque()
    
    if pergunta == 3:
        return saldoTerminalBancario()
        
    if pergunta == 4:
        print("Encerrado as operações no terminal!\n Passar bem!")

    if pergunta > 5 or pergunta <= 0:
        print('Digite novamente')
        return main()
    
main()