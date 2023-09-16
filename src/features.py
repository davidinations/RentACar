import main
import csv
import pandas as pd

path = "D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\RentACar\\data\\data.csv"

def nik_validate(data_nik):
    global path
    primary_keys = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row and len(row) > 0:
                primary_keys.append(row[0])

    data_list = primary_keys
    if data_nik in data_list:
        return True
    else:
        return False

def add_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar):
    global path
    rows = [[data_nik, data_nama, data_mobil, data_tanggal_masuk, data_tanggal_keluar, data_harga, data_status]]

    with open(path, 'a', newline='\n') as file:
        exampleWriter = csv.writer(file, delimiter=';')
        exampleWriter.writerows(rows)

def show_full_data(my_tree):
    count = 1
    # add sample data to the Treeview widget
    with open(path, 'r') as file:
            exampleReader = csv.reader(file, delimiter=";")
            next(exampleReader)
            for row in exampleReader:
                my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                count += 1  

def show_by_nik(my_tree, data_nik):
    count = 1
    # add sample data to the Treeview widget
    with open(path, 'r') as file:
            exampleReader = csv.reader(file, delimiter=";")
            for row in exampleReader:
                if row[0] == data_nik:
                    my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def show_validate():
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in reader)

    if row_count > 0:
        return True
    else:
        return False

def edit_get_data(data_nik):
    global data_nama, data_mobil, data_tanggal_masuk, data_tanggal_keluar, data_harga, data_status
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0] == data_nik:
                return row
    
def edit_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar):
    global path
    # read the CSV file into a list of dictionaries
    data = []
    # open the CSV file and turn it into a list of dictionaries
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data.append(row)

    # find the dictionary in the list that matches the primary key value
    for row in data:
        if row["nik"] == data_nik:
            # update the values of the desired columns in the dictionary
            row["name"] = data_nama
            row["merk"] = data_mobil
            row["start_date"] = data_tanggal_masuk
            row["end_date"] = data_tanggal_keluar
            row["price"] = data_harga
            row["status"] = data_status
            break

    # rewrite the CSV file from the list of dictionaries
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(data)

def delete_data(data_nik):
    # Read the CSV file into a list of rows
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        rows = list(reader)

    # Find the index of the row where the first column contains the word "Jane"
    index = None
    for i, row in enumerate(rows):
        if row[0] == data_nik:
            index = i
            break

    # If the row was found, delete it from the list
    if index is not None:
        rows.pop(index)
        # Write the updated list to the CSV file
        with open(path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(rows)