from ListaCircular import ListaCircularEnlazada
from Matriz import Matriz

class Lista_Enlazada:
    def __init__(self):
        self.matrices = ListaCircularEnlazada()
    
    def insertar_matriz(self,nombre, n ,m ):
        matriz = Matriz(nombre,n,m)
        self.matrices.insertar(matriz)
    
    def obtener_matriz(self, indice):
        return self.matrices.obtener_info(indice)

    def contar_matrices(self):
        return self.matrices.contar()

    def imprimir_todas(self):
        for i in range(self.contar_matrices()):
            matriz = self.obtener_matriz(i)
            print(f"Matriz: {matriz.nombre}")
            matriz.imprimir_matriz()
            print()  # Espacio entre matrices
  


