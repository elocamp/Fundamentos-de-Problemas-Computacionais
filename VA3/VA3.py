import quicksort, pilha, random

class Algoritmo:
    
    def __init__(self):
        self.lista_random = []
        
    def gerar_lista(self):
        for x in range(1000):
            x = random.randint(1, 5000)
            self.lista_random.append(x)
    
    def quicksortPilha(self):
        if len(self.lista_random) == 0:
            print("A lista está vazia. É necessário gerar a lista antes de ordená-la.")
        else:
            quicksort.quicksort(algoritmo.lista_random)
            self.lista_random = pilha.pilha.lista
            algoritmo.ordemCrescente()
    
    def ordemCrescente(self):
        if len(self.lista_random) == 0:
            print("A lista está vazia. É necessário gerar a lista antes de ordená-la.")
        else:
            ordenada = True
            cont = 0
            while cont < len(self.lista_random)-1:
                if self.lista_random[cont] > self.lista_random[cont+1]:
                    ordenada = False
                cont += 1
            
            if ordenada == True:
                print("\n A lista está ordenada")
            else:
                print("\n A lista está desordenada.")
                
            
    

algoritmo = Algoritmo()