#!/usr/bin/env python

def intToBinary(maxValue,size):
    ans = [int(d) for d in str(bin(maxValue)[2:].zfill(size))]
    return ans

def fatorial2k(k,y):
    matrix = []
    #combinacoes = [1,4,11]

    print "k: ", k, "\ty: ", y

    ## add linhas
    for i in range(2**k):
        linha=[]
        fatores = intToBinary(i,k)        
        fatores = [-1 if fatores[j]==0 else 1 for j in range(len(fatores))]

        for j in range(len(fatores)):
            linha.append(fatores[j])
       
        valor = 1
        ## 2 a 2
        for comb_i in range(k):
            for comb_j in range(comb_i+1,k):
                valor *= fatores[comb_i] * fatores[comb_j]
                linha.append(valor)
            valor = 1

        ## 3 a 3
        for comb_i in range(k):
            for comb_j in range(comb_i+1,k):
                for comb_k in range(comb_j+1,k):
                    valor *= fatores[comb_i] * fatores[comb_j] * fatores[comb_k]
                    linha.append(valor)
                valor = 1
            valor = 1

        ## 4 a 4
        for comb_i in range(k):
            for comb_j in range(comb_i+1,k):
                for comb_k in range(comb_j+1,k):
                    for comb_z in range(comb_k+1,k):
                        valor *= fatores[comb_i] * fatores[comb_j] * fatores[comb_k] * fatores[comb_z]
                        linha.append(valor)
                    valor = 1
                valor = 1
            valor = 1

        ## add y[i]
        linha.append(y[i])
        print linha
    
    matrix.append(linha)
            
    
if __name__ == "__main__":
    linha = input()
    k=int(linha)
    y=[]

    linha = raw_input().split()
    
    for i in xrange(0,len(linha)):
        y.append(int(linha[i]))

    fatorial2k(k,y)
