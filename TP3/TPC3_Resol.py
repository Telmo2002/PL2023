import re
import json

def savefile(filename):
    pattern = r"(?P<ProcID>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nomePai>[a-zA-Z ]+)::(?P<nomeMae>[a-zA-Z ]+)::(?P<obs>.*)::"
    regex = re.compile(pattern)
    data = []
    with open(filename, 'r') as file:
        for line in file:
            match = regex.finditer(line)
            if match:
                data += [m.groupdict() for m in match]
    return data


# A.
def processosPorAno(data):
    processosPorAnoDict = dict()

    for elem in data:
        year = elem.get("ano")
        if year:
            if year not in processosPorAnoDict:
                processosPorAnoDict[year] = 1
            else:
                processosPorAnoDict[year] += 1

    print(processosPorAnoDict)

processosPorAno(savefile("processos.txt"))  

# B.

def simplifyName(name):
    return re.match(r"\w+\b", name).group(), re.search(r"\b\w+$", name).group()

def freqNomesT5(parsed_list, seculo, nome_id):

    dictNomesT5 = dict()
    for d in parsed_list:
        if (100 * (seculo - 1) + 1) <= int(d["ano"]) <= (100 * seculo):
            nome = simplifyName(d["nome"])
            pai = simplifyName(d["nomePai"])
            mae = simplifyName(d["nomeMae"])

            for n in [nome, pai, mae]:
                if n[nome_id] not in dictNomesT5:
                    dictNomesT5[n[nome_id]] = 0
                dictNomesT5[n[nome_id]] += 1

    return sorted(dictNomesT5.items(), key=lambda x: x[1], reverse=True)[:5]

def top5NS(data):
    firstNamesT5 = dict()
    lastNamesT5 = dict()
    for seculo in range(1, 22):
        firstNamesT5[(100 * (seculo - 1) + 1, 100 * seculo)] = freqNomesT5(data, seculo, 0)
        lastNamesT5[(100 * (seculo - 1) + 1, 100 * seculo)] = freqNomesT5(data, seculo, 1)

    print(firstNamesT5)
    print(lastNamesT5)

# C.
def frequencyOFrelationships(data):
    regex1 = re.compile(r",[\w\s]+.[\s*](?i:Proc)|,[\w\s]+.[:]+")
    regex2 = re.compile(r".[\s*](?i:Proc.)")
    parentesco = dict()

    for d in data:
        match = regex1.findall(d["obs"])
        if match:
            for elem in match:
                pos = elem.find(".")
                elem = elem[1:-(len(elem) - pos)]

                if elem not in parentesco:
                    parentesco[elem] = 0

                parentesco[elem] += 1

    print(parentesco)


# D.
def convertTojson(data, outputFile):
    if ".json" not in outputFile:
        outputFile = outputFile + ".json"

    file = open(outputFile, "w")
    file.write("[\n")

    for i in range(min(20, len(data))):
        json.dump(data[i], file, indent=3, separators=(',', ': '))
        if i != min(19, len(data)-1):
            file.write(",\n")
    file.write("\n]")

    file.close()

data = savefile("processos.txt")
print("------------------ #A ------------------\n")
processosPorAno(data)
print("\n")
print("\n")
print("------------------ #B ------------------\n")
top5NS(data)
print("\n")
print("\n")
print("------------------ #C ------------------\n")
frequencyOFrelationships(data)
print("\n")
print("\n")
print("------------------ #D ------------------\n")
print("Ficheiro Criado...")
convertTojson(savefile("processos.txt"), "ficheiroJsonC")