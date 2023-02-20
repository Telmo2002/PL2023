from tabulate import tabulate
from CSV_Parse import Parse
import matplotlib.pyplot as plt

def main():
    parser = Parse()
    parser.saveInfo("myheart.csv")
    parser.distSexo()
    parser.distEtaria()
    parser.distColesterol()
    

    while(1):
        print("-------------- TPC1 --------------")
        ops = {"1":"Tabela relativa à distribuição da doença por sexo.",
               "2":"Tabela relativa à distribuição da doença por escalões etários.",
               "3":"Tabela relativa à distribuição da doença por níveis de colesterol.",
               "4":"Gráfico relativo à distribuição da doença por sexo.",
               "5":"Gráfico relativo à distribuição da doença por escalões etários.",
               "6":"Gráfico relativo à distribuição da doença por níveis de colesterol.",
               "7":"Sair."}
        
        # Dar print a menu
        for op in ops:
            print(op + ": " + ops.get(op))
        print()
        
        op = input("Escolha uma das opções acima: ")
        print()
        
        if(op == "1"):
            results = parser.distribPSexo
        if(op == "2"):
            results = parser.escaloes
        if(op == "3"):
            results = parser.LvlColestrol
        if(op == "4"):
            labels = ["M", "F"]
            plt.bar(labels, parser.distribPSexo, width = 0.8)

            plt.xlabel('Sexo')
            plt.ylabel('Nº de Doentes')
            plt.title('Distribuição da doença por sexo')
            # Mostrar o gráfico
            plt.show()
            continue
        if(op == "5"):
            plt.bar(parser.escaloes, parser.escaloesValues, width = 0.8)

            plt.xlabel('Escalão Etário')
            plt.ylabel('Nº de Doentes')
            plt.title('Distribuição da doença por escalões etários.')
            # Mostrar o gráfico
            plt.show()
            continue
        if(op == "6"):
            plt.bar(parser.lvl, parser.LvlColestrol, width = 0.8)

            plt.xlabel('Nível de Colesterol')
            plt.ylabel('Nº de Doentes')
            plt.title('Distribuição da doença por níveis de colesterol.')
            # Mostrar o gráfico
            plt.show()
            continue
        if(op == "7"):
            break
            
        # Lista vazia para guardar os resultados
        table = list()
        
        if(op == "1"): 
            table = [["M", parser.distribPSexo[0]], ["F", parser.distribPSexo[1]]]
            print(tabulate(table, headers=["Sexo", "Nº de Doentes"]))
            print()
            print()
        
        if(op == "2"):
            i = 0
            for escalao in parser.escaloes:
                table.append([escalao,parser.escaloesValues[i]])
                i+=1

            print(tabulate(table, headers=["Escalão Etário", "Nº de Doentes"]))
            print()
            print()

        if(op == "3"):
            i = 0
            for lvl in parser.lvl:
                table.append([lvl, parser.LvlColestrol[i]])
                i+=1

            print(tabulate(table, headers=["Nível de Colesterol", "Nº de Doentes"]))
            print()
            print()

    print()
    print("------- See you soon!! -------")
    print()


if __name__ == "__main__":
    main()        
        