from Nodo import Nodo
class ListaCircularEnlazada:
        def __init__(self):
            self.primero = None
            self.longitud = 0

        def insertar(self, matriz):
            nuevo_nodo = Nodo(matriz)

            if not self.primero:
                self.primero = nuevo_nodo
                nuevo_nodo.siguiente = self.primero
            else:
                actual = self.primero
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = self.primero
            self.longitud += 1

        def obtener_info(self, indice):
            if self.longitud == 0 or indice >= self.longitud:
                return None
            actual = self.primero
            for i in range(indice):
                actual = actual.siguiente
            return actual.matriz

        def actualizar_info(self, indice, matriz):
            if self.longitud == 0 or indice >= self.longitud:
                return False
            actual = self.primero
            for i in range(indice):
                actual = actual.siguiente
            actual.matriz = matriz
            return True

        def contar(self):
            return self.longitud
        
        def recorrer(self):
            if not self.primero:
                return
            actual = self.primero
            while True:
                yield actual.matriz
                actual = actual.siguiente
                if actual == self.primero:
                    break
