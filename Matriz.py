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

    

    
