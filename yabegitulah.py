from prettytable import PrettyTable
import json
import pwinput

def menu_utama():
    table = PrettyTable()
    table.title = "SELAMAT DATANG DI KELAS BIMBEL ONLINE TAHUTEK"
    table.field_names = ["No", "Menu"]

    pilihan_menu = [
        ["1", "Login"],
        ["2", "Buat Akun"],
        ["3", "Keluar"]
    ]

    for option in pilihan_menu:
        table.add_row(option)
    
    print(table)
    
    while True:
        try:
            choice = int(input("Pilin menu yang ingin digunakan (1/2/3) = "))
            if choice == 1:
                print("Anda memilih Login.")
                # Tambahkan kode untuk login di sini
                break
            elif choice == 2:
                print("Anda memilih Buat Akun.")
                # Tambahkan kode untuk membuat akun di sini
                break
            elif choice == 3:
                print("Anda memilih Keluar.")
                # Tambahkan kode untuk keluar di sini
                break
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Mohon isi nomor yang benar!")

def menu_admin():

def admin_liat():

def admin_tambah():

def admin_baruin():

def admin_hapus():

def menu_pelajar():

def pelajar_liat():

def pelajar_beli():

def pelajar_isi():

def menu_regis():

def menu_login():

menu_utama()