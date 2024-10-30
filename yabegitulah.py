from prettytable import PrettyTable
import json
import pwinput
import os
os.system("cls")

tabel_data = PrettyTable()
tabel_data.field_names = ["No","Kode", "Mata Kulih", "Jadwal", "Harga/Sesi", "Status"]

jsonkelas = open("D:\STUFF\Visual Code\Python\PA DDP\kelas.json")
data = json.loads(jsonkelas.read())

def simpan():
    with open("kelas.json", "w") as sn:
        json.dump(data, sn, indent=4)

def menu_utama():
    table = PrettyTable()
    table.title = "SELAMAT DATANG DI KELAS BIMBEL ONLINE TAHUTEK"
    table.field_names = ["No", "Menu"]

    pilihan_menu = [
        ["1", "Login sebagai Admin"],
        ["2", "Login sebagai Member"],
        ["3", "Keluar"]
    ]

    for option in pilihan_menu:
        table.add_row(option)
    
    print(table)
    
    while True:
        try:
            choice = int(input("Pilin menu yang ingin digunakan (1/2/3) = "))
            if choice == 1:
                masuk_admin()
                print("Masuk ke menu Admin")

            elif choice == 2:
                print("Anda memilih Buat Akun.")
                
            elif choice == 3:
                print("Anda memilih Keluar.")
                
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Mohon isi nomor yang benar!")

def masuk_admin():
    while True:
        try:
            email = str(input("Email : "))
            pw = pwinput.pwinput("Password : ")
            if email == "adminganteng@gmail.com" and pw == "admin111":
                print("     --- LOGIN BERHASIL ---     ")
                return menu_admin()
            else:
                print("Email atau Password salah, mohon coba lagi")
                return masuk_admin()
        except ValueError:
            print("Mohon isi dengan benar")
        except KeyboardInterrupt:
            print("Mohon isi dengan benar")
            

def menu_admin():
    table = PrettyTable()
    table.title = "SELAMAT DATANG ADMIN"
    table.field_names = ["No", "Menu"]

    pilihan_menu = [
        ["1", "Menambah Kelas"],
        ["2", "Menghapus Kelas"],
        ["3", "Melihat Kelas"],
        ["4", "Memperbarui Kelas"],
        ["5", "Kembali"],
        ["6", "Keluar"]
    ]

    while True:
        for option in pilihan_menu:
            table.add_row(option)
        
        print(table)
    
        try:
            choice = int(input("Pilih menu yang ingin digunakan (1/2/3/4/5/6) = "))
            if choice == 1:
                print("Menambah Kelas...")
                # Tambahkan logika untuk menambah kelas di sini
            elif choice == 2:
                print("Menghapus Kelas...")
                # Tambahkan logika untuk menghapus kelas di sini
            elif choice == 3:
                return admin_liat()
                # Tambahkan logika untuk melihat kelas di sini
            elif choice == 4:
                print("Memperbarui Kelas...")
                # Tambahkan logika untuk memperbarui kelas di sini
            elif choice == 5:
                print("Kembali ke menu utama.")
                break  # Kembali ke menu utama
            elif choice == 6:
                print("Keluar dari program.")
                exit()  # Keluar dari program
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            break

def admin_liat():
    
    print(tabel_data)

#def admin_tambah():

#def admin_baruin():

#def admin_hapus():

#def menu_pelajar():

#def pelajar_liat():

#def pelajar_beli():

#def pelajar_isi():

#def menu_regis():

#def menu_login():

menu_utama()
