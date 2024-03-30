import features as ft
import tkinter
import re
import babel.numbers
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import pygame.mixer

# Initialize the mixer module
pygame.mixer.init()

click_sound = pygame.mixer.Sound("../RentACar/assets/sounds/Click.wav")
error_sound = pygame.mixer.Sound("../RentACar/assets/sounds/Error.wav")
success_sound = pygame.mixer.Sound("../RentACar/assets/sounds/Success.wav")

def sort_data(treeview, column, reverse):
        """
        Fungsi untuk mengurutkan data pada tabel
        """        
        data = [(treeview.set(child, column), child) for child in treeview.get_children('')]

        data.sort(reverse=reverse)

        for index, (val, child) in enumerate(data):
                treeview.move(child, '', index)

        treeview.heading(column, command=lambda: sort_data(treeview, column, not reverse))

def validate_number(input):
        """
        mendeteksi inputan keyboard supaya hanya diperbolehkan angka dan maksimal 10 digit

        Args:
            input (string)

        Returns:
            boolean: Jika True maka diperbolehkan, jika False maka tidak diperbolehkan
        """        
        if input.isdigit() and len(input) <= 10:
                return True
        elif input == "":
                return True
        else:
                return False

def validate_alphabet(input):
        """
        mendeteksi inputan keyboard supaya hanya diperbolehkan huruf dan spasi

        Args:
            input (string)

        Returns:
            boolean: Jika True maka diperbolehkan, jika False maka tidak diperbolehkan
        """        
        pattern = r'^[a-zA-Z ]+$'

        if re.match(pattern, input) is not None or input == "":
                return True
        else:
                return False

def validate_digit(input):
        """
        mendeteksi inputan keyboard supaya hanya diperbolehkan angka

        Args:
            input (string)

        Returns:
            boolean: Jika True maka diperbolehkan, jika False maka tidak diperbolehkan
        """        
        if input.isdigit():
                return True
        elif input == "":
                return True
        else:
                return False

def nik_type_menu():
        """
        menu untuk memasukkan NIK
        """
        # Play the sound
        click_sound.play()
        
        global top_frame, bottom_frame, label_menu, entry_nik, button_exit
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        top_frame = Frame(root, width=1175, height=500, bg='grey')
        top_frame.grid(row=1, column=0, padx=50, pady=50)

        label_nik = Label(top_frame, text="NIK", bg='grey', width=10, font=("Helvetica", 20))
        label_nik.grid(row=0, column=0, padx=10, pady=10)

        validate_nik = (top_frame.register(validate_number), '%P')
        entry_nik = Entry(top_frame, width=60, validate="key", validatecommand=validate_nik)
        entry_nik.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_nik.grid(row=0, column=1, padx=30, pady=10)

def input_identity(data_nik):
        """
        Menu Untuk Memasukkan Identitas
        Args:
            data_nik (integer): NIK
        """        
        global top_frame, bottom_frame, button_show_all

        top_frame.grid_forget()
        bottom_frame.grid_forget()

        top_frame = Frame(root, width=1175, height=50, bg='grey')
        top_frame.grid(row=0, column=0, padx=100, pady=30)

        label_nik = Label(top_frame, text="NIK", bg='grey', width=10, font=("Helvetica", 20))
        label_nik.grid(row=0, column=0, padx=10, pady=10)

        lock_nik_value = StringVar(value=data_nik)
        lock_entry_nik = Entry(top_frame, width=52, textvariable=lock_nik_value, state='readonly')
        lock_entry_nik.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        lock_entry_nik.grid(row=0, column=1, padx=40, pady=10)
        
        label_nama = Label(top_frame, text="Nama", bg='grey', font=("Helvetica", 20))
        label_nama.grid(row=1, column=0, padx=40, pady=10)
        
        label_mobil = Label(top_frame, text="Mobil", bg='grey', font=("Helvetica", 20))
        label_mobil.grid(row=2, column=0, padx=40, pady=10)

        label_harga = Label(top_frame, text="Harga (Rupiah)", bg='grey', font=("Helvetica", 20))
        label_harga.grid(row=3, column=0, padx=40, pady=10)

        label_tanggal_masuk = Label(top_frame, text="Tanggal Masuk", bg='grey', font=("Helvetica", 20))
        label_tanggal_masuk.grid(row=4, column=0, padx=40, pady=10)

        label_tanggal_keluar = Label(top_frame, text="Tanggal Keluar", bg='grey', font=("Helvetica", 20))
        label_tanggal_keluar.grid(row=5, column=0, padx=40, pady=10)

        label_status = Label(top_frame, text="Status", bg='grey', font=("Helvetica", 20))
        label_status.grid(row=6, column=0, padx=40, pady=10)

