import main
import csv
import pyinputplus as pypi

path = "D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\RentACar\\data\\data.csv"

def transition_add():
    main.add_identity()
    top.destroy()

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
    rows = [[data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar]]

    with open(path, 'a') as file:
        exampleWriter = csv.writer(file, delimiter=';')
        exampleWriter.writerows(rows)

def show():
    print("Show")
    
def edit():
    print("Edit")

def delete():
    print("Delete")

def exit():
    print("Exit")