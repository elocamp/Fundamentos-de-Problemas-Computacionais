entrada = input().split()

lista = []
for i in entrada:
    
    if i == "[" or i == "]" or i == "{" or i == "}" or i == "(" or i == ")":
        lista.append(i)

casamento = True
cont = 0
while cont < len(lista):
    
    if lista[cont] == "[":
        if lista[cont+1] != "[" or lista[cont+1] != "{" or lista[cont+1] != "(" or lista[cont+1] != "]":
            casamento == False
    
    elif lista[cont] == "{":
        if lista[cont+1] != "[" or lista[cont+1] != "{" or lista[cont+1] != "(" or lista[cont+1] != "}":
            casamento == False
    
    elif lista[cont] == "(":
        if lista[cont+1] != "[" or lista[cont+1] != "{" or lista[cont+1] != "(" or lista[cont+1] != ")":
            casamento == False
    
    cont += 1
    
if casamento == True:
    print("casamento perfeito")
else:
    print("casamento imperfeito")
    
