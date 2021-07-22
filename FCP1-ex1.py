entrada = input().split()

cont = 0
total = 0
lista = []
soma = 0

while cont < len(entrada):
    
    if entrada[cont] == "OP":
        lista.append(entrada[cont])
        lista.append(entrada[cont+1])
        
    if entrada[cont] == "LOOP":
        lista.append(entrada[cont])
        lista.append(entrada[cont+1])
        
    if entrada[cont] == "FIMLOOP":
        lista.append(entrada[cont])
               
    cont += 1

cont2 = len(lista)

while cont2 > 0:
    
    if lista[cont2-1] == "OP":
        soma += int(lista[cont2])
    
    if lista[cont2-1] == "LOOP":
        soma *= int(lista[cont2])
        total += soma
        
        
    cont2 -= 1

print(soma)

