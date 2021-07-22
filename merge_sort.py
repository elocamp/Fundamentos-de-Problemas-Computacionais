def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita =vetor[divisao:].copy()
        
        merge_sort(esquerda)
        merge_sort(direita)
        
        i = j = k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
        
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    
    return vetor

def merge_sort_inverso(vetor):
    
    lista_inversa = []
    cont = len(vetor)-1
    while cont > 0:
        lista_inversa.append(vetor[cont])
        cont -= 1
    return lista_inversa

lista = [(5, 'girafa'), (0, 'lavanderia'), (3, 'pena'), (1, 'alho')]
lista_ordenada = merge_sort(lista)
a = merge_sort_inverso(lista_ordenada)
print(a)
