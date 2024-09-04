from ListaCircular import ListaCircularEnlazada
class Matriz:

    def __init__(self,nombre,n,m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.filas = ListaCircularEnlazada()

        for i in range(n):
            fila = ListaCircularEnlazada()
            for j in range(m):
                fila.insertar(0)  # Inicializar con ceros o algún valor por defecto
            self.filas.insertar(fila)
    
    def insertar_valor(self, fila_indice, columna_indice, valor):
        fila = self.filas.obtener_info(fila_indice)
        if fila:
            fila.actualizar_info(columna_indice, valor)

    def imprimir_matriz(self):
        for i in range(self.filas.contar()):
            fila = self.filas.obtener_info(i)
            for j in range(fila.contar()):
                print(fila.obtener_info(j), end=" ")
            print()  # Nueva línea al final de cada fila

    def obtener_valor(self, fila_indice, columna_indice):
            fila = self.filas.obtener_info(fila_indice)
            if fila:
                return fila.obtener_info(columna_indice)
            return None

    def obtener_fila(self, indice_fila):
        fila = ListaCircularEnlazada()
        for i in range(self.m):  # Asumiendo que `self.m` es el número de columnas
            fila.insertar(self.obtener_valor(indice_fila, i))  # Asumiendo que tienes un método `obtener_valor`
        return fila

    def insertar_fila(self, fila):
        if self.filas is None:
            self.filas = ListaCircularEnlazada()
        self.filas.insertar(fila)


    def imprimir_matriz_reducida(self):
        # Recorremos cada fila en la matriz
        for i in range(self.filas.longitud):
            fila = self.filas.obtener_info(i)
            # Recorremos cada valor en la fila
            actual = fila.primero  # Nodo inicial en la fila
            for j in range(fila.longitud):
                if actual is not None:
                    # Imprimimos el valor con un espacio al final (sin nueva línea)
                    print(actual.matriz, end=" ")
                    actual = actual.siguiente
            # Imprimimos una nueva línea al final de cada fila
            print()

    

