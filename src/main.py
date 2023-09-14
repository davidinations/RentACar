import features as ft
import winsound
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox


# Function to create GUI
def transition():
        global bottom_frame, top_frame
        bottom_frame.grid_forget()
        top_frame.grid_forget()
        main_menu()

def main_menu():                # Semua Menu dan Exit
        global top_frame, bottom_frame
        
        # create a top frames
        top_frame = Frame(root, width=1175, height=500, bg='grey')
        top_frame.grid(row=0, column=0, padx=50, pady=50)

        # create a bottom frames
        bottom_frame = Frame(root, width=1175, height=100, bg='grey')
        bottom_frame.grid(row=1, column=0, padx=50, pady=10)

        # Add a label to the top frame
        label_selamat_datang = Label(top_frame, text="Selamat Datang di Aplikasi Rental Mobil", bg='grey', font=("Helvetica", 20), height=7)
        label_selamat_datang.grid(row=0, column=0, padx=340, pady=100)
        
        # add 5 buttons to the bottom frame
        button_show = Button(bottom_frame, text="Show", width=30, height=3, command=show_menu)
        button_show.grid(row=0, column=0, padx=10, pady=10)
        button_add = Button(bottom_frame, text="Add", width=30, height=3, command=add_menu)
        button_add.grid(row=0, column=1, padx=10, pady=10)
        button_edit = Button(bottom_frame, text="Edit", width=30, height=3, command=edit_menu)
        button_edit.grid(row=0, column=2, padx=10, pady=10)
        button_delete = Button(bottom_frame, text="Delete", width=30, height=3, command=delete_menu)
        button_delete.grid(row=0, column=3, padx=10, pady=10)
        button_exit = Button(bottom_frame, text="Exit", width=30, height=3, command=exit_menu)
        button_exit.grid(row=0, column=4, padx=10, pady=10)

def add_menu():                 # Input Primary Key dan Exit
        global top_frame, bottom_frame, entry_nik, button_validate
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        top_frame = Frame(root, width=1175, height=50, bg='grey')
        top_frame.grid(row=0, column=0, padx=50, pady=30)

        bottom_frame = Frame(root, width=1175, height=500, bg='grey')
        bottom_frame.grid(row=1, column=0, padx=50, pady=20)

        # create a label identitas + entry identitas
        label_nik = Label(top_frame, text="NIK", bg='grey', width=10)
        label_nik.grid(row=0, column=0, padx=10, pady=10)

        entry_nik = Entry(top_frame, width=100)
        entry_nik.grid(row=0, column=1, padx=30, pady=10)

        # add button after entry nik to validate
        button_validate = Button(top_frame, text="Validate", width=10, height=1, command=get_entry_nik)
        button_validate.grid(row=0, column=2, padx=10, pady=10)

        # add button after validate to exit menu
        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=10, pady=10)

def get_entry_nik():
        global entry_nik
        data_nik = entry_nik.get()
        ft.add_validate(data_nik)       
        if ft.add_validate(data_nik) == False:
                pesan = f"Data dengan NIK {data_nik} belum ada silahkan tambah data lain terlebih dahulu"
                showinfo(title="Success",message=pesan)
                add_identity()
        else:
                pesan = f"Data dengan NIK {data_nik} sudah ada"
                showinfo(title="Warning",message=pesan)