def main_menu():               
        """
        Menu Utama
        """        
        global top_frame, bottom_frame
        
        top_frame = Frame(root, width=1100, height=500, bg='grey')
        top_frame.grid(row=0, column=0, padx=40, pady=50)

        bottom_frame = Frame(root, width=1175, height=100, bg='#4a9c46')
        bottom_frame.grid(row=1, column=0, padx=40, pady=10)

        label_selamat_datang = Label(top_frame, text="Selamat Datang di Aplikasi Rental Mobil", bg='grey', font=("Helvetica", 20), height=7)
        label_selamat_datang.grid(row=0, column=0, padx=355, pady=100)
        
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

def transition():         
        """
        Fungsi Untuk Animasi Kembali Ke Menu Utama
        """        
        # Play the sound
        click_sound.play()
        global bottom_frame, top_frame, label_menu
        bottom_frame.grid_forget()
        top_frame.grid_forget()
        label_menu.grid_forget()
        main_menu()

def add_menu():  
        """
        Menu Untuk Menambahkan Data
        """                 
        global label_menu
        nik_type_menu()

        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=40, pady=10)

        label_menu = Label(root, text=" Add Menu ", bg='#4a9c46', font=("Helvetica", 20), height=2)
        label_menu.grid(row=0, column=0, padx=20, pady=5)

        button_validate = Button(top_frame, text="Validate", width=10, height=1, command=add_get_entry_nik)
        button_validate.grid(row=0, column=2, padx=10, pady=10)

def add_get_entry_nik():
        """
        Fungsi Untuk Mendapatkan NIK Yang Dimasukkan saat Menambahkan Data
        """        
        global entry_nik, data_nik
        data_nik = entry_nik.get()
        if len(data_nik) != 10:
                # Play the sound
                error_sound.play()
                pesan = "NIK harus 10 digit"
                showinfo(title="Warning",message=pesan)
        else:
                ft.nik_validate(data_nik)       
                if ft.nik_validate(data_nik) == False:
                        success_sound.play()
                        pesan = f"Data dengan NIK {data_nik} belum ada silahkan tambah data lain terlebih dahulu"
                        showinfo(title="Success",message=pesan)
                        add_identity()
                else:
                        error_sound.play()
                        pesan = f"Data dengan NIK {data_nik} sudah ada"
                        showinfo(title="Warning",message=pesan)

def add_identity():
        """
        Menu Untuk Memasukkan Identitas
        """        
        global data_nik,entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        input_identity(data_nik)

        validate_name = (top_frame.register(validate_alphabet), '%P')
        entry_nama = Entry(top_frame, width=52, validate="key", validatecommand=validate_name)
        entry_nama.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_nama.grid(row=1, column=1, padx=40, pady=10)

        entry_mobil = Entry(top_frame, width=52)
        entry_mobil.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_mobil.grid(row=2, column=1, padx=40, pady=10)

        validate_price = (top_frame.register(validate_digit), '%P')
        entry_harga = Entry(top_frame, width=52, validate="key", validatecommand=validate_price)
        entry_harga.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_harga.grid(row=3, column=1, padx=40, pady=10)

        entry_tanggal_masuk = DateEntry(top_frame, width=50, background='darkblue', foreground='white', borderwidth=2, sticky='w')
        entry_tanggal_masuk.config(font=("Arial", 14))
        entry_tanggal_masuk.grid(row=4, column=1, padx=40, pady=10)

        entry_tanggal_keluar = DateEntry(top_frame, width=50, background='darkblue', foreground='white', borderwidth=2, sticky='w')
        entry_tanggal_keluar.config(font=("Arial", 14))
        entry_tanggal_keluar.grid(row=5, column=1, padx=40, pady=10)

        entry_status = tkinter.StringVar()
        options = ["Progress", "Selesai"]
        entry_status_options = tkinter.OptionMenu(top_frame, entry_status, "", *options)
        entry_status_options.configure(font=("Arial", 14), background="white", foreground="black", borderwidth=2, relief="groove", width=48)
        entry_status_options.grid(row=6, column=1, padx=40, pady=10)

        button_add = Button(top_frame, text="Add", width=30, height=3, command=add_get_entry_data)
        button_add.grid(row=7, column=0, padx=10, pady=30)

        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=add_menu)
        button_exit.grid(row=0, column=2, padx=30, pady=10)

