#Menu bienvenida
while True:
    print("1-.Ingresar el trabajador.");
    print("2-.Listar todos los trabajadores.");
    print("3-.Imprimir planilla de sueldos.");
    print("4-.Salir del programa.");
    try:
        opc=int(input("Ingrese una opcion-->"));
    except ValueError:
        if opc==1:
            print("Ingrese el nombre del trabajador.")
            input("-->");
        else:
            if opc==2:
                print("")

#manejo de archivos .csv
import csv
encabezado=['Trabajador','Cargo','Sueldo Bruto','Desc. Salud','Desc.Afp','Liquido a pagar'];
matrizDatos=[
    ['Homero Simpson','CEO','1000000','70000','120000','810000'],
]
#Se crea el contexto del archivo para abrir un archivo .csv
with open('menus/datos_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
    archivo_csv=csv.write(archivo_csv);
    archivo_csv=writerow(encabezado);
    archivo_csv=writerow(matrizDatos);
print("Se creo el archivo correctaente.");

#Leer archivo csv
import csv
#Sintaxis open
with open('menus/datos_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
    csv.reader(archivo_csv);
archivo_csv=csv.dictwriter(archivo_csv)