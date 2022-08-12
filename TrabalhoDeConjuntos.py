f = open("trabalhos.txt", 'r')
conjuntos = f.readlines()

qtd = int(conjuntos[0])

def printar(x,y,z):
    for c in range(len(y)):
        print(y[c])

def uniao(value1, value2):
    lista1 = value1.replace("\n","").replace(" ","").split(",")
    lista2 = value2.replace("\n","").replace(" ","").split(",")
    for i in lista1:
        for x in lista2:
            if x == i:
                lista2.remove(x)
    for i in range(len(lista2)):
        lista1.append(lista2[i])

    s = ",".join([str(i) for i in lista1])
    print("O resultado da sua UNIÃO é ")
    print("{"+s+"}")

def inter(value1, value2):
    lista1 = value1.replace("\n", "").replace(" ", "").split(",")
    lista2 = value2.replace("\n", "").replace(" ", "").split(",")
    lista = []
    for i in lista1:
        for x in lista2:
            if i == x:
                lista.append(i)

    s = ",".join([str(i) for i in lista])
    print("O resultado da sua INTERSECÇÃO é ")
    print("{" + s + "}")


def difer(value1,value2):
    lista1 = value1.replace("\n", "").replace(" ", "").split(",")
    lista2 = value2.replace("\n", "").replace(" ", "").split(",")
    lista = []
    for i in lista1:
        for x in lista2:
            if i == x:
                lista.append(i)
    for i in lista:
        lista1.remove(i)

    s = ",".join([str(i) for i in lista1])
    print("O resultado da sua DIFERENÇA é ")
    print("{" + s + "}")

def cart(linhas,colunas):
    lista1 = linhas.replace("\n", "").replace(" ", "").split(",")
    lista2 = colunas.replace("\n", "").replace(" ", "").split(",")
    print("O Resultado dos seus PRODUTOS CARTESIANOS é ")
    for i in lista1:
        for c in lista2:
            print("(" + i + c + ")", end=",")

for i in range(1, len(conjuntos), 3):
    oper = conjuntos[i]
    valores1 = conjuntos[i+1]
    valores2 = conjuntos[i+2]
    operacao = oper.replace("\n","")
    val1 = valores1
    val2 = valores2

    if operacao == "U":
        uniao(val1, val2)
    elif operacao == "I":
        inter(val1, val2)
    elif operacao == "D":
        difer(val1, val2)
    elif operacao == "C":
        cart(val1, val2)
