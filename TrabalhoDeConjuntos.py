qtd = int(input("Quantas operações você irá fazer? \n"))
x = 0

def printar(x,y,z):
    for c in range(len(y)):
        print(y[c])

def uniao(value1, value2):

    for i in value1:
        for x in value2:
            if x == i:
                value2.remove(x)
    for i in range(len(value2)):
        value1.append(value2[i])

    value1
    s = ",".join([str(i) for i in value1])
    print("O resultado da sua UNIÃO é ")
    print("{"+s+"}")

def inter(value1, value2):
    lista = []
    for i in value1:
        for x in value2:
            if i == x:
                lista.append(i)

    s = ",".join([str(i) for i in lista])
    print("O resultado da sua INTERSECÇÃO é ")
    print("{" + s + "}")


def difer(value1,value2):
    lista = []
    for i in value1:
        for x in value2:
            if i == x:
                lista.append(i)
    for i in lista:
        value1.remove(i)

    s = ",".join([str(i) for i in value1])
    print("O resultado da sua DIFERENÇA é ")
    print("{" + s + "}")

def cart(linhas,colunas):
    """ CRIADO MATRIZ Item x Item """
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




while x < qtd:
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