def add_get_entry_data():
        """
        Fungsi Untuk Mendapatkan Data Yang Dimasukkan saat Menambahkan Data + konfirmasi
        """        
        global entry_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        data_nik = entry_nik.get()
        data_nama = entry_nama.get()
        data_mobil = entry_mobil.get()
        data_harga = entry_harga.get()
        data_tanggal_masuk = entry_tanggal_masuk.get_date()
        data_status = entry_status.get()
        data_tanggal_keluar = entry_tanggal_keluar.get_date()
        error_sound.play()
        result = messagebox.askyesno(title="Confirmation", message="Apakah anda yakin ingin menambahkan data ini?")
        if result:
                success_sound.play()
                pesan = f"Data dengan NIK {data_nik} berhasil ditambahkan"
                showinfo(title="Success",message=pesan)
                ft.add_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar)
                transition()
        else:
                pass

def show_menu():          
        """
        Menu Untuk Menampilkan Data
        """        
        click_sound.play()
        
        global top_frame, bottom_frame, label_menu, button_show_all, button_show_by_nik, button_exit
        
        top_frame.grid_forget()
        bottom_frame.grid_forget()

        label_menu = Label(root, text="Show Menu", bg='#4a9c46', font=("Helvetica", 20), height=2)
        label_menu.grid(row=0, column=0, padx=10, pady=5)

        top_frame = Frame(root, width=1175, height=500, bg='grey')
        top_frame.grid(row=1, column=0, padx=50, pady=50)

        button_show_all = Button(top_frame, text="Show All", width=30, height=3, command=show_get_length_all)
        button_show_all.grid(row=0, column=0, padx=480, pady=50)

        button_show_by_nik = Button(top_frame, text="Show By NIK", width=30, height=3, command=show_get_length_nik)
        button_show_by_nik.grid(row=1, column=0, padx=480, pady=50)

        button_exit = Button(top_frame, text="Exit", width=30, height=3, command=transition)
        button_exit.grid(row=2, column=0, padx=480, pady=50)

def show_get_length_all():   
        """
        Fungsi Untuk Mendapatkan Data Yang Dimasukkan saat Menampilkan Data
        """        
        global label_menu             
        ft.show_validate()
        if ft.show_validate() == False:
                error_sound.play()
                pesan = "Data masih kosong silahkan tambah data terlebih dahulu"
                showinfo(title="Warning",message=pesan)
                pass
        else:
                click_sound.play()
                button_show_all.grid_forget()
                button_show_by_nik.grid_forget()
                button_exit.grid_forget()
                show_all()

def show_all():   
        """
        Menu Untuk Menampilkan Semua Data
        """                      
        global top_frame

        button_exit = Button(top_frame, text="Exit", width=30, height=3, command=show_menu)
        button_exit.grid(row=2, column=0, padx=480, pady=50)

        tree_frame = Frame(top_frame, width=1100, height=500, bg='grey')
        tree_frame.grid(row=0, column=0, padx=10, pady=50)  

        tree_scroll_y = Scrollbar(tree_frame)
        tree_scroll_y.pack(side=RIGHT, fill=Y)

        tree_scroll_x = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_x.pack(side=BOTTOM, fill=X)

        my_tree = ttk.Treeview(tree_frame)
        my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        my_tree.configure(yscrollcommand=tree_scroll_y.set)
        tree_scroll_y.configure(command=my_tree.yview)

        my_tree.configure(xscrollcommand=tree_scroll_x.set)
        tree_scroll_x.configure(command=my_tree.xview)

        my_tree['columns'] = ('NIK', 'Name', 'Car', 'DateIn', 'DateOut', 'Price', 'Status')

        my_tree.heading('#0', text='No')
        my_tree.column('#0', width=50)
        my_tree.heading('NIK', text='NIK', command=lambda: sort_data(my_tree, 'NIK', False))
        my_tree.column('NIK', width=150)
        my_tree.heading('Name', text='Name', command=lambda: sort_data(my_tree, 'Name', False))
        my_tree.column('Name', width=150)
        my_tree.heading('Car', text='Car', command=lambda: sort_data(my_tree, 'Car', False))
        my_tree.column('Car', width=150)
        my_tree.heading('DateIn', text='Date In', command=lambda: sort_data(my_tree, 'DateIn', False))
        my_tree.column('DateIn', width=150)
        my_tree.heading('DateOut', text='Date Out', command=lambda: sort_data(my_tree, 'DateOut', False))
        my_tree.column('DateOut', width=150)
        my_tree.heading('Price', text='Harga (Rupiah)', command=lambda: sort_data(my_tree, 'Price', False))
        my_tree.column('Price', width=150)
        my_tree.heading('Status', text='Status', command=lambda: sort_data(my_tree, 'Status', False))
        my_tree.column('Status', width=100)

        ft.show_full_data(my_tree)

