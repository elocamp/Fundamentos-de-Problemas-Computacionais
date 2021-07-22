a = map(int, input().split())
entrada = []
for b in a:
    entrada.append(b)

qtde_conteiners = entrada[0]
tam_conteiners = entrada[1]
tam_overflow = entrada[2]
qtde_insercoes = entrada[3]

lista_insercoes = []
cont = 4
while cont < (4 + qtde_insercoes):
    lista_insercoes.append(entrada[cont])
    cont += 1
print (qtde_insercoes) 
print (lista_insercoes)

lista_busca = []
cont2 = (4 + qtde_insercoes)
while cont2 < len(entrada):
    lista_busca.append(entrada[cont2])
    cont2 += 1
print(lista_busca)
    