import csv

def read_header():
    with open("Dataset.csv", "r") as file:
        read_file = file.readline()
        header = read_file.splitlines()
        header = header[0].split(",")
        return header

def read_data_csv():
    with open("Dataset.csv", "r") as file:
        cities = list(csv.reader(file, delimiter=","))
    return cities

def read_data():
    with open("Dataset.csv", "r") as f:
        read = f.read().splitlines()
        data = []
        for i in read:
            row = i.split(",")
            data.append(row)
    return data




# ©Zairul Mazwan©
