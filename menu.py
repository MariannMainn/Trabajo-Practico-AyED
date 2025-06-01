#aplicacion(trabajo practico)
var0="INICIO"
print(var0.center(100,"*"))

# IMPORTS DE MODULOS NECESARIOS--->
import os
from pathlib import Path

#---INICIO---

defaultdirectory = Path(".")


on = True
while on is not False:
    print("""Opciones:
 1 - Listar todos los archivos
 2 - Mostrar el directorio de trabajo actual
 3 - Listar los archivos por patron
 4 - Crear una nueva carpeta 
 5 - Borrar una carpeta 
 6 - Copiar un archivo  
 0 - Salir del Programa\n""")
    
    #funciones de las opciones
    opcion = int(input("ingrese la opcion deseada: "))

    if opcion == 1:
            print("---------LISTAR ELEMENTOS----------")
            for file in defaultdirectory.iterdir():
                if file.is_dir():
                        print(f"»[carpeta] {file.name}")
                else:       
                        print (f"»[archivo] {file.name}")
                   
    if opcion ==2:
            print("opcion 2.mostrar directorio")
            dirActual = Path.cwd()
            print(dirActual)

    if opcion == 3:
           buscar_archivo = int(input("buscar archivos por \n1.nombre \n2.extension: "))
           if buscar_archivo == 1:
                namearch = input("ingrese el nombre del archivo/carpeta: ")
           for file in defaultdirectory.glob(f"*{namearch}*.*"):
                        print(file)
           if buscar_archivo ==2:
                extarch= input("extension del archivo... ")
                for file in defaultdirectory.glob(f"**.{extarch}"):
                        print(file)

    
    if opcion == 4:   
        name_folder = input("ingrese nombre de nueva carpeta:-->")
        pathDir = Path(f"./{name_folder}")
        
        try:
                pathDir.mkdir()
                print("carpeta creado exitosamente...")
        except Exception as e:
                print("error esta carpeta ya existe")



            
    if opcion == 0:
            print("opcion 0.Salida")
            opcion = 0
            break
    
    
    #condicional para pausar el ciclo y que no se repita innecesariamente
    condition = input("\ncontinuar?")
    if condition == "si":
           print("")
    elif condition == "no":
           on = False


#control para probar que el ciclo termino exitosamente
print("fuera del programa")
