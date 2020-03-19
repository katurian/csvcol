import os       
import csv

def addColumns(inputCSV, outputCSV, cols):
    cols = sorted(cols, reverse=True)
    with open(inputCSV, "r") as input:
        reader = csv.reader(input)
        with open(outputCSV, "w", newline='') as output:
            writer = csv.writer(output)
            for row in reader:
                writer.writerow([row[n] for n in cols])
     os.remove(inputCSV)
