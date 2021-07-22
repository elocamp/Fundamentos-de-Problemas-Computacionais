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


class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.cont = 0
        
    def mostrar_nodo(self):
        print(self.valor)

class Lista:
    
    def __init__(self):
        self.primeiro = None

    def inserir_lista(self, valor):
        novo = Nodo(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar_lista(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
    
        atual = self.primeiro
        while atual != None:
            atual.mostrar_nodo()
            atual = atual.proximo

    def pesquisa_lista(self, valor):
        if self.primeiro == None:
            print("A lista está vazia.")
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual

    def remover_lista(self, valor):
        if self.primeiro == None:
            print("A lista está vazia.")
            return None
    
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
    
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual
    
    def remover_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
    
        self.primeiro = self.primeiro.proximo

class Dicionário():
    
    def __init__(self):
        self.tabela = []
        while len(self.tabela) < 25:
            self.tabela.append([])
    
    def funcao_hash(self, palavra):
        p1 = ord(palavra[0])
        p2 = ord(palavra[1])
        v = max(p1, p2) - min(p1, p2)
        return v
    
    def Inserir(self, palavra):
        chave = self.funcao_hash(palavra)
        colisao = False
        
        pos = 0
        while pos < len(self.tabela[chave]):
            if self.tabela[chave][pos][1] == palavra:
                temp = ((self.tabela[chave][pos][0] + 1, palavra))
                self.tabela[chave][pos] = temp
                colisao = True
                print("A palavra já está na lista. O contador foi acresentado.")
            pos += 1
            
        if colisao == False:
            self.tabela[chave].append((0, palavra))
            print("Palavra adicionada com sucesso.")
        
    def mostra_tabela(self):
        for linha in self.tabela:
            print(linha)
    
    def ordenaListas(self):
        
        cont = 0
        while cont < len(self.tabela):
            lista_ordenada = merge_sort(self.tabela[cont])
            lista_inversa = merge_sort_inverso(lista_ordenada)
            self.tabela[cont] = lista_inversa
            cont +=1
        self.mostra_tabela()
    
    def consulta(self, palavra):
        chave = self.funcao_hash(palavra)
        
        pos = 0
        cont = 0
        
        while pos < len(self.tabela[chave]):
            if self.tabela[chave][pos][1] == palavra:
                print("Palavra encontrada com sucesso.")
                print('Palavra:', self.tabela[chave][pos][1],'Chave:', chave, 'Contador:', cont)
            else:
                cont += 1
            pos += 1
        if cont == pos:
            print("A palavra não está na lista.")

lista = Lista()
dicionário = Dicionário()

lista_palavras = []
aux = ''
cont = 0
with open('palavras.txt', 'r') as palavras:
    texto = palavras.read()

for l in texto:
    while cont < len(texto):
        if texto[cont] != ",":
            if texto[cont] != " ":
                aux += texto[cont]
        else:
            lista_palavras.append(aux)
            aux = ''
        cont += 1

for palavra in lista_palavras:
    dicionário.Inserir(palavra)

    
while True:
    entrada = int(input(""""Bem-vindo ao menu do Dicionário!
O que você deseja fazer?
1 - Adicionar uma nova palavra
2 - Consultar uma palavra
3 - Ordenar as listas
4 - Mostrar a tabela 
0 - Encerrar o programa
"""))
    
    if entrada == 1:
        while True:
            palavra = input("Insira uma palavra a ser inserida na lista ou pressione 0 para interromper: ").lower()
            if palavra == '0':
                break
            else:
                dicionário.Inserir(palavra)
    
    if entrada == 2:
        while True:
            palavra = input("Insira uma palavra a ser consultada na lista ou pressione 0 para interromper: ").lower()
            if palavra == '0':
                break
            else:
                dicionário.consulta(palavra)
    
    if entrada == 3:
        dicionário.ordenaListas()
    
    if entrada == 4:
        dicionário.mostra_tabela()
    
    if entrada == 0:
        print("\nO programa foi encerrado..")
        break