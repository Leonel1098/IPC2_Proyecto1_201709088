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
            #print(f"Inserting value {valor} at position ({x}, {y})")
            matriz.insertar_valor(x, y, valor)

    return lista_matrices

def imprimir_matrices(lista_matrices):
    lista_matrices.imprimir_todass()


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
            lista_matrices = lecturaMatrices(archivo)
            lista_matrices.imprimir_todas()

            # Luego, selecciona una matriz
            indice_seleccionado = int(input("Ingresa el índice de la matriz que deseas seleccionar: "))
            lista_matrices.elegir_matriz(indice_seleccionado)
            # ...
            matriz_reducida = lista_matrices.matriz_reducida(indice_seleccionado)
            
            # Imprimir la matriz reducida
            print("Matriz reducida:")
            matriz_reducida.imprimir_matriz()


        elif opcion == "3":
            print("")
           # pisos.mostrarPisos_Orden()
            
            #imprimir_con_indices()
            print("Escribir Archivo de Salida ")

        elif opcion == "4":
            print(f"\n --Leonel Antonio Gonzalez Garcia \n --201709088 \n --Introduccion a la Programacion y Computacion 2 seccion N \n --Ingenieria en Ciencias y Sistemas \n --4to Semestre")
        
        elif opcion == "5":
            print("\nGenerar Grafica\n")
            lista_circular = lecturaMatrices(archivo)
            #graficar_listas_circulares(lista_circular)

        elif opcion == "6":
            print("")
            print("Regresa Pronto :)")
            break

        else:
            print("\n Seleccione una opción válida...")
            input("Presione una tecla para continuar...")
            


Menu()