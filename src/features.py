import csv

path = "../RentACar/data/data.csv"

def nik_validate(data_nik):
    """
    Validate NIK
    """
    global path
    primary_keys = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        primary_keys = [row[0] for row in reader if row and len(row) > 0]

    return data_nik in primary_keys

def add_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar):
    """
    Add data to csv file
    """
    global path
    rows = [[data_nik, data_nama, data_mobil, data_tanggal_masuk, data_tanggal_keluar, data_harga, data_status]]

    with open(path, 'a', newline='\n') as file:
        exampleWriter = csv.writer(file, delimiter=';')
        exampleWriter.writerows(rows)

def show_full_data(my_tree):
    """
    Show data from csv file in Treeview widget
    """
    count = 1
    with open(path, 'r') as file:
        exampleReader = csv.reader(file, delimiter=";")
        next(exampleReader)
        for row in exampleReader:
            my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            count += 1  

def show_by_nik(my_tree, data_nik):
    """
    Show data from csv file in Treeview widget by NIK
    """
    count = 1
    with open(path, 'r') as file:
        exampleReader = csv.reader(file, delimiter=";")
        for row in exampleReader:
            if row[0] == data_nik:
                my_tree.insert(parent='', index='end', iid=count, text=count, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def show_validate():
    """
    Validate number of data in csv file
    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in reader)

    return row_count > 0

def edit_get_data(data_nik):
    """
    Get data from csv file by NIK for editing
    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0] == data_nik:
                return row
    
def edit_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar):
    """
    Edit data in csv file
    """
    global path
    data = []
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        data = [row for row in reader]

    for row in data:
        if row["nik"] == data_nik:
            row["name"] = data_nama
            row["merk"] = data_mobil
            row["start_date"] = data_tanggal_masuk
            row["end_date"] = data_tanggal_keluar
            row["price"] = data_harga
            row["status"] = data_status
            break

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(data)

def delete_data(data_nik):
    """
    Delete data from csv file
    """
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        rows = list(reader)

    index = None
    for i, row in enumerate(rows):
        if row[0] == data_nik:
            index = i
            break

    if index is not None:
        rows.pop(index)
        with open(path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(rows)