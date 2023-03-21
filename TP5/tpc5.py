import re
from sys import stdin

def saldoF(saldoAtual):
    euro = 0
    cent = 0

    euro = int(saldoAtual/100)
    cent = int(saldoAtual%(euro*100)) 
    if euro == 0:
        return (str(cent) + "c")
    else: 
        return (str(euro) + "e" + str(cent) + "c")

def moedinhaF():

    moedasValidas = []
    moedasNvalidas = []
    saldo = 0 # Em centimos
    moedinha = ["5c","10c", "20c", "50c", "1e", "2e"]
    flag = 0
    for command in stdin:
        if command == "LEVANTAR\n" and flag == 0:
            flag = 1
            print("maq:\"Introduza as moedas.\"")
        if command == "ABORTAR\n" and flag == 1:
            flag = 0
            print("Volte sempre!\n")
            print(f"Saldo: {saldoF(saldo)}")
            break
        
        if re.match(r"MOEDA\s", command) and flag == 1:
            moedas = re.findall(r'\d+\w', command)
            for m in moedas:
                if m in moedinha:
                    moedasValidas.append(m)
                else:
                    moedasNvalidas.append(m)

            for m in moedasValidas:
                if m == "5c":
                    saldo+=5
                if m == "10c":
                    saldo+=10
                elif m == "20c":
                    saldo+=20
                elif m == "50c":
                    saldo+=50
                elif m == "1e":
                    saldo+=100
                elif m == "2e":
                    saldo+=200
            print(f"maq:\"Conjunto de moedas inválidas: {moedasNvalidas}. Saldo: {saldoF(saldo)}\"")

        if command[0] == "T" and flag == 1:
            if re.match(r"T=601\d+|T=641\d+", command):
                print("maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"")
            elif re.match(r"T=00", command):
                if saldo >= 150:
                    saldo-=150
                    flag = 2
                    print("A chamar...\n")
                else:
                    print("Saldo Insuficiente para a realização deste tipo de chamadas! Saldo Mínimo necessário: 1e50c")
            elif re.match(r"T=2\d+", command):
                if saldo >= 25:
                    saldo-=25
                    flag = 2
                    print("A chamar...\n")
                else:
                    print("Saldo Insuficiente para a realização deste tipo de chamadas! Saldo Mínimo necessário: 25c")
            elif re.match(r"T=800\d+", command):
                flag = 2
                print("A chamar...\n")
            elif re.match(r"T=805\d+", command):
                if saldo >= 10:
                    saldo-=10
                    flag = 2
                    print("A chamar...\n")
                else:
                    print("Saldo Insuficiente para a realização deste tipo de chamadas! Saldo Mínimo necessário: 10c")

        if command == "POUSAR\n" and flag == 1:
            print("maq:\"Queira introduzir um número antes de terminar a chamada!\"")
        elif command == "POUSAR\n" and flag == 2:
            flag == 0
            print(f"maq: Chamada Terminada. Volte sempre! Troco: {saldoF(saldo)}\"")
            break

moedinhaF()

