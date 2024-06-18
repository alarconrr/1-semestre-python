



   trabajador= 
#manejo de archivos .csv
import csv
encabezado=['Trabajador','Cargo','Sueldo Bruto','Desc.Salud','Desc.Afp','Liquido a pagar'];
matrizDatos=[
    ['Homero Simpson','CEO','1000000','70000','120000','810000'],
]
#Se crea el contexto del archivo para abrir un archivo .csv
with open('datos_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
    archivo_csv=csv.writer(archivo_csv);
    archivo_csv.writerow(encabezado);
    archivo_csv.writerow(matrizDatos);
print("Se creo el archivo correctaente.");

"""
#Leer archivo csv
import csv
#Sintaxis open
with open('datos_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
    csv.reader(archivo_csv);
archivo_csv=csv.dictwriter(archivo_csv);
for x in archivo_csv:
        trabajador=x['Trabajador'];
        cargo=x['Cargo'];
        sueldo_bruto=x['Sueldo Bruto'];
        desc_salud=x['Desc.Salud'];
        desc_afp=x['Desc.Afp'];
        liquido_a_pagar=x['Liquido a pagar'];"""