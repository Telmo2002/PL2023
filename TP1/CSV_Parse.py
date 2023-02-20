# import csv

# class Parse:



#     def __init__(self):
#         self.pacientes = dict() # Dicionário com a informação geral dos pacientes
#         self.size = 0 # Número de pacientes
#         self.distribPSexo = list() # Array tamanho 2 para distribuição por sexo
#         self.escaloes = list() # Array com tamanho igual ao número de escalões disponíveis
#         self.LvlColestrol = list() # Array com tamanho igual ao nmr de niveis de colestrol existentes

    


    
    
    
#     with open('myheart.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)

#     #max = 0
#         i=0
#         next(reader)
#         min = 100
#         for row in reader:
#             print(row[3])
#             #if int(row[0]) < min:
#                 #min = int(row[0])
        

#     print(min)

class Parse:
    
    def __init__(self):
        self.pacientes = dict()
        self.distribPSexo = [0,0]
        self.escaloesValues = list()
        self.escaloes = list()
        self.maxIdade = 0
        self.minIdade = 0
        self.LvlColestrol = list()
        self.lvl = list()
        self.maxColesterol = 0
        self.minColesterol = 0


    # Função que guarda a informação do ficheiro
    def saveInfo(self, file):
        with open(file, 'r') as csv_file:
            lines = csv_file.readlines()
            #self.pacientes = dict() Se der erro verificar
            i = 1
            for line in lines[1:]:
                row = line.strip().split(',')
                if row[5] == "1":
                    # idade,sexo,tensão,colesterol,batimento,temDoença
                    #   0     1     2       3           4       5
                    #pacientes = dict()
                    if "D" not in self.pacientes:
                        self.pacientes["D"] = []
                    #if i not in self.pacientes["D"]:
                    #    self.pacientes["D"][i] = []
                    self.pacientes["D"].append({"idade":int(row[0]), "sexo":row[1], "tensão":int(row[2]), "colesterol":int(row[3]), "batimento":int(row[4])})
                    
                else:
                    if "ND" not in self.pacientes:
                        self.pacientes["ND"] = []
                    #if i not in self.pacientes["ND"]:
                    #    self.pacientes["ND"][i] = []
                    self.pacientes["ND"].append({"idade":int(row[0]), "sexo":row[1], "tensão":int(row[2]), "colesterol":int(row[3]), "batimento":int(row[4])})
                i+=1

    # Função que calcula a distribuição da doença por sexo;    

    def distSexo(self):

        for paciente in self.pacientes["D"]:
            if(paciente["sexo"] == "M"): self.distribPSexo[0]+=1
            else: self.distribPSexo[1]+=1
        

    # Auxiliar
    def valuesIdade(self): 
        idades = []
        for paciente in self.pacientes["D"]:
            idades.append(paciente["idade"])
        self.maxIdade = max(idades)
        self.minIdade = min(idades)

    # Função que calcula a distribuição da doença por escalões etários.

    def distEtaria(self):
        self.valuesIdade() 
        
        # Descobrir onde começa o primeiro escalão
        escalao = 5 * (self.minIdade // 5)
        escalaoI = escalao
        # Assumir que o primeiro escalão começa em 30
        i = 0
        # counter = 30 # -> Começo do primeiro escalão
        while(escalao < self.maxIdade):
            (self.escaloesValues).append(0)
            #self.escaloes.append("["+)
            i+=1
            self.escaloes.append("[" + str(escalao) + "," + str(escalao+4) + "]")
            escalao+=5
        
        # Encontrar o escalão respetivo e incrementar
        for paciente in self.pacientes["D"]:
            self.escaloesValues[(paciente["idade"] - escalaoI)//5]+=1

    
    # Auxiliar
    def valueColesterol(self): 
        colesterolValues = []
        for paciente in self.pacientes["D"]:
            colesterolValues.append(paciente["colesterol"])
        self.maxColesterol = max(colesterolValues)
        self.minColesterol = min(colesterolValues)
        #return max(colesterolValues)




    # função que calcula a distribuição da doença por níveis de colesterol. (Cada nível abrange 10 unidades)
    def distColesterol(self):
        self.valueColesterol()

        # Descobrir o primeiro nível, no caso será 0
        nivel = 10 * (self.minColesterol // 10)
        nivelI = nivel # Guardar o primeiro nível
        i = 0
        #nivel = 0 # -> Começo do primeiro nivel
        while(nivel < self.maxColesterol):
            (self.LvlColestrol).append(0)
            self.lvl.append("[" + str(nivel) + "," + str(nivel+9) + "]")
            i+=1
            nivel+=10
        
        # Encontrar o nível respetivo e incrementar
        for paciente in self.pacientes["D"]:
            self.LvlColestrol[(paciente["colesterol"] - nivelI)//10]+=1


    

