#!/ur/bin/env python
# -*- coding: utf-8 -*-

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

def fatorial2k(k,y):
    matrix = []
    #combinacoes = [1,4,11]

    print "k: ", k, "\ty: ", y
    print "\n"
    print "fatores: "
    for i in range(k):
        print i, "\t",

    combinado = combinacoes(k)
    for lista in combinado:
        for tupla in list(lista):
            print tupla, "\t", 
    print "\n",

    ## add linhas
    for i in range(2**k):
        linha=[]
        fatores = intToBinary(i,k)        
        fatores = [-1 if fatores[j]==0 else 1 for j in range(len(fatores))]

        for j in range(len(fatores)):
            linha.append(fatores[j])
       
        combinado = combinacoes(k)
        for lista in combinado:
            for tupla in list(lista):
                valor = 1
                for elem in tupla:
                    valor *= linha[elem]
                linha.append(valor)

        ## add y[i]
        linha.append(y[i])
        for elem in linha:
            print elem, "\t",
        print "\n",

    matrix.append(linha)
            
    
if __name__ == "__main__":
    linha = input()
    k=int(linha)
    y=[]

    linha = raw_input().split()
    
    for i in xrange(0,len(linha)):
        y.append(int(linha[i]))

    fatorial2k(k,y)
