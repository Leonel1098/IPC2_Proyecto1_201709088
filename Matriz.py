from ListaCircular import ListaCircularEnlazada
#En esta clase se trabaja con la matriz de la lista circular 
class Matriz:

    def __init__(self,nombre,n,m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.filas = ListaCircularEnlazada()

        for i in range(n):
            fila = ListaCircularEnlazada()
            for j in range(m):
                fila.insertar(0) 
            self.filas.insertar(fila)
    
    #Va agregando los valores a las matices 
    def insertar_valor(self, fila_indice, columna_indice, valor):
        fila = self.filas.obtener_info(fila_indice)
        if fila:
            fila.actualizar_info(columna_indice, valor)

    #Sirve para imprimir la matriz que se crea 
    def imprimir_matriz(self):
        for i in range(self.filas.contar()):
            fila = self.filas.obtener_info(i)
            for j in range(fila.contar()):
                print(fila.obtener_info(j), end=" ")
            print() 

    #Obtiene el valor de una posicion especifica de la matriz
    def obtener_valor(self, fila_indice, columna_indice):
            fila = self.filas.obtener_info(fila_indice)
            if fila:
                return fila.obtener_info(columna_indice)
            return None

    #Obtiene la fila completa de la matriz 
    def obtener_fila(self, indice_fila):
        fila = ListaCircularEnlazada()
        for i in range(self.m):  
            valor = self.obtener_valor(indice_fila, i)
            #print(f"Valor en fila {indice_fila}, columna {i}: {valor}") 
            fila.insertar(valor)
        return fila

    #Inserta una fila completa en la matriz
    def insertar_fila(self, fila):
        if self.filas is None:
            self.filas = ListaCircularEnlazada()
        self.filas.insertar(fila)


    def imprimir_matriz_reducida(self):
        # Recorremos cada fila en la matriz
        for i in range(self.filas.longitud):
            fila = self.filas.obtener_info(i)
            # Recorremos cada valor en la fila
            actual = fila.primero  
            for j in range(fila.longitud):
                if actual is not None:
                    print(actual.matriz, end=" ")
                    actual = actual.siguiente
            print()

    

