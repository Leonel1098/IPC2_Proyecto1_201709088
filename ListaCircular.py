from Nodo import Nodo

#Con esta lista circular gestionamos las matrices del archivo xml
class ListaCircularEnlazada:
    
    def __init__(self):
        self.primero = None
        self.longitud = 0

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)

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
        return actual.valor

    def actualizar_info(self, indice, valor):
        if self.longitud == 0 or indice >= self.longitud:
            return False
        actual = self.primero
        for i in range(indice):
            actual = actual.siguiente
        actual.valor = valor
        return True

    def contar(self):
        return self.longitud
    
    def recorrer(self):
        if not self.primero:
            return
        actual = self.primero
        while True:
            yield actual.valor
            actual = actual.siguiente
            if actual == self.primero:
                break
    
    def contar_matrices(self):
        if not self.primero:
            return 0
        contador = 1
        actual = self.primero
        while actual.siguiente != self.primero:
            contador += 1
            actual = actual.siguiente
        return contador            


    def imprimir_matrices_con_indices(self):
        if not self.primero:
            print("La lista está vacía.")
            return
        
        actual = self.primero
        indice = 0
        
        while True:
            print(f"Índice {indice}: Matriz {actual.valor.nombre} ({actual.valor.n}x{actual.valor.m})")
            indice += 1
            actual = actual.siguiente
            if actual == self.primero:
                break

    def obtener_indice(self, fila):
        actual = self.primero
        indice = 0
        while True:
            if self.son_filas_iguales(actual.matriz, fila):
                return indice
            actual = actual.siguiente
            indice += 1
            if actual == self.primero:
                break
        return -1

    def imprimir_fila(self):
        actual = self.primero
        if actual is None:
            print("Fila vacía")
            return
        
        while True:
            print(actual.valor, end=" ")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()