def show_get_length_nik():
        """
        Fungsi Untuk Validasi Jumlah Data
        """        
        global button_exit, entry_nik, button_validate, top_frame, label_menu

        ft.show_validate()
        if ft.show_validate() == False:
                error_sound.play()
                pesan = "Data masih kosong silahkan tambah data terlebih dahulu"
                showinfo(title="Warning",message=pesan)
                pass
        else:
                nik_type_menu()
                button_exit = Button(top_frame, text="Exit", width=10, height=1, command=show_menu)
                button_exit.grid(row=0, column=3, padx=40, pady=10)
                button_validate = Button(top_frame, text="Validate", width=10, height=1, command=show_get_entry_nik)
                button_validate.grid(row=0, column=2, padx=30, pady=10)
                
def show_get_entry_nik():
        """
        Fungsi Untuk Mendapatkan NIK Yang Dimasukkan saat Menampilkan Data
        """        
        global entry_nik, data_nik, label_menu, button_exit
        data_nik = entry_nik.get()
        if len(data_nik) != 10:
                error_sound.play()
                pesan = "NIK harus 10 digit"
                showinfo(title="Warning",message=pesan)
        else:
                ft.nik_validate(data_nik)       
                if ft.nik_validate(data_nik) == False:
                        error_sound.play()
                        pesan = f"Data dengan NIK {data_nik} belum ada silahkan tambah data nik-nya terlebih dahulu"
                        showinfo(title="Warning",message=pesan)
                else:
                        success_sound.play()
                        pesan = f"Data dengan NIK {data_nik} ada inilah hasilnya"
                        showinfo(title="Success",message=pesan)
                        button_exit.grid_forget()
                        show_by_nik()

def show_by_nik():
        """
        Menu Untuk Menampilkan Data Berdasarkan NIK
        """        
        global top_frame, data_nik, button_exit, entry_nik, button_validate, label_menu

        button_exit.grid_forget()
        entry_nik.grid_forget()
        button_validate.grid_forget()

        button_exit = Button(top_frame, text="Exit", width=30, height=3, command=show_menu)
        button_exit.grid(row=4, column=0, padx=480, pady=20)

        tree_frame = Frame(top_frame, width=1100, height=500, bg='grey')
        tree_frame.grid(row=0, column=0, padx=10, pady=50)  

        tree_scroll_y = Scrollbar(tree_frame)
        tree_scroll_y.pack(side=RIGHT, fill=Y)

        tree_scroll_x = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_x.pack(side=BOTTOM, fill=X)

        my_tree = ttk.Treeview(tree_frame)
        my_tree.pack(side=LEFT, fill=BOTH, expand=True)

        my_tree.configure(yscrollcommand=tree_scroll_y.set)
        tree_scroll_y.configure(command=my_tree.yview)

        my_tree.configure(xscrollcommand=tree_scroll_x.set)
        tree_scroll_x.configure(command=my_tree.xview)

        my_tree['columns'] = ('NIK', 'Name', 'Car', 'DateIn', 'DateOut', 'Price', 'Status')

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

        ft.show_by_nik(my_tree,data_nik)

def edit_menu():       
        """
        Menu Untuk Mengedit Data
        """        
        global label_menu, button_validate, entry_nik, entry_mobile, entry_name, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar, button_exit
        nik_type_menu()

        label_menu = Label(root, text=" Edit Menu ", bg='#4a9c46', font=("Helvetica", 20), height=2)
        label_menu.grid(row=0, column=0, padx=20, pady=5)

        button_validate = Button(top_frame, text="Validate", width=10, height=1, command=edit_get_entry_nik)
        button_validate.grid(row=0, column=2, padx=10, pady=10)

        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=40, pady=10)

