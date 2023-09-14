import main
import csv
import pyinputplus as pypi

path = "D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\RentACar\\data\\data.csv"

def add_validate(data_nik):
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
            for row in exampleReader:
                my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                count += 1    

def show_validate():
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in reader)

    if row_count > 0:
        return True
    else:
        return False

def edit():
    print("Edit")

def delete():
    print("Delete")

def exit():
    print("Exit")