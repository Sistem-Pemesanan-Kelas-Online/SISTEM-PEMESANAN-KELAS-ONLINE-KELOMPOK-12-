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
                menuawal_pelajar()
                
            elif choice == 3:
                print("Keluar program")
                exit()
            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Program dihentikan.")
            exit()

def masuk_admin():
    os.system("cls")
    print("=== Login Admin ===")
    print("Masukkan Username dan PIN")
    
    percobaan_login = 3
    try:
        for i in range(percobaan_login):
            input_username = input("Username : ")
            if input_username == data.get("AdminKelas", {}).get("Username"):
                input_pin = pwinput.pwinput(pinpass="Pin : ")
                if input_pin == data.get("AdminKelas", {}).get("PIN"):
                    menu_admin()
                    return  
                else:
                    print("PIN salah")
            else:
                print("Username salah")
            if i == percobaan_login - 1:
                print("Anda salah memasukkan lebih dari 3 kali, kembali ke menu awal")
                menu_utama()  
                return  
    except KeyboardInterrupt:
        print("Program dihentikan.")
        exit()

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
                menu_utama()  
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
    
    try:
        kodelama = set(kelas["Kode"] for kelas in data.get("Kelas",[]))
        while True:
            kode = input("Masukkan Kode Kelas (harus diawali dengan 'KLS'): ")
            if not kode.startswith("KLS"):
                print("Kode kelas harus diawali dengan 'KLS'. Silakan coba lagi.")
                continue
            
            if not kode[3:].isdigit():
                print("Setelah 'KLS' harus diikuti dengan angka. Silakan coba lagi.")
                continue

            if kode in kodelama:
                print("Kode sudah ada, mohon masukkan yang baru")
            else:
                kodelama.add(kode)
                break
        
        matkul = set(kelas["Mata_Kuliah"] for kelas in data.get("Kelas",[]))
        while True:
            mata_kuliah = str(input("Masukkan nama mata kuliah : "))

            if any(char.isdigit() for char in mata_kuliah):
                print("Mata kuliah tidak boleh mengandung angka. Silakan coba lagi.")
                continue
            if not mata_kuliah.strip():
                print("Mata kuliah tidak boleh kosong")
                continue
            if mata_kuliah in matkul:
                print("Mata kuliah sudah ada. Silahkan masukkan mata kuliah yang baru")
            else:
                matkul.add(mata_kuliah)
                break

        jadwal_ada = set(kelas["Jadwal"] for kelas in data.get("Kelas", []))
        while True:
            jadwal = input("Masukkan Jadwal (contoh: Senin 10:00-12:00): ")
            jadwal = jadwal.replace(" - ", "-").replace(" -", "-").replace("- ", "-")

            try:
                hari, waktu = jadwal.split(" ")
                jam_mulai, jam_selesai = waktu.split("-")
                
                hari_valid = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
                if hari not in hari_valid:
                    raise ValueError("Hari tidak valid")
                
                if len(jam_mulai) != 5 or len(jam_selesai) != 5:
                    raise ValueError("Format waktu harus HH:MM")
                
                jam_mulai_split = jam_mulai.split(":")
                jam_selesai_split = jam_selesai.split(":")
                
                if not (0 <= int(jam_mulai_split[0]) <= 23 and 0 <= int(jam_mulai_split[1]) <= 59 and
                    0 <= int(jam_selesai_split[0]) <= 23 and 0 <= int(jam_selesai_split[1]) <= 59):
                    raise ValueError("Jam atau menit tidak valid")
                
                if jadwal in jadwal_ada:
                    print("Jadwal sudah ada. Silakan masukkan jadwal yang berbeda.")
                else:
                    jadwal_ada.add(jadwal)
                    break
                    
            except ValueError:
                print(f"Format jadwal tidak valid")
                print("Gunakan format: Hari HH:MM-HH:MM (contoh: Senin 17:00-18:00)")
                continue
            
        try:
            harga = int(input("Masukkan Harga/Sesi: "))
        except ValueError:
            print("Masukkan harga yang valid")
        

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
    except ValueError:
            print("Mohon isi sesuai perintah")
    except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            exit()

def menuawal_pelajar():
    os.system("cls")
    table = PrettyTable()
    table.title = "MENU PELAJAR"
    table.field_names = ["No", "Menu"]
    pilihan_menu = [
        ["1", "Login"],
        ["2", "Registrasi Akun"],
        ["3", "Kembali"],
        ["4", "Keluar"]
    ]
    for option in pilihan_menu:
        table.add_row(option)
    
    print(table)

    while True:
        try:
            choice = int(input("Pilin menu yang ingin digunakan (1/2/3/4) = "))
            if choice == 1:
                masuk_pelajar()

            elif choice == 2:
                regis()
                
            elif choice == 3:
                menu_utama()

            elif choice == 4:
                print("Keluar program")
                exit()

            else:
                print("Nomor tidak valid, silahkan pilih nomor sesuai perintah!")
        except ValueError:
            print("Mohon isi nomor yang benar!")
        except KeyboardInterrupt:
            print("Program dihentikan.")
            exit()

def regis():
    os.system("cls")
    print("=== Registrasi Akun Pelajar ===")

    namalama = set(kelas["Nama"] for kelas in data.get("User",[]))
    while True:
        nama = str(input("Masukkan Nama: "))
        if not nama.strip():
            print("Nama tidak boleh kosong")
            continue
        
        if nama in namalama:
            print("Nama sudah terdaftar")
        else:
            namalama.add(nama)
            break

    userlama = set(kelas["Username"] for kelas in data.get("User",[]))
    while True:
        user = str(input("Masukkan username : "))
        if not user.strip():
            print("Username tidak boleh kosong")
            continue
        
        if user in userlama:
            print("Username sudah terdaftar")
        else:
            userlama.add(user)
            break

    pin = set(kelas["Pin"] for kelas in data.get("User",[]))
    while True:    
        try:
            buatpw = int(pwinput.pwinput("Buat PIN : "))
        except ValueError:
            print("Mohon buat PIN dengan benar")
            continue
        pin.add(buatpw)
        break

    while True:
        saldo = input("Masukkan saldo (minimal 0): ")
        if saldo.isdigit():
            break
        print("Saldo harus berupa angka. Silakan coba lagi.")

    # Menambahkan data baru ke dalam daftar "User" yang ada
    pelajar_baru = {
        "Nama": nama,
        "Username": user,
        "Pin": buatpw,
        "Saldo": saldo  # Simpan sebagai string untuk konsistensi
    }
    if "User" not in data:
        data["User"] = []  # Jika belum ada "User", buat daftar baru
    data["User"].append(pelajar_baru)  # Tambahkan data baru

    # Simpan data ke file JSON
    simpan()
    print("Pelajar baru berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu awal pelajar...")
    menuawal_pelajar()


#def masuk_pelajar():

#def admin_baruin():

#def admin_hapus():

#def menu_pelajar():

#def pelajar_liat():

#def pelajar_beli():

#def pelajar_isi():

#def menu_regis():

#def menu_login():

menu_utama()
