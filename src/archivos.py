#Lectura del csv
import csv

def readFile():
    barcos = []
    with open(r"C:\Users\thmon\OneDrive\Documents\Universidad\Labo Progra 2\Final Boss Final\G01_MonterosForte_FinalBoss\ships.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            barcos.append(row)
    return barcos
