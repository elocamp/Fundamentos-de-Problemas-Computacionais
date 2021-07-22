entrada = map(int, input().split())

lista_final = []

lista_ent = []
for a in entrada:
    if a != " ":
        lista_ent.append(a)

cont = 0
lista_nos = []
lista_elementos = []
while cont < (len(lista_ent)):
    altura = lista_ent[0]
    cont += 1
    if cont <= ((2**altura)-1):
        lista_nos.append(lista_ent[cont])

class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def mostra_no(self):
        print(self.valor)
    
class ArvoreBinariaBusca:
    
    def __init__(self):
      self.raiz = None
      self.ligacoes = []

    def inserir(self, valor):
      novo = No(valor)

      if self.raiz == None:
        self.raiz = novo
      
      else:
        atual = self.raiz
      
        while True:
          pai = atual
        
          if valor < atual.valor:
            atual = atual.esquerda
          
            if atual == None:
              pai.esquerda = novo
              self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
              return
        
          else:
            atual = atual.direita
            if atual == None:
              pai.direita = novo
              self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
              return 
  
    def pre_ordem(self, no):
        if no != None:
          lista_final.append(no.valor)
          self.pre_ordem(no.esquerda)
          self.pre_ordem(no.direita)
    
                   
arvore = ArvoreBinariaBusca()
for elemento in lista_nos:
    arvore.inserir(elemento)

arvore.pre_ordem(arvore.raiz)

cont2 = 0
while cont2 < len(lista_final):
    
    if altura == 3:
        
        if cont2 == 0 or cont2 == 1 or cont2 == 4:
            
            if cont2 == 0:
                lista_final[cont2] = (1, lista_final[cont2])
                
            elif cont2 == 1 or cont2 == 4:
                lista_final[cont2] = (2, lista_final[cont2])
                
        else:
            lista_final[cont2] = (3, lista_final[cont2]) 
        
        cont2 += 1
        
    if altura == 4:
        
        if cont2 == 0 or cont2 == 1 or cont2 == 2 or cont2 == 5 or cont2 == 8 or cont2 == 9 or cont2 == 12:
            
            if cont2 == 0:
                lista_final[cont2] = (1, lista_final[cont2])
                
            elif cont2 == 1 or cont2 == 8:
                lista_final[cont2] = (2, lista_final[cont2])
            
            elif cont2 == 2 or cont2 == 5 or cont2 == 9 or cont2 == 12:
                lista_final[cont2] = (3, lista_final[cont2])
                
        else:
            lista_final[cont2] = (4, lista_final[cont2]) 
        
        cont2 += 1

lista_final.sort()
lista_nos.clear()

cont3 = (altura**2)-1
while cont3 < len(lista_ent):
    lista_elementos.append(lista_ent[cont3])
    cont3 += 1

cont4 = 0
while cont4 < len(lista_final):
    lista_nos.append(lista_final[cont4][1])
    lista_final[cont4] = lista_final[cont4][0]
    cont4 +=1

lista_ent.clear()

for m in lista_elementos:
    if m in lista_nos:
        var = lista_final[lista_nos.index(m)]
        lista_ent.append(var)
        var = " "
        lista_ent.append(var)
        var = lista_nos.index(m)
        lista_ent.append(var)
        var = "!!!"
        lista_ent.append(var)
    else:
        var = (0)
        lista_ent.append(var)
        var = '!!!'
        lista_ent.append(var)

lista_print = []
if altura == 3:
    cont5 = 0
    while cont5 < len(lista_ent)-1:
        lista_print.append(lista_ent[cont5])
        cont5 += 1
    for n in lista_print:
            print(n, end='')

elif altura == 4:
    cont5 = 4
    while cont5 < len(lista_ent)-1:
        lista_print.append(lista_ent[cont5])
        cont5 += 1
    for n in lista_print:
            print(n, end='')

