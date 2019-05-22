#!/ur/bin/env python
# -*- coding: utf-8 -*-
# @author: Diogo 'dsm' Soares
#

from itertools import combinations
from string import ascii_uppercase
from sys import stdout

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

# ordena confome a ordem do anova
# que eh pelo ultimo fator de tras pra frente
# a partir do ultimo fator
def anovaOrder(a,b):
    aux_k = k-1 ## num de fatores
    while(aux_k>0):
        if(a[aux_k] != b[aux_k]):
            return a[aux_k]-b[aux_k]
            break
        aux_k = aux_k-1
    return a[0]-b[0]

def criaCabecalho():
    cabecalho = []
    
    for i in range(k):
        lista = []
        lista.append(i)
        cabecalho.append(lista)
    for lista in combinacoes(k):
        for tupla in list(lista):
            cabecalho.append(list(tupla))
            
    return cabecalho

def SST(q):
    yTraco = 0
    sstTotal = 0

    for i in range(2**k):
        yTraco += y[i]
    yTraco /= 2**k

    for i in range(2**k):    
        sstTotal += (y[i]-yTraco)**2
    
    return sstTotal    

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

    ## orderna no estilo da ANOVA
    matrix.sort(anovaOrder)
    ## gambi pra pegar o y na ordem original da entrada
    for i in range(2**k):
        matrix[i][len(matrix[0])-1] = y[i]

    printMatrix(k,y,matrix)

    return matrix
            
def fatorial2k(k,y):
    matrix = createStructureFatorial2k(k, y)
    cabecalho = criaCabecalho()
    q = []
    porcaoVariacao = []
    valor = 0
    
    ## calc q[0]
    for i in range(2**k):
        valor += matrix[i][len(matrix[0])-1]
    q.append(valor)
    
    for j in range(len(matrix[0])-1):
        valor = 0
        for i in range(2**k):
            valor += matrix[i][len(matrix[0])-1] * matrix[i][j]
        q.append(valor)

    for i in range(len(q)):
        q[i] = q[i]/2**k

    ## calc SST
    sst = SST(q)
    
    ## calc porcaoVariacao
    for i in range(1,len(q)):
        porcaoVariacao.append(q[i]**2 * 2**k)

    return sst, porcaoVariacao, cabecalho    

def printMatrix(k,y,matrix):
    print "Num. fatores: ", k, "\tVetor Y: ", y
    print "\n",
    print "Fatores: "
    fatores = list(ascii_uppercase)
    for i in range(k):
        print fatores[i], "\t",

    combinado = combinacoes(k)
    for lista in combinado:
        for tupla in list(lista):
            for elem in tupla:
                stdout.write(fatores[elem])
            print "\t", 
    print "Y\n",

    for linha in matrix:
        for elem in linha:
            print elem, "\t",
        print "\n",
    print ""

def printVariacao(sst, porcaoVariacao, cabecalho):
    fatores = list(ascii_uppercase)
    iterador = 0
    
    print "Porcao de variacao (%):\n"
    for fator in cabecalho:
        for pos in fator:
            stdout.write(fatores[pos])
        print " = ", "%.2f" % (100.0*(1.0*porcaoVariacao[iterador]/sst))
        iterador += 1

if __name__ == "__main__":
    linha = input()
    k=int(linha)
    y=[]

    linha = raw_input().split()
    
    for i in xrange(0,len(linha)):
        y.append(float(linha[i]))

    sst, porcaoVariacao, cabecalho = fatorial2k(k, y)
    
    printVariacao(sst, porcaoVariacao, cabecalho)

