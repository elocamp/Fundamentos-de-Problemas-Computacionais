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

    def pesquisar(self, valor):
      atual = self.raiz
    
      while atual.valor != valor:
        if valor < atual.valor:
          atual = atual.esquerda
        
        else:
          atual = atual.direita
        
        if atual == None:
          return None
      return atual
  
    def pre_ordem(self, no):
        if no != None:
          print(no.valor)
          self.pre_ordem(no.esquerda)
          self.pre_ordem(no.direita)
    
          
        
arvore = ArvoreBinariaBusca()
arvore.inserir(5)
arvore.inserir(2)
arvore.inserir(3)
arvore.inserir(1)
arvore.inserir(7)
arvore.inserir(10)
arvore.inserir(6)