def add_identity():             # Input Nama, Mobil, Harga, Tanggal Masuk, Status, Tanggal Keluar, dan Exit
        global entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar, button_validate

        button_validate.grid_forget()

        # add button after validate to exit menu
        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=110, pady=10)

        # Make Entry NIK Read Only
        lock_nik_value = StringVar(value=entry_nik.get())
        lock_entry_nik = Entry(top_frame, width=120, textvariable=lock_nik_value, state='readonly')
        lock_entry_nik.grid(row=0, column=1, padx=30, pady=10)
        
        # create a label nama + entry nama
        label_nama = Label(bottom_frame, text="Nama", bg='grey')
        label_nama.grid(row=0, column=1, padx=10, pady=10)

        entry_nama = Entry(bottom_frame, width=30)
        entry_nama.grid(row=0, column=2, padx=10, pady=10)

        # create a label mobil + entry mobil
        label_mobil = Label(bottom_frame, text="Mobil", bg='grey')
        label_mobil.grid(row=1, column=1, padx=10, pady=10)

        entry_mobil = Entry(bottom_frame, width=30)
        entry_mobil.grid(row=1, column=2, padx=10, pady=10)

        # create a label harga + entry harga
        label_harga = Label(bottom_frame, text="Harga", bg='grey')
        label_harga.grid(row=2, column=1, padx=10, pady=10)

        entry_harga = Entry(bottom_frame, width=30)
        entry_harga.grid(row=2, column=2, padx=10, pady=10)

        # create a label tanggal masuk + entry tanggal masuk
        label_tanggal_masuk = Label(bottom_frame, text="Tanggal Masuk", bg='grey')
        label_tanggal_masuk.grid(row=3, column=1, padx=10, pady=10)

        entry_tanggal_masuk = Entry(bottom_frame, width=30)
        entry_tanggal_masuk.grid(row=3, column=2, padx=10, pady=10)

        # create a label status + entry status
        label_status = Label(bottom_frame, text="Status", bg='grey')
        label_status.grid(row=5, column=1, padx=10, pady=10)

        entry_status = Entry(bottom_frame, width=30)
        entry_status.grid(row=5, column=2, padx=10, pady=10)

        # create a label tanggal keluar + entry tanggal keluar
        label_tanggal_keluar = Label(bottom_frame, text="Tanggal Keluar", bg='grey')
        label_tanggal_keluar.grid(row=4, column=1, padx=10, pady=10)

        entry_tanggal_keluar = Entry(bottom_frame, width=30)
        entry_tanggal_keluar.grid(row=4, column=2, padx=10, pady=10)

        # add buttons to the bottom frame

        button_add = Button(bottom_frame, text="Add", width=30, height=1, command=get_entry_data)
        button_add.grid(row=6, column=1, padx=8, pady=10, sticky='w')

def get_entry_data():
        global entry_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        data_nik = entry_nik.get()
        data_nama = entry_nama.get()
        data_mobil = entry_mobil.get()
        data_harga = entry_harga.get()
        data_tanggal_masuk = entry_tanggal_masuk.get()
        data_status = entry_status.get()
        data_tanggal_keluar = entry_tanggal_keluar.get()
        result = messagebox.askyesno(title="Confirmation", message="Apakah anda yakin ingin menambahkan data ini?")
        if result:
                ft.add_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar)
                pesan = f"Data dengan NIK {data_nik} berhasil ditambahkan"
                showinfo(title="Success",message=pesan)
                add_menu()
        else:
                add_menu()

def show_menu():                # Show All Data, Show By Primary Key, dan Exit
        global top_frame, bottom_frame
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        mid_frame = Frame(root, width=1175, height=500, bg='grey')
        mid_frame.grid(row=1, column=0, padx=50, pady=50)

def edit_menu():                # Input Primary Key, Edit Data, dan Exit
        global top_frame, bottom_frame
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        mid_frame = Frame(root, width=1175, height=500, bg='grey')
        mid_frame.grid(row=1, column=0, padx=50, pady=50)

def delete_menu():              # Input Primary Key, Delete Data, dan Exit
        global top_frame, bottom_frame
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        mid_frame = Frame(root, width=1175, height=500, bg='grey')
        mid_frame.grid(row=1, column=0, padx=50, pady=50)

def exit_menu():                # Exit
        root.destroy()

if __name__ == '__main__':
        # create a windows
        root = tkinter.Tk()
        # config icon windows
        root.iconbitmap("D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\RentACar\\assets\\images\\favicon.ico")
        # config size windows
        root.geometry("1280x720+150-50")   # <width>x<height>+<x_position>+<y_position>
        # make a windows size fixed
        root.maxsize(1280, 720)
        root.minsize(1280, 720)
        # disable maximize button
        root.resizable(False, False)
        # config title windows
        root.title("Rent A Car (Personal Project)")
        # config background color windows
        root.config(bg="#4a9c46")
        # path into csv file
        path = "D:\\Users\\david\\Onedrive\\Documents\\Project\\Application\\Education\\Python\\Personal\\data\\data.csv"

        # Action Code
        main_menu()

        # make a windows loop
        root.mainloop()