class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
  
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


lista = Lista()
lista.inserir_lista('teste')
lista.inserir_lista('cachorro')
lista.inserir_lista('cachorro')
lista.mostrar_lista()

pesquisa = lista.pesquisa_lista('cachorro')
if pesquisa != None:
  print('Encontrado:', pesquisa.valor)
else:
  print('Não encontrado')