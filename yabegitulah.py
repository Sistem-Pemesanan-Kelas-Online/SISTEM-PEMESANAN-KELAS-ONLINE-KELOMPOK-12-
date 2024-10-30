from prettytable import PrettyTable
import json
import sys
import pwinput
import os
os.system("cls")

json_path = "D:\STUFF\Visual Code\Python\PA DDP\storage.json"
with open(json_path, "r") as jsonstorage:   
    data = json.loads(jsonstorage.read())

def simpan():
    json_path = "D:\STUFF\Visual Code\Python\PA DDP\storage.json"
    with open(json_path, "w") as jsonstorage:
        json.dump(data, jsonstorage, indent=4)

def menu_utama():
    os.system("cls")
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
            elif choice == 2:
                print("Anda memilih Buat Akun.")
                
            elif choice == 3:
                print("Anda memilih Keluar.")
                
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Program dihentikan.")
            exit()

def masuk_admin():
    os.system("cls")
    print("Masukkan Email dan PIN")
    
    percobaan_login = 3

    try:
        for i in range(percobaan_login):
            input_username = input("Username : ")
            if input_username == data.get("AdminKelas", {}).get("Username"):
                input_pin = pwinput.pwinput(prompt="Pin : ")
                if input_pin == data.get("AdminKelas", {}).get("PIN"):
                    menu_admin()
                    return  
                else:
                    print("PIN Tidak Valid!")
            else:
                print("Username anda salah!")

            if i == percobaan_login - 1:
                print("Anda telah menggunakan kesempatan yang ada, silakan kembali ke Program")
                menu_utama()  
                return  
    except KeyboardInterrupt:
        print("Program dihentikan.")
        exit()
    except ValueError:
        print("Masukkan data yang benar!")

def menu_admin():
    os.system("cls")
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

    for option in pilihan_menu:
        table.add_row(option)

    while True:
        print(table)
    
        try:
            choice = int(input("Pilih menu yang ingin digunakan (1/2/3/4/5/6) = "))
            if choice == 1:
                tambah_kelas()
                
            elif choice == 2:
                print("Menghapus Kelas...")
                
            elif choice == 3:
                daftar_kelas() 
                
            elif choice == 4:
                print("Memperbarui Kelas...")
                
            elif choice == 5:
                print("Kembali ke menu utama.")
                break  
            elif choice == 6:
                print("Keluar dari program.")
                exit()  
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Program dihentikan.")
            exit()

def daftar_kelas():
    os.system("cls")
    tabel = PrettyTable()
    tabel.title = "DAFTAR KELAS"
    tabel.field_names = ["Kode", "Mata Kuliah", "Jadwal", "Harga/Sesi", "Status"]

    if "Kelas" in data:
        for detail in data["Kelas"]:
            tabel.add_row([
                detail.get("Kode"),
                detail.get("Mata_Kuliah"),
                detail.get("Jadwal"),
                detail.get("Harga/Sesi"),
                detail.get("Status")
            ])
    print(tabel)

def tambah_kelas():
    os.system("cls")
    print("Menambah Kelas Baru")
    
    while True:
        kode = input("Masukkan Kode Kelas (harus diawali dengan 'KLS'): ")
        if not kode.startswith("KLS"):
            print("Kode kelas harus diawali dengan 'KLS'. Silakan coba lagi.")
            continue
        break

    mata_kuliah = input("Masukkan Nama Mata Kuliah: ")

    jadwal = ""
    jadwal_ada = set(kelas["Jadwal"] for kelas in data.get("Kelas", []))  # Set untuk menyimpan jadwal yang sudah ada
    while True:
        jadwal = input("Masukkan Jadwal (contoh: Senin 10:00 - 12:00): ")
        
        if jadwal in jadwal_ada:
            print("Jadwal sudah ada. Silakan masukkan jadwal yang berbeda.")
        else:
            jadwal_ada.add(jadwal)  
            break 

    harga = input("Masukkan Harga/Sesi: ")

    kelas_baru = {
        "Kode": kode,
        "Mata_Kuliah": mata_kuliah,
        "Jadwal": jadwal,
        "Harga/Sesi": harga,
        "Status": "Kosong"  
    }

    if "Kelas" not in data:
        data["Kelas"] = []  
    data["Kelas"].append(kelas_baru)


    simpan()

    print("Kelas baru berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu admin...")



#def admin_baruin():

#def admin_hapus():

#def menu_pelajar():

#def pelajar_liat():

#def pelajar_beli():

#def pelajar_isi():

#def menu_regis():

#def menu_login():

menu_utama()