def edit_get_entry_nik():
        """
        Fungsi Untuk Mendapatkan NIK Yang Dimasukkan saat Mengedit Data
        """        
        global entry_nik, data_nik, button_validate, label_menu
        data_nik = entry_nik.get()
        if len(data_nik) != 10:
                error_sound.play()
                pesan = "NIK harus 10 digit"
                showinfo(title="Warning",message=pesan)
        else:
                ft.nik_validate(data_nik)       
                if ft.nik_validate(data_nik) == False:
                        error_sound.play()
                        pesan = f"Data dengan NIK {data_nik} belum ada silahkan tambah data nik-nya terlebih dahulu"
                        showinfo(title="Warning",message=pesan)
                else:
                        success_sound.play()
                        pesan = f"Data dengan NIK {data_nik} ada inilah hasilnya"
                        showinfo(title="Success",message=pesan)
                        edit_by_nik()

def edit_by_nik():
        """
        Menu Untuk Konfirmasi Edit Data Berdasarkan NIK
        """
        global top_frame, bottom_frame, data_nik, button_exit, entry_nik, button_validate, label_menu
        label_menu.grid_forget()
        show_by_nik()
        button_exit.grid_forget()

        edit_label = Label(top_frame, text="Apakah anda yakin ingin mengedit data ini?", bg='grey', width=50, font=("Helvetica", 20))
        edit_label.grid(row=2, column=0, padx=10, pady=10)
        edit_button = Button(top_frame, text="Yes", width=30, height=3, command=edit_identity)
        edit_button.grid(row=3, column=0, padx=480, pady=20)
        button_exit = Button(top_frame, text="No", width=30, height=3, command=edit_menu)
        button_exit.grid(row=4, column=0, padx=480, pady=20)

def edit_identity():
        """
        Menu Untuk Mengedit Identitas Data
        """
        global data_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        input_identity(data_nik)

        all_data = ft.edit_get_data(data_nik)

        data_nama = all_data[1]
        data_mobil = all_data[2]
        data_tanggal_masuk = all_data[3]
        data_tanggal_keluar = all_data[4]
        data_harga = all_data[5]
        data_status = all_data[6]

        nama_value = StringVar(value=data_nama)
        entry_nama = Entry(top_frame, width=52, textvariable=nama_value)
        entry_nama.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_nama.grid(row=1, column=1, padx=40, pady=10)

        mobil_value = StringVar(value=data_mobil)
        entry_mobil = Entry(top_frame, width=52, textvariable=mobil_value)
        entry_mobil.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_mobil.grid(row=2, column=1, padx=40, pady=10)

        validate_price = (top_frame.register(validate_digit), '%P')
        harga_value = StringVar(value=data_harga)
        entry_harga = Entry(top_frame, width=52, textvariable=harga_value, validate="key", validatecommand=validate_price)
        entry_harga.config(font=("Arial", 14), bg="white", fg="black", bd=2, relief="groove")
        entry_harga.grid(row=3, column=1, padx=40, pady=10)

        date_obj_masuk = datetime.strptime(data_tanggal_masuk, '%Y-%m-%d')
        formatted_date_masuk = date_obj_masuk.strftime('%d/%m/%Y')
        entry_tanggal_masuk = DateEntry(top_frame, width=50, background='darkblue', foreground='white', borderwidth=2)
        entry_tanggal_masuk.config(font=("Arial", 14))
        entry_tanggal_masuk.grid(row=4, column=1, padx=40, pady=10)
        entry_tanggal_masuk.set_date(formatted_date_masuk)

        date_obj_keluar = datetime.strptime(data_tanggal_keluar, '%Y-%m-%d')
        formatted_date_keluar = date_obj_keluar.strftime('%d/%m/%Y')
        entry_tanggal_keluar = DateEntry(top_frame, width=50, background='darkblue', foreground='white', borderwidth=2)
        entry_tanggal_keluar.config(font=("Arial", 14))
        entry_tanggal_keluar.grid(row=5, column=1, padx=40, pady=10)
        entry_tanggal_keluar.set_date(formatted_date_keluar)

        entry_status = tkinter.StringVar(value=data_status)
        options = ["Progress", "Selesai"]
        entry_status_options = tkinter.OptionMenu(top_frame, entry_status, "", *options)
        entry_status_options.configure(font=("Arial", 14), background="white", foreground="black", borderwidth=2, relief="groove", width=48)
        entry_status_options.grid(row=6, column=1, padx=40, pady=10)

        button_edit = Button(top_frame, text="Save", width=30, height=3, command=edit_get_entry_data)
        button_edit.grid(row=7, column=0, padx=10, pady=30)  

        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=edit_menu)
        button_exit.grid(row=0, column=2, padx=30, pady=10)

