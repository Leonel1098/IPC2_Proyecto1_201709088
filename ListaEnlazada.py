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


    def matriz_reducida(self, indice):
        matriz_original = self.obtener_matriz(indice)
        
        if matriz_original is None:
            print("Matriz no encontrada.")
            return None
        
        matriz_reducida = Matriz(matriz_original.nombre + "_reducida", 0, matriz_original.m)
        filas_procesadas = ListaCircularEnlazada()

        for i in range(matriz_original.n):
            fila_actual = matriz_original.obtener_fila(i)

            print(f"Procesando fila {i}:")
            fila_actual.imprimir_fila()  # Imprime la fila actual para depurar

            # Verificar si ya existe una fila similar procesada
            fila_similar = self.obtener_fila_similar(filas_procesadas, fila_actual)

            if fila_similar is not None:
                print(f"Fila similar encontrada, sumando:")
                fila_similar.imprimir_fila()  # Imprime la fila similar para depurar
                self.sumar_fila(fila_similar, fila_actual)
                print("Resultado de la suma:")
                fila_similar.imprimir_fila()  # Verifica el resultado de la suma
            else:
                print("No se encontró fila similar, agregando la fila actual.")
                filas_procesadas.insertar(fila_actual)
        
        # Crear la matriz reducida basada en las filas procesadas
        actual = filas_procesadas.primero
        while actual is not None:
            matriz_reducida.insertar_fila(actual.valor)
            actual = actual.siguiente
            if actual == filas_procesadas.primero:
                break
        
        matriz_reducida.n = filas_procesadas.contar()  # Actualizar el número de filas
        print("Matriz reducida creada correctamente.")
        return matriz_reducida

    def obtener_fila_similar(self, filas_procesadas, fila_actual):
        actual = filas_procesadas.primero
        while actual is not None:
            if self.son_filas_iguales(actual.valor, fila_actual):
                return actual.valor
            actual = actual.siguiente
            if actual == filas_procesadas.primero:
                break
        return None

    def sumar_fila(self, fila_destino, fila_origen):
        nodo_destino = fila_destino.primero
        nodo_origen = fila_origen.primero
        
        while nodo_destino is not None and nodo_origen is not None:
            print(f"Sumando {nodo_destino.valor} + {nodo_origen.valor}")
            nodo_destino.valor += nodo_origen.valor
            
            nodo_destino = nodo_destino.siguiente
            nodo_origen = nodo_origen.siguiente
            
            if nodo_destino == fila_destino.primero or nodo_origen == fila_origen.primero:
                break







    def fila_ya_procesada(self, filas_procesadas, fila):
        for fila_procesada in filas_procesadas.recorrer():
            if self.son_filas_iguales(fila, fila_procesada):
                return True
        return False

    def son_filas_iguales(self, fila1, fila2):
        nodo1 = fila1.primero
        nodo2 = fila2.primero

        while True:
            if nodo1.valor != nodo2.valor:
                return False
            nodo1 = nodo1.siguiente
            nodo2 = nodo2.siguiente
            if nodo1 == fila1.primero and nodo2 == fila2.primero:
                break

        return True


    def obtener_indice_fila(self, lista_filas, fila):
        actual = lista_filas.primero
        indice = 0
        while True:
            if self.son_filas_iguales(actual.valor, fila):
                return indice
            actual = actual.siguiente
            indice += 1
            if actual == lista_filas.primero:
                break
        return None
