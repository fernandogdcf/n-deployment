import csv

saida = "baseline.csv"
file = "indice.txt"
lista = []

with open(file) as f:
    for e in f:
        if(e == '\n'):
            continue
        x = e.split('(')[1].split(',')[0]
        y = e.split(',')[1].split(')')[0].replace(' ', '')
        pair =  [x, y]
        lista.append(pair)

with open(saida, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
