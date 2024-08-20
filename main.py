from tkinter import Tk, filedialog
import xml.etree.ElementTree as ET
import graphviz

def cargarArchivo():

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    print("Archivo Seleccionado: ", archivo)
   
    
    archivo_texto = open(archivo, "r", encoding="utf8")
    print("\n",archivo_texto.read())
    #archivo_texto.close()
    #lecturaXml(archivo)
    print( "\n Carga Exitosa")



def grafica(cod,columnas,filas):
    contfilas = 1
    print("Matriz de:...")
    print(columnas, "  Columnas")
    print( filas, "  Filas ")
    fila =''
    cont = 0
    cn=1
    contenidoTabla = '''<TR>'''
    grafica = graphviz.digraph(filename='structs_revisited.gv')
    
    for c in cod:
        if c == 'B':
            grafica.attr('node',shape='record', style='filled', color='black')
            grafica.node(str(cn) ,label= c)
            contenidoTabla += '<TD  COLOR = "WHITE" BGCOLOR="BLACK">     </TD>'
            
            cn += 1
            cont += 1
            fila += c
        elif c=='W':
            grafica.attr('node',shape='record', style='filled',color="lightgrey",bgcolor='black')
            grafica.node(str(cn) ,label= c)
            contenidoTabla += '<TD   COLOR = "BLACK" BGCOLOR="WHITE">     </TD>'
            cn += 1
            cont += 1
            
            fila += c

       
        if cont >= int(columnas):
            print(fila)
            fila = ''
            cont = 0
            
            
            contenidoTabla +='</TR>'
            if contfilas != int(filas):

                contenidoTabla +='<TR>'
                contfilas += 1
            else:
                break
        

   
    grafica.node('structx', '''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="3" CELLPADDING="3">
        '''
        +contenidoTabla+
        '''
        </TABLE>>''')     
            
    grafica.view()




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
            cargarArchivo()
        
        elif opcion == "2":
            print("")
            #menu2()
            print("Procesar Archivo")

        elif opcion == "3":
            print("")
           # pisos.mostrarPisos_Orden()
            print("Escribir Archivo de Salida ")

        elif opcion == "4":
            print(f"\n --Leonel Antonio Gonzalez Garcia \n --201709088 \n --Introduccion a la Programacion y Computacion 2 seccion N \n --Ingenieria en Ciencias y Sistemas \n --4to Semestre")
        
        elif opcion == "5":
            print("\nGenerar Grafica\n")
            grafica()

        elif opcion == "6":
            print("")
            print("Regresa Pronto :)")
            break

        else:
            print("\n Seleccione una opción válida...")
            input("Presione una tecla para continuar...")
            


Menu()