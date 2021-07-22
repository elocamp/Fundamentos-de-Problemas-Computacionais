def busca_linear(lista, n, comeco, end, cont = 0):
    
    if comeco <= end:
        cont += 1
        ponteiro = (comeco + end) // 2
        
        print(lista[ponteiro])
        
        if n == lista[ponteiro]:
            return cont
        
        elif n < lista[ponteiro]:
            return busca_linear(lista, n, comeco, ponteiro-1, cont)
        
        elif n > lista[ponteiro]:
            return busca_linear(lista, n, ponteiro+1, end, cont)
        
    else:
        return cont

entrada = input().split()

tamanho = int(entrada[0])
lista = entrada[1 : tamanho+1]
elementos = entrada[tamanho+1 :]

for n in elementos:
    print(busca_linear(lista, n, 0, len(lista)-1), end = ' ')

    
