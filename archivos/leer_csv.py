import csv

with open('archivos\\datos.csv') as archivo:
    reader = csv.reader(archivo)
    for i in reader:
        print(i)