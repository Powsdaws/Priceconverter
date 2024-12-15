import json
import csv

#https://medium.com/analytics-vidhya/cleaning-up-data-and-turning-a-csv-file-into-json-using-python-72e67c2ee76e

FILE_INPUT = "C:\ITU\EgneProjekter\Priceconverter\Data\Walmart\WMT_Grocery_202209.csv"
FILE_OUTPUT = "C:\ITU\EgneProjekter\Priceconverter\Data\Walmart\cleanupWalmart.json"

print("HELLO")



def readDataFromCSV():
    data_list = []
    with open(FILE_INPUT, mode="r", encoding="utf-8") as csv_read:
        file_reader = csv.reader(csv_read, delimiter=",")

        for field in file_reader:
            if (field[0] != "index"):
                data_list.append({
                    "name": transfromName(field[8]),
                    "price": transfromPrice(field[11])
                })
        
        writeToJSON(data_list)

def writeToJSON(data):
    with open(FILE_OUTPUT, "wt", encoding="utf-8") as json_write:
        json_write.write("[")
        for i, result in enumerate(data):
            json.dump(result, json_write, sort_keys=True, indent=4, ensure_ascii=False)
            if i < len(data) - 1:
                json_write.write(",")
        json_write.write("]")

def transfromName(name):
    return name.split(',')[0].split('-')[0]

def transfromPrice(price):
    return price.replace("$", "")

readDataFromCSV()