import os       
import csv
from zipfile import ZipFile

def addColumns(inputCSV, outputCSV, cols):
    cols = sorted(cols, reverse=True)
    with open(inputCSV, "r") as inp:
        reader = csv.reader(inp)
        with open(outputCSV, "w", newline='') as output:
            writer = csv.writer(output)
            for row in reader:
                writer.writerow([row[n] for n in cols])
     os.remove(inputCSV)
        
def removeColumns(inputCSV, outputCSV, cols):   
    with open(inputCSV, "r") as inp:
        reader = csv.reader(inp)
        with open(outputCSV, "w", newline='') as output:
            writer = csv.writer(output)
            for row in reader:
                for index in cols:
                    del row[index]
                writer.writerow(row)
    os.remove(inputCSV)
    
def fromZipExtractCSVs(inputZip):   
    with ZipFile(inputZip, 'r') as zipObj:
       files = zipObj.namelist()
       for fileName in files:
           if fileName.endswith('.csv'):
               zipObj.extract(fileName)
    os.remove(inputZip)
  
