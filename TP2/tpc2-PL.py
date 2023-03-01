def somatext():
    text = input("Introduza aqui o texto: \n")
    
    isON = True
    word = ""
    number = ""
    soma = 0
    lastChar = ""
    s = 1 # Contar as somas

    for char in text:
        if char.isalpha():
            if char.lower() == "o":
                word+=char
            if char.lower() == "f":
                word+=char
                if lastChar.lower() == "f":
                    if word.lower() == "off":
                        isON = False
                        word = ""
                    else: word = ""
            
            if char.lower() == "n":
                word+=char
                if word.lower() == "on":
                    isON = True
                    word = ""
                else: word = ""
            if lastChar.isnumeric() and isON:
                soma += int(number)
                number = ""

            lastChar = char


        elif char.isnumeric() and isON:
            number+=char
            lastChar = char

            
        
        elif char == "=":
            if lastChar.isnumeric(): # Acrescentar o numero antes do = à soma
                soma += int(number)
            print("O resultado da " + str(s) +  "ª soma é " + str(soma) + ".")
            s+=1
            #break # Terminar logo após imprimir o resultado

        else:
            if lastChar.isnumeric() and isON:
                soma += int(number)
                number = "" 
            word = ""
            lastChar = char

somatext()
