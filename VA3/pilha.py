class Pilha:
    
    def __init__(self):
        self.lista = []
        self.topo = None
    
    def __pilha_vazia(self):
        if self.topo == None:
            return True
        else:
            return False
    
    def empilhar(self, valor):
        self.lista.append(valor)
        self.topo = self.lista[0]
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha está vazia.")
        else:
            self.lista.pop(0)
            if len(self.lista) > 1:    
                self.topo = self.lista[0]
            else:
                self.topo = None
    
    def ver_pilha(self):
        if len(self.lista) != 0:
            print(self.lista)
        else:
            print("A pilha está vazia.")
    
    def ver_topo(self):
        print(self.topo)

pilha = Pilha()        