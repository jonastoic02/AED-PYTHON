from random import shuffle
from time import time

class Heap():
    def __init__(self,heap = None):
        if heap is None:
            self.__heap = list()
        else:
            self.__heap = heap

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        retorno = "["
        for i, e in enumerate(self):
            retorno += e.__repr__()
            if i < len(self)-1:
                retorno += ", "

        retorno += "]"
        return retorno

    def __getitem__(self, item):
        return self.__heap[item]

    def __setitem__(self, key, value):
        self.__heap[key] = value

    def __delitem__(self, key):
        del self.__heap[key]

    def __len__(self):
        return len(self.__heap)

    @property
    def heap(self):
        return self.__heap

    @heap.setter
    def heap(self,obj):
        self.__heap = list(obj)

    def pai(self,i):
        _pai = (i - 1) / 2

        return int(_pai) if _pai >= 0 else None

    def esquerda(self,i):
        _esquerda = (2 * i + 1)

        return _esquerda if _esquerda < len(self) else None

    def direita(self,i):
        _direita = (2 * i + 1) + 1

        return _direita if _direita < len(self) else None

    def construir_heap(self):
        i = (len(self) // 2) - 1
        while i >= 0:
            self.heapify(i)
            i -= 1

    def sort(self):
        self.construir_heap()

        ordenado = list()

        i = len(self) - 1

        while i >= 0:
            ordenado.insert(0,self.extrair_maximo())
            i -= 1

        self.__heap = ordenado


    def heapify(self,i):
        e = self.esquerda(i)
        d = self.direita(i)

        if e is not None and self[e] > self[i]:
            maior = e
        else:
            maior = i

        if d is not None and self[d] > self[maior]:
            maior = d

        if maior != i:
            self.__heap[i], self.__heap[maior] = self.__heap[maior], self.__heap[i]

            self.heapify(maior)


    def extrair_maximo(self):
        if len(self) > 0:
            maximo = self[0]

            self.__heap[0] = self.__heap[-1]

            del self.__heap[-1]

            self.heapify(0)

            return maximo

        else:
            return None

    def aumentar_chave(self,i,chave):
        if chave > self[i]:
            self.__heap[i] = chave

            while i > 0 and self[self.pai(i)] < self[i]:
                self.__heap[i], self.__heap[self.pai(i)] = self.__heap[self.pai(i)] , self.__heap[i]

                i = self.pai(i)



    def inserir(self,chave):
        self.__heap.append(chave - 1)
        self.aumentar_chave(len(self) - 1, chave)

n = 11
vetor = list(range(0,n))
print(vetor)
shuffle(vetor)
print(vetor)

lista = Heap(vetor)

antes = time() * 1000
lista.sort()
depois = time() * 1000

lista.inserir(50)
lista.aumentar_chave(10,60)
lista.aumentar_chave(9,40)

tempo = depois - antes

print("Demorou {:.2f}ms para ordenar {} elementos".format(tempo,n))

print(lista)