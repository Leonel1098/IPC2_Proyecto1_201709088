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
            print(f"Índice: {i}, Matriz: {matriz.nombre}, Filas: {matriz.n}, Columnas: {matriz.m}")
            matriz.imprimir_matriz()
            print()  # Espacio entre matrices
  

    def matriz_patrones(self, indice):
        matriz_original = self.obtener_matriz(indice)
        matriz_patrones = Matriz(matriz_original.nombre + "_patrones", matriz_original.n, matriz_original.m)
        
        for i in range(matriz_original.n):
            fila = matriz_original.filas.obtener_info(i)
            for j in range(matriz_original.m):
                valor = fila.obtener_info(j)
                matriz_patrones.insertar_valor(i, j, 1 if valor != 0 else 0)
        
        return matriz_patrones
    

    def elegir_matriz(self, indice):
            if indice < 0 or indice >= self.contar_matrices():
                print("Índice fuera de rango")
                return
            
            matriz = self.obtener_matriz(indice)
            print(f"Seleccionaste la matriz: {matriz.nombre} ({matriz.n}x{matriz.m})")
            matriz.imprimir_matriz()
            
            print("\nMatriz de patrones de acceso:")
            matriz_patron = self.matriz_patrones(indice)
            matriz_patron.imprimir_matriz()



    """def imprimir_con_indices(self):
        for i in range(self.contar_matrices()):
            matriz = self.obtener_matriz(i)
            print(f"Índice: {i}, Matriz: {matriz.nombre}, Filas: {matriz.n}, Columnas: {matriz.m}")"""

    