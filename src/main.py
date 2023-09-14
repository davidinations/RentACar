import features as ft
import winsound
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkcalendar import DateEntry

# Function to create GUI
def transition():
        global bottom_frame, top_frame
        bottom_frame.grid_forget()
        top_frame.grid_forget()
        main_menu()

def main_menu():               
        global top_frame, bottom_frame, mid_frame, tree_frame
        
        # create a top frames
        top_frame = Frame(root, width=1100, height=500, bg='grey')
        top_frame.grid(row=0, column=0, padx=40, pady=50)

        # create a bottom frames
        bottom_frame = Frame(root, width=1175, height=100, bg='grey')
        bottom_frame.grid(row=1, column=0, padx=40, pady=10)

        # Add a label to the top frame
        label_selamat_datang = Label(top_frame, text="Selamat Datang di Aplikasi Rental Mobil", bg='grey', font=("Helvetica", 20), height=7)
        label_selamat_datang.grid(row=0, column=0, padx=355, pady=100)
        
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

def add_menu():                
        global top_frame, bottom_frame, entry_nik, button_validate
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        top_frame = Frame(root, width=1175, height=50, bg='grey')
        top_frame.grid(row=0, column=0, padx=45, pady=30)

        bottom_frame = Frame(root, width=1175, height=500, bg='grey')
        bottom_frame.grid(row=1, column=0, padx=60, pady=20)

        # create a label identitas + entry identitas
        label_nik = Label(top_frame, text="NIK", bg='grey', width=10, font=("Helvetica", 20))
        label_nik.grid(row=0, column=0, padx=10, pady=10)

        entry_nik = Entry(top_frame, width=100)
        entry_nik.grid(row=0, column=1, padx=30, pady=10)

        # add button after entry nik to validate
        button_validate = Button(top_frame, text="Validate", width=10, height=1, command=add_get_entry_nik)
        button_validate.grid(row=0, column=2, padx=10, pady=10)

        # add button after validate to exit menu
        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=10, pady=10)

def add_get_entry_nik():
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

def add_identity():            
        global entry_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar, button_validate

        button_validate.grid_forget()

        # add button after validate to exit menu
        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=10, pady=10)

        # Make Entry NIK Read Only
        lock_nik_value = StringVar(value=entry_nik.get())
        lock_entry_nik = Entry(top_frame, width=120, textvariable=lock_nik_value, state='readonly')
        lock_entry_nik.grid(row=0, column=1, padx=30, pady=10)
        
        # create a label nama + entry nama
        label_nama = Label(bottom_frame, text="Nama", bg='grey', font=("Helvetica", 20))
        label_nama.grid(row=0, column=1, padx=10, pady=10)

        entry_nama = Entry(bottom_frame, width=30)
        entry_nama.grid(row=0, column=2, padx=10, pady=10)

        # create a label mobil + entry mobil
        label_mobil = Label(bottom_frame, text="Mobil", bg='grey', font=("Helvetica", 20))
        label_mobil.grid(row=1, column=1, padx=10, pady=10)

        entry_mobil = Entry(bottom_frame, width=30)
        entry_mobil.grid(row=1, column=2, padx=10, pady=10)

        # create a label harga + entry harga
        label_harga = Label(bottom_frame, text="Harga (Rupiah)", bg='grey', font=("Helvetica", 20))
        label_harga.grid(row=2, column=1, padx=10, pady=10)

        entry_harga = Entry(bottom_frame, width=30)
        entry_harga.grid(row=2, column=2, padx=10, pady=10)

        # create a label tanggal masuk + entry tanggal masuk
        label_tanggal_masuk = Label(bottom_frame, text="Tanggal Masuk", bg='grey', font=("Helvetica", 20))
        label_tanggal_masuk.grid(row=3, column=1, padx=10, pady=10)

        entry_tanggal_masuk = DateEntry(bottom_frame, width=30, background='darkblue', foreground='white', borderwidth=2)
        entry_tanggal_masuk.grid(row=3, column=2, padx=10, pady=10)

        # create a label status + entry status
        label_status = Label(bottom_frame, text="Status", bg='grey', font=("Helvetica", 20))
        label_status.grid(row=5, column=1, padx=10, pady=10)

        entry_status = Entry(bottom_frame, width=30)
        entry_status.grid(row=5, column=2, padx=10, pady=10)

        # create a label tanggal keluar + entry tanggal keluar
        label_tanggal_keluar = Label(bottom_frame, text="Tanggal Keluar", bg='grey', font=("Helvetica", 20))
        label_tanggal_keluar.grid(row=4, column=1, padx=10, pady=10)

        entry_tanggal_keluar = DateEntry(bottom_frame, width=30, background='darkblue', foreground='white', borderwidth=2)
        entry_tanggal_keluar.grid(row=4, column=2, padx=10, pady=10)

        # add buttons to the bottom frame
        button_add = Button(bottom_frame, text="Add", width=30, height=1, command=add_get_entry_data)
        button_add.grid(row=6, column=1, padx=8, pady=10, sticky='w')

