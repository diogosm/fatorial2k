#!/ur/bin/env python
# -*- coding: utf-8 -*-
# @author: Diogo 'dsm' Soares
#

from itertools import combinations

def intToBinary(maxValue,size):
    ans = [int(d) for d in str(bin(maxValue)[2:].zfill(size))]
    return ans

# realiza as combinacoes 
# INPUT array[x1, x2, ..., xk], tal que k = número de fatores
# utiliza a funcao combinations da itertools pra realizar todas
# as combinacoes de tamanho maxSize
def combine(k,maxSize):
    vetor = [i for i in range(k)]
    return combinations(vetor,maxSize)

# realiza todas as combinacoes de 2 a 2 até k a k
def combinacoes(k):
    ans=[]
    for i in range(2,k+1):
        ans.append(combine(k,i))

    return ans

def createStructureFatorial2k(k,y):
    matrix = []

    ## add linhas
    for i in range(2**k):
        linha=[]
        fatores = intToBinary(i,k)        
        fatores = [-1 if fatores[j]==0 else 1 for j in range(len(fatores))]

        for j in range(len(fatores)):
            linha.append(fatores[j])
       
        ## add as combinacoes possiveis
        ## utiliza os indices para multiplicar os valores de cada
        ## fator individualmente
        ## linha[Fator_i] * linha[Fator_j] * linha[Fator_k] * ... * linha[Fator_z]
        ## tal que z é o tamanho máximo de cada tupla da combinacao
        combinado = combinacoes(k)
        for lista in combinado:
            for tupla in list(lista):
                valor = 1
                for elem in tupla:
                    valor *= linha[elem]
                linha.append(valor)
        
        ## add y[i]
        linha.append(y[i])
        matrix.append(linha)

    printMatrix(k,y,matrix)

    return matrix
            
def fatorial2k(k,y):
    matrix = createStructureFatorial2k(k, y)

    q = []
    numColunas = len(matrix[0])

    #for i in range(

def printMatrix(k,y,matrix):
    print "Num. fatores: ", k, "\tVetor Y: ", y
    print "\n",
    print "Fatores: "
    for i in range(k):
        print i, "\t",

    combinado = combinacoes(k)
    for lista in combinado:
        for tupla in list(lista):
            print tupla, "\t", 
    print "Y\n",

    for linha in matrix:
        for elem in linha:
            print elem, "\t",
        print "\n",
    print ""


if __name__ == "__main__":
    linha = input()
    k=int(linha)
    y=[]

    linha = raw_input().split()
    
    for i in xrange(0,len(linha)):
        y.append(int(linha[i]))

    fatorial2k(k, y)
