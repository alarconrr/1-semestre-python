print("")
import csv

with open('actividadtrabajadores',newline='') as file:
        reader= csv.writer(file)
        for now in reader:
                print()