def edit_get_entry_data():
        """
        Fungsi Untuk Mendapatkan Data Yang Dimasukkan saat Mengedit Data + konfirmasi
        """
        global entry_nik, entry_nama, entry_mobil, entry_harga, entry_tanggal_masuk, entry_status, entry_tanggal_keluar
        error_sound.play()
        data_nik = entry_nik.get()
        data_nama = entry_nama.get()
        data_mobil = entry_mobil.get()
        data_harga = entry_harga.get()
        data_tanggal_masuk = entry_tanggal_masuk.get_date()
        data_status = entry_status.get()
        data_tanggal_keluar = entry_tanggal_keluar.get_date()
        result = messagebox.askyesno(title="Confirmation", message="Apakah anda yakin ingin mengedit data ini?")
        if result:
                success_sound.play()
                pesan = f"Data dengan NIK {data_nik} berhasil diedit"
                showinfo(title="Success",message=pesan)
                ft.edit_data(data_nik, data_nama, data_mobil, data_harga, data_tanggal_masuk, data_status, data_tanggal_keluar)
                edit_menu()
        else:
                pass

def delete_menu():     
        """
        Menu Untuk Menghapus Data
        """
        global label_menu, button_validate                       
        nik_type_menu()

        label_menu = Label(root, text=" Delete Menu ", bg='#4a9c46', font=("Helvetica", 20), height=2)
        label_menu.grid(row=0, column=0, padx=20, pady=5)

        button_validate = Button(top_frame, text="Validate", width=10, height=1, command=delete_get_entry_nik)
        button_validate.grid(row=0, column=2, padx=10, pady=10)

        button_exit = Button(top_frame, text="Exit", width=10, height=1, command=transition)
        button_exit.grid(row=0, column=3, padx=40, pady=10)

def delete_get_entry_nik():
        """
        Fungsi Untuk Mendapatkan NIK Yang Dimasukkan saat Menghapus Data
        """
        global entry_nik, data_nik, button_validate, label_menu
        data_nik = entry_nik.get()
        if len(data_nik) != 10:
                error_sound.play()
                pesan = "NIK harus 10 digit"
                showinfo(title="Warning",message=pesan)
        else:
                ft.nik_validate(data_nik)       
                if ft.nik_validate(data_nik) == False:
                        error_sound.play()
                        pesan = f"Data dengan NIK {data_nik} tidak ditemukan harap input nik yang lainnya"
                        showinfo(title="Warning",message=pesan)
                else:
                        success_sound.play()
                        pesan = f"Data dengan NIK {data_nik} ada inilah hasilnya"
                        showinfo(title="Success",message=pesan)
                        delete_by_nik()

def delete_by_nik():
        """
        Menu Untuk Konfirmasi Hapus Data Berdasarkan NIK
        """
        global top_frame, bottom_frame, entry_nik, button_exit, button_validate, label_menu
        label_menu.grid_forget()
        show_by_nik()
        button_exit.grid_forget()

        delete_label = Label(top_frame, text="Apakah anda yakin ingin menghapus data ini?", bg='grey', width=50, font=("Helvetica", 20))
        delete_label.grid(row=2, column=0, padx=10, pady=10)
        delete_button = Button(top_frame, text="Yes", width=30, height=3, command=delete_get_entry_data)
        delete_button.grid(row=3, column=0, padx=480, pady=20)
        button_exit = Button(top_frame, text="No", width=30, height=3, command=delete_menu)
        button_exit.grid(row=4, column=0, padx=480, pady=20)

def delete_get_entry_data():
        """
        Fungsi Untuk Mendapatkan Data Yang Dimasukkan saat Menghapus Data + konfirmasi
        """
        ft.delete_data(data_nik)
        success_sound.play()
        pesan = f"Data dengan NIK {data_nik} berhasil dihapus"
        showinfo(title="Success",message=pesan)
        delete_menu()

def exit_menu():                    
        root.destroy()

if __name__ == '__main__':
        # create a windows
        root = tkinter.Tk()
        # config icon windows
        root.iconbitmap("../RentACar/assets/images/favicon.ico")
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
        root.configure(bg="#4a9c46")

        # Action Code
        main_menu()

        # make a windows loop
        root.mainloop()