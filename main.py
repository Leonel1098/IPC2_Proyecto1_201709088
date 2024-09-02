from tkinter import Tk, filedialog
import xml.etree.ElementTree as ET
from graphviz import Digraph
import graphviz
from ListaCircular import ListaCircularEnlazada
from Matriz import Matriz
from ListaEnlazada import Lista_Enlazada

def cargarArchivo():

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    print("Archivo Seleccionado: ", archivo)
   
    with open(archivo, "r", encoding="utf8") as texto_archivo:
        contenido = texto_archivo.read()
        print("\n", contenido)
    
    print("Carga Exitosa")
    return archivo


def lecturaMatrices(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    lista_matrices = Lista_Enlazada()

    for elementos_matriz in root.findall('matriz'):
        nombre = elementos_matriz.get("nombre")
        n = int(elementos_matriz.get('n'))
        m = int(elementos_matriz.get('m'))
        
        lista_matrices.insertar_matriz(nombre, n, m)
        matriz = lista_matrices.obtener_matriz(lista_matrices.contar_matrices() - 1)

        for elementos_dato in elementos_matriz.findall('dato'):
            x = int(elementos_dato.get('x')) - 1
            y = int(elementos_dato.get('y')) - 1

            valor = int(elementos_dato.text)
            print(f"Inserting value {valor} at position ({x}, {y})")
            matriz.insertar_valor(x, y, valor)

    return lista_matrices

def imprimir_matrices(lista_matrices):
    lista_matrices.imprimir_todas()

    # Función para graficar una matriz con Graphviz
def graficar_matriz(matriz, nombre_archivo):
    dot = Digraph(comment='Matriz')
    filas = matriz.contar_filas()

    for i in range(filas):
        columnas = matriz.contar_columnas(i)
        for j in range(columnas):
            valor = matriz.obtener_valor(i, j)
            print(f"Value at ({i}, {j}) is {valor}")
            dot.node(f'{i}_{j}', label=str(valor))

        for j in range(columnas):
            if j < columnas - 1:
                dot.edge(f'{i}_{j}', f'{i}_{j+1}')
            if i < filas - 1 and matriz.contar_columnas(i+1) > j:
                dot.edge(f'{i}_{j}', f'{i+1}_{j}')

    dot.render(nombre_archivo, format='png', cleanup=True)

# Función para graficar todas las matrices en la lista circular
def graficar_listas_circulares(lista_circular):
    for i, matriz in enumerate(lista_circular.recorrer()):
        graficar_matriz(matriz, f'matriz_{i}')

def Menu():
    while  True:
        print("")
        print("----------Menú----------")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Salida")
        # Definimos la variable opcion que es la que recibe la selección del usuario y la válida en los if 
        opcion = input("\n Por favor seleccione una opción:... ")

        if opcion == "1":
            print("")
            archivo = cargarArchivo()
        
        elif opcion == "2":
            print("")
            #menu2()
            print("Procesar Archivo")
            lista_matrices = lecturaMatrices(archivo)
            imprimir_matrices(lista_matrices)

        elif opcion == "3":
            print("")
           # pisos.mostrarPisos_Orden()
            print("Escribir Archivo de Salida ")

        elif opcion == "4":
            print(f"\n --Leonel Antonio Gonzalez Garcia \n --201709088 \n --Introduccion a la Programacion y Computacion 2 seccion N \n --Ingenieria en Ciencias y Sistemas \n --4to Semestre")
        
        elif opcion == "5":
            print("\nGenerar Grafica\n")
            lista_circular = lecturaMatrices(archivo)
            graficar_listas_circulares(lista_circular)

        elif opcion == "6":
            print("")
            print("Regresa Pronto :)")
            break

        else:
            print("\n Seleccione una opción válida...")
            input("Presione una tecla para continuar...")
            


Menu()