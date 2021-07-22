import pilha

def quicksort(vetor):
    pivo = int(len(vetor)/2)
    esquerda = []
    direita = []
    print("\nExibição da lista não ordenada:")
    print("\n", vetor)
    print("\n===========================================================================\n")
    
    for i in range(len(vetor)):
        pilha.pilha.empilhar(i)
        
    cont = 0
    while cont < len(vetor):
        if pilha.pilha.topo <= vetor[pivo]:
            esquerda.append(vetor[cont])
            
        else:
            direita.append(vetor[cont])
            
        cont += 1
        
    for l in range(len(vetor)):
        pilha.pilha.desempilhar()
#==================================================================# 
    
    cont3 = 0
    cont4 = 0
    while cont3 < len(esquerda):
        while cont4 < len(esquerda)-1:
            if esquerda[cont4] > esquerda[cont4+1]:
                esquerda[cont4], esquerda[cont4+1] = esquerda[cont4+1], esquerda[cont4]
            cont4 += 1
        cont3 += 1
        cont4 = 0
    
    for e in esquerda:
        pilha.pilha.empilhar(e)

#==================================================================#
    
    cont1 = 0
    cont2 = 0
    while cont1 < len(direita):
        while cont2 < len(direita)-1:
            if direita[cont2] > direita[cont2+1]:
                direita[cont2], direita[cont2+1] = direita[cont2+1], direita[cont2]
            cont2 += 1
        cont1 += 1
        cont2 = 0
    
    for d in direita:
        pilha.pilha.empilhar(d)
    
    print("Exibição da lista ordenada: \n")
    pilha.pilha.ver_pilha()
    
            
