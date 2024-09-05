from tkinter import Tk, filedialog
import os
import webbrowser
from xml.dom import minidom
import xml.etree.ElementTree as ET
from graphviz import Digraph
from ListaEnlazada import Lista_Enlazada

#Muestra el explorador de archivos para cargar el archivo xml y leer la informacion
def cargarArchivo():

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    print("Archivo Seleccionado: ", archivo)
   
    with open(archivo, "r", encoding="utf8") as texto_archivo:
        contenido = texto_archivo.read()
        #print("\n", contenido)
    
    print("Carga Exitosa")
    return archivo


# Lee el archivo XML y carga las matrices en la lista enlazada.
def lecturaMatrices(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    lista_matrices = Lista_Enlazada()

    # Recorre el archivo para iterar las matrices
    for elementos_matriz in root.findall('matriz'):
        nombre = elementos_matriz.get("nombre")
        n = int(elementos_matriz.get('n'))
        m = int(elementos_matriz.get('m'))
        
        #Se crea y agrega la matriz a la lista de matrices
        lista_matrices.insertar_matriz(nombre, n, m)
        matriz = lista_matrices.obtener_matriz(lista_matrices.contar_matrices() - 1)
        #Se agregarn los elementos de laas matrices
        for elementos_dato in elementos_matriz.findall('dato'):
            x = int(elementos_dato.get('x')) - 1
            y = int(elementos_dato.get('y')) - 1

            valor = int(elementos_dato.text)
            #print(f"Inserting value {valor} at position ({x}, {y})")
            matriz.insertar_valor(x, y, valor)

    return lista_matrices


#Improme las matrices de la lista
def imprimir_matrices(lista_matrices):
    lista_matrices.imprimir_todass()

#Realiza la Grafica de la matriz
def graficar_matriz(matriz):
    # Crear un nuevo objeto Digraph
    dot = Digraph()

    # Contar el número de filas y columnas
    num_filas = 0
    fila_actual = matriz.filas.primero
    while fila_actual:
        num_filas += 1
        fila_actual = fila_actual.siguiente

    num_columnas = 0
    if matriz.filas.primero:
        fila = matriz.filas.primero
        num_columnas = fila.longitud

    if num_filas == 0 or num_columnas == 0:
        print("La matriz está vacía.")
        return None

    # Crear nodos para cada valor en la matriz
    for i in range(num_filas):
        fila = matriz.filas.obtener_info(i)
        for j in range(num_columnas):
            valor = fila.obtener_info(j)
            dot.node(f'{i}_{j}', label=str(valor), shape='ellipse')

            if j < num_columnas - 1:
                dot.edge(f'{i}_{j}', f'{i}_{j+1}', dir='none')

            if i < num_filas - 1:
                dot.edge(f'{i}_{j}', f'{i+1}_{j}', dir='none')

    # Guardar el archivo DOT
    dot_file = 'matriz.dot'
    dot.save(dot_file)
    print(f"Archivo DOT guardado como '{dot_file}'")

    # Renderizar la gráfica
    dot.render('matriz', format='png', view=True)
    print("Gráfica generada y guardada como 'matriz.png'.")
    return dot

#Crea el archivo XML de la matriz reducida
def escribir_matriz_reducida_xml(matriz_reducida, nombre_archivo):
    # Crear el elemento raíz
    root = ET.Element("matriz", nombre="Matriz Reducida", n=str(matriz_reducida.filas.longitud),
                      m=str(matriz_reducida.obtener_fila(0).longitud))

    # Cuenta el número de filas y columnas
    num_filas = matriz_reducida.filas.longitud
    num_columnas = matriz_reducida.obtener_fila(0).longitud if num_filas > 0 else 0

    # Agregar los datos de la matriz
    for i in range(num_filas):
        fila = matriz_reducida.obtener_fila(i)
        for j in range(num_columnas):
            valor = fila.obtener_info(j)
            dato_element = ET.SubElement(root, "dato", x=str(i + 1), y=str(j + 1))
            dato_element.text = str(valor)

    # Crear el XML
    tree = ET.ElementTree(root)

    # Convertir a cadena XML
    xml_str = ET.tostring(root, encoding='utf-8', method='xml')

    #Con el minidom se le da formato al xml para que se cree organizado
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml_str = parsed_xml.toprettyxml(indent="  ")

    # Escribir en archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(pretty_xml_str)

def abrir_pdf():
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'Ensayo_Proyecto1_201709088.pdf')
    #print(f"Puedes abrir el archivo PDF haciendo clic en el siguiente enlace:")
    #print(f"file:///{ruta_archivo}")
    
    # Pedir al usuario que presione Enter para abrir el archivo
    input("\nPresiona Enter para abrir la Documentacion...")
    webbrowser.open(f'file:///{ruta_archivo}')

#Este es el menu con el que se maneja la aplicacion

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
            print("Escribiendo Archivo de Salida ")
            escribir_matriz_reducida_xml(matriz_reducida, 'matriz_reducida.xml')

        elif opcion == "4":
            print("---------------DATOS DEL ESTUDIANTE-------------------------------")
            print(f"\n --Leonel Antonio Gonzalez Garcia \n --201709088 \n --Introduccion a la Programacion y Computacion 2 seccion N \n --Ingenieria en Ciencias y Sistemas \n --4to Semestre")
            abrir_pdf()
        
        elif opcion == "5":
            print("\nGenerar Gráfica\n")
            if lista_matrices is None:
                print("Primero, debes procesar un archivo.")
                continue

            indice_seleccionado = int(input("Ingresa el índice de la matriz que deseas graficar: "))
            matriz = lista_matrices.obtener_matriz(indice_seleccionado)
            if matriz is None:
                print("Índice de matriz inválido.")
                continue

            print(f"Matriz seleccionada: {matriz.nombre} ({matriz.n}x{matriz.m})")
            grafico = graficar_matriz(matriz)
            if grafico:
                try:
                    grafico.render('matriz', format='png', view=True) 
                    print("Gráfica generada y guardada como 'matriz.png'.")
                except Exception as e:
                    print(f"Error al generar la gráfica: {e}")
            else:
                print("No se pudo generar la gráfica.")


        elif opcion == "6":
            print("")
            print("Regresa Pronto :)")
            break

        else:
            print("\n Seleccione una opción válida...")
            input("Presione una tecla para continuar...")
            


Menu()