#aplicacion(trabajo practico)
var0="INICIO"
print(var0.center(100,"*"))

# IMPORTS DE MODULOS NECESARIOS--->
import shutil
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
                   
    elif opcion ==2:
            print("opcion 2.mostrar directorio")
            dirActual = Path.cwd()
            print(dirActual)

    elif opcion == 3:
           print("opcion 3.ver archivos por referencia")
           buscar_archivo = int(input("buscar archivos por \n1.nombre \n2.extension: "))
           if buscar_archivo == 1:
                namearch = input("ingrese el nombre del archivo: ")
           for file in defaultdirectory.glob(f"*{namearch}*.*"):
                        print(file)
           if buscar_archivo ==2:
                extarch= input("extension del archivo... ")
                for file in defaultdirectory.glob(f"**.{extarch}"):
                        print(file)

    
    elif opcion == 4:   
        print("opcion 4. crear nueva carpeta")
        name_folder = input("ingrese nombre de nueva carpeta:-->")
        pathDir = Path(f"./{name_folder}")
        
        try:
                pathDir.mkdir()
                print("carpeta creado exitosamente...")
        except Exception as e:
                print("error esta carpeta ya existe")
                
                
    elif opcion == 5:
        print("opcion 5. borrar archivo/carpeta")
        borrar = input("nombre de la carpeta: ")
        condicion = str(input(f"desea borrar la carpeta {borrar} si /no :"))
        try:
            if condicion == "si":
                defaultdirectory= Path(f"./{borrar}")
                defaultdirectory.rmdir()
        except Exception as e:
                print("carpeta no encontrada")


    elif opcion == 6:
           print("opcion 6. copiar un archivo")
           arch = input("nombre del archivo :__")
           shutil.copy2(Path(f"./{arch}"),".")

            
    elif opcion == 0:
            print("opcion 0.Salida")
            opcion = 0
            break
    
    else:
           print("opcion incorrecta")
    
    
    #condicional para pausar el ciclo y que no se repita innecesariamente
    condition = input("\ncontinuar?")
    if condition == "si":
           print("")
    elif condition == "no":
           on = False


#control para probar que el ciclo termino exitosamente
print()
print("fuera del programa")
