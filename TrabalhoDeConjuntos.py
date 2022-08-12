f = open("trabalhos.txt", 'r')
conjuntos = f.readlines()


qtd = int(conjuntos[0])
"""
int(input("Quantas operações você irá fazer? \n"))
"""

x = 0

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

    """ CRIADO MATRIZ Item x Item
    mat = []
    matriz = []
    for i in range(0, len(colunas)):
        for c in range(0, len(linhas)):
            mat.append([linhas[i],colunas[c]])
    print("O resultado de seus PONTOS CARTESIANOS é ")
    for i in range(0, len(mat)):
        if i % len(colunas) == 0 and i != 0:
            print("\n")
            print(mat[i],end = " ")
        else:
            print(mat[i],end =" ")
"""

""" COMEÇO """



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




"""  
    oper = input("Qual operação você deseja fazer? \n união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C) \n").upper()

    valores1 = input("Qual os valores do primeiro conjunto? \n").replace(" ",",")
    valores2 = input("Qual os valores do segundo conjunto? \n").replace(" ",",")

    val1 = valores1.split(",")
    val2 = valores2.split(",")

    if oper == "U":
        uniao(val1,val2)
    elif oper == "I":
        inter(val1,val2)
    elif oper == "D":
        difer(val1,val2)
    elif oper == "C":
        cart(val1,val2)

    x = x + 1
"""