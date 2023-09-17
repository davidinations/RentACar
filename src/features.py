import main
import csv
import pandas as pd

path = "D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\RentACar\\data\\data.csv"

def nik_validate(data_nik):
    """
    Fungsi untuk validasi NIK
    Args:
        data_nik (int): NIK yang akan divalidasi

    Returns:
        boolean: True jika NIK valid, False jika NIK tidak valid
    """    
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
    """
    Fungsi untuk menambahkan data ke dalam file csv
    Args:
        data_nik (int): nik yang akan ditambahkan
        data_nama (string): nama yang akan ditambahkan
        data_mobil (string): merk mobil yang akan ditambahkan
        data_harga (int): harga yang akan ditambahkan
        data_tanggal_masuk (date): tanggal masuk yang akan ditambahkan dengan input format yyyy-mm-dd
        data_status (options): status yang akan ditambahkan dengan input options ("Progress", "Done")
        data_tanggal_keluar (date): tanggal keluar yang akan ditambahkan dengan input format yyyy-mm-dd
    """    
    global path
    rows = [[data_nik, data_nama, data_mobil, data_tanggal_masuk, data_tanggal_keluar, data_harga, data_status]]

    with open(path, 'a', newline='\n') as file:
        exampleWriter = csv.writer(file, delimiter=';')
        exampleWriter.writerows(rows)

def show_full_data(my_tree):
    """
    Fungsi untuk menampilkan data dari file csv ke dalam Treeview widget
    Args:
        my_tree (table): Treeview widget yang akan ditampilkan dengan module tkinter
    """    
    count = 1
    # add sample data to the Treeview widget
    with open(path, 'r') as file:
            exampleReader = csv.reader(file, delimiter=";")
            next(exampleReader)
            for row in exampleReader:
                my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                count += 1  

def show_by_nik(my_tree, data_nik):
    """
    Fungsi untuk menampilkan data dari file csv ke dalam Treeview widget berdasarkan NIK
    Args:
        my_tree (table): Treeview widget yang akan ditampilkan dengan module tkinter
        data_nik (int): NIK yang akan ditampilkan
    """
    count = 1
    # add sample data to the Treeview widget
    with open(path, 'r') as file:
            exampleReader = csv.reader(file, delimiter=";")
            for row in exampleReader:
                if row[0] == data_nik:
                    my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def show_validate():
    """
    Fungsi untuk validasi jumlah data dalam file csv
    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in reader)

    if row_count > 0:
        return True
    else:
        return False

def edit_get_data(data_nik):
    """
    Fungsi untuk mendapatkan data dari file csv berdasarkan NIK yang akan diedit
    Args:
        data_nik (int): NIK yang akan ditampilkan
    Returns:
        row (list): data yang akan ditampilkan
    """
    global data_nama, data_mobil, data_tanggal_masuk, data_tanggal_keluar, data_harga, data_status
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0] == data_nik:
                return row
    
def edit_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar):
    """
    Fungsi untuk mengedit data dalam file csv
    Args:
        data_nik (int): NIK yang akan diedit
        data_nama (string): nama yang akan diedit
        data_mobil (string): merk mobil yang akan diedit
        data_harga (int): harga yang akan diedit
        data_tanggal_masuk (date): tanggal masuk yang akan diedit dengan input format yyyy-mm-dd
        data_status (string): status yang akan diedit dengan input options ("Progress", "Selesai")
        data_tanggal_keluar (date): tanggal keluar yang akan diedit dengan input format yyyy-mm-dd
    """    
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
    """
    Fungsi untuk menghapus data dalam file csv
    Args:
        data_nik (int): NIK yang akan jadi acuan untuk menghapus data
    """
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