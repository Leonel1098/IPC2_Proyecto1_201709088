from NodoCircular import NodoCircular
class ListaCircularEnlazada:
        def __init__(self):
            self.primero = None
            self.ultimo = None

        def insertar(self, matriz):
            nuevo_nodo = NodoCircular(matriz)
            if not self.primero:
                self.primero = nuevo_nodo
                self.ultimo = nuevo_nodo
                nuevo_nodo.siguiente = self.primero
            else:
                self.ultimo.siguiente = nuevo_nodo
                self.ultimo = nuevo_nodo
                self.ultimo.siguiente = self.primero

        def recorrer(self):
            if not self.primero:
                return
            actual = self.primero
            while True:
                yield actual.matriz
                actual = actual.siguiente
                if actual == self.primero:
                    break