def add_get_entry_data():
        global entry_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        data_nik = entry_nik.get()
        data_nama = entry_nama.get()
        data_mobil = entry_mobil.get()
        data_harga = entry_harga.get()
        data_tanggal_masuk = entry_tanggal_masuk.get_date()
        data_status = entry_status.get()
        data_tanggal_keluar = entry_tanggal_keluar.get_date()
        result = messagebox.askyesno(title="Confirmation", message="Apakah anda yakin ingin menambahkan data ini?")
        if result:
                pesan = f"Data dengan NIK {data_nik} berhasil ditambahkan"
                showinfo(title="Success",message=pesan)
                ft.add_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar)
                add_menu()
        else:
                add_menu()

def show_menu():                
        global top_frame, bottom_frame, button_show_all, button_show_by_nik, button_exit
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        top_frame = Frame(root, width=1175, height=500, bg='grey')
        top_frame.grid(row=1, column=0, padx=50, pady=50)

        # add 3 buttons to the bottom frame
        button_show_all = Button(top_frame, text="Show All", width=30, height=3, command=show_get_length)
        button_show_all.grid(row=0, column=0, padx=480, pady=50)

        button_show_by_nik = Button(top_frame, text="Show By NIK", width=30, height=3, command=show_by_nik)
        button_show_by_nik.grid(row=1, column=0, padx=480, pady=50)

        button_exit = Button(top_frame, text="Exit", width=30, height=3, command=transition)
        button_exit.grid(row=2, column=0, padx=480, pady=50)

def show_get_length():                
        ft.show_validate()
        if ft.show_validate() == False:
                pesan = "Data masih kosong silahkan tambah data terlebih dahulu"
                showinfo(title="Warning",message=pesan)
                pass
        else:
                button_show_all.grid_forget()
                button_show_by_nik.grid_forget()
                button_exit.grid_forget()
                show_all()

def show_all():                 
        global top_frame

        button_exit = Button(top_frame, text="Exit", width=30, height=3, command=show_menu)
        button_exit.grid(row=2, column=0, padx=480, pady=50)

        # create a new frame inside the right frame
        tree_frame = Frame(top_frame, width=1100, height=500, bg='grey')
        tree_frame.grid(row=0, column=0, padx=10, pady=50)  

        # create a new scrollbar widget
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create a Treeview widger and add it to the new frame
        my_tree = ttk.Treeview(tree_frame)
        my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        # configure the scrollbar to scroll the Treeview widget
        my_tree.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.configure(command=my_tree.yview)

        # add columns to the Treeview widget
        my_tree['columns'] = ('NIK', 'Name', 'Car', 'DateIn', 'DateOut', 'Price', 'Status')

        # set column headings
        my_tree.heading('#0', text='No')
        my_tree.column('#0', width=50)
        my_tree.heading('NIK', text='NIK')
        my_tree.column('NIK', width=150)
        my_tree.heading('Name', text='Name')
        my_tree.column('Name', width=150)
        my_tree.heading('Car', text='Car')
        my_tree.column('Car', width=150)
        my_tree.heading('DateIn', text='Date In')
        my_tree.column('DateIn', width=150)
        my_tree.heading('DateOut', text='Date Out')
        my_tree.column('DateOut', width=150)
        my_tree.heading('Price', text='Harga (Rupiah)')
        my_tree.column('Price', width=150)
        my_tree.heading('Status', text='Status')
        my_tree.column('Status', width=100)

        ft.show_full_data(my_tree)

def show_by_nik():             
        print("Show By NIK")

def edit_menu():                
        global top_frame, bottom_frame
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        mid_frame = Frame(root, width=1175, height=500, bg='grey')
        mid_frame.grid(row=1, column=0, padx=50, pady=50)

def delete_menu():             
        global top_frame, bottom_frame
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        mid_frame = Frame(root, width=1175, height=500, bg='grey')
        mid_frame.grid(row=1, column=0, padx=50, pady=50)

def exit_menu():                
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