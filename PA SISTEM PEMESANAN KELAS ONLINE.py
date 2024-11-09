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
        ["2", "Login sebagai Pelajar"],
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
                print("Nomor tidak valid, masukkan nomor yang benar")
        except ValueError:
            print("Mohon isi dengan angka")
        except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK 'CTRL + C' PAHAM")
            menu_utama()
            return

def masuk_admin():
    os.system("cls")
    print("=== Login Admin ===")
    print("Masukkan Username dan PIN")
    
    percobaan_login = 3
    try:
        for i in range(percobaan_login):
            input_username = input("Username : ")
            if input_username == data.get("AdminKelas", {}).get("Username"):
                input_pin = pwinput.pwinput("Pin : ")
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
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        masuk_admin()
        return

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
                hapus_kelas()
                
            elif choice == 3:
                daftar_kelas() 
                
            elif choice == 4:
                barui_kelas()
                
            elif choice == 5:
                menu_utama()  
            elif choice == 6:
                print("Keluar dari program")
                exit()  
            else:
                print("Nomor tidak valid, masukkan nomor yang benar")
        except ValueError:
            print("Mohon isi dengan angka")
        except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
            menu_admin()
            return

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
    
    try:
        kodelama = set(kelas["Kode"] for kelas in data.get("Kelas",[]))
        while True:
            
            kode = input("Masukkan kode kelas (harus diawali dengan 'KLS' atau ketik 'batal' untuk kembali) = ")
            if kode.lower() == 'batal' and 'Batal':
                print("Tambah kelas dibatalkan")
                menu_admin()
                return
            if not kode.startswith("KLS"):
                print("Kode kelas harus diawali dengan 'KLS'")
                continue
            
            if not kode[3:].isdigit():
                print("Setelah 'KLS' harus angka")
                continue
                
            if kode in kodelama:
                print("Kode sudah ada, masukkan yang baru")
            else:
                kodelama.add(kode)
                break
        
        matkul = set(kelas["Mata_Kuliah"] for kelas in data.get("Kelas",[]))
        while True:
            mata_kuliah = str(input("Masukkan nama mata kuliah = "))

            if any(char.isdigit() for char in mata_kuliah):
                print("Mata kuliah tidak boleh ada angka")
                continue
            if not mata_kuliah.strip():
                print("Mata kuliah tidak boleh kosong")
                continue
            if mata_kuliah in matkul:
                print("Mata kuliah sudah ada, masukkan mata kuliah baru")
            else:
                matkul.add(mata_kuliah)
                break

        jadwal_ada = set(kelas["Jadwal"] for kelas in data.get("Kelas", []))
        while True:
            jadwal = input("Masukkan jadwal (contoh: Senin 10:00-12:00) = ")
            jadwal = jadwal.replace(" - ", "-").replace(" -", "-").replace("- ", "-")

            try:
                hari, waktu = jadwal.split(" ")
                jam_mulai, jam_selesai = waktu.split("-")
                
                hari_valid = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
                if hari not in hari_valid:
                    raise ValueError("Hari tidak valid")
                
                if len(jam_mulai) != 5 or len(jam_selesai) != 5:
                    raise ValueError("Format waktu tidak sesuai")
                
                if jadwal in jadwal_ada:
                    print("Jadwal sudah ada")
                else:
                    jadwal_ada.add(jadwal)
                    break
                    
            except ValueError:
                print(f"Format jadwal salah")
                print("Gunakan format yang sesuai (contoh: Senin 17:00-18:00)")
                continue
            
        while True:
            harga = input("Masukkan harga/sesi = ")
            if harga.isdigit():
                harga = int(harga)
                break
            else:
                print("Masukkan harga dengan angka")
        

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
        print("Kelas baru berhasil ditambah")
        input("Tekan tombol enter untuk kembali ke menu admin...")
    except ValueError:
            print("Mohon isi sesuai perintah")
    except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
            tambah_kelas()
            return

def hapus_kelas():
    os.system("cls")
    
    try:
        if not data.get("Kelas"):
            print("Tidak ada kelas untuk dihapus")
            input("Tekan tombol enter untuk kembali ke menu admin...")
            return

        while True:
            daftar_kelas() 
            
            kode_hapus = input("Masukkan kode kelas yang ingin dihapus (atau ketik 'batal' untuk kembali) = ")
            if kode_hapus.lower() == 'batal' and 'Batal':
                print("Penghapusan kelas dibatalkan")
                break

            kelas_ditemukan = False
            for kelas in data["Kelas"]:
                if kelas["Kode"] == kode_hapus:
                    kelas_ditemukan = True
                    konfirmasi = input(f"Yakin ingin menghapus kelas {kelas['Mata_Kuliah']} ({kode_hapus})? (y/n) = ")
                    if konfirmasi == 'y' and 'Y':
                        data["Kelas"].remove(kelas)
                        simpan()
                        print(f"Kelas dengan kode {kode_hapus} berhasil dihapus.")
                        input("Tekan tombol enter untuk kembali ke menu admin...")
                        return
                    elif konfirmasi == 'n' and 'N':
                        print("Penghapusan kelas dibatalkan.")
                        menu_admin()
                        return
                    else:
                        print("Jawaban tidak sesuai perintah, mohon ulang")
                        continue

            if not kelas_ditemukan:
                print(f"Kelas dengan kode {kode_hapus} tidak ditemukan")
                continue

        input("Tekan tombol enter untuk kembali ke menu admin...")
        menu_admin()
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        hapus_kelas()
        return

def barui_kelas():
    os.system("cls")
    
    try:
        if not data.get("Kelas"):
            print("Tidak ada kelas untuk diperbarui")
            input("Tekan tombol enter untuk kembali ke menu admin...")
            return

        while True:
            daftar_kelas() 
            
            kode_edit = input("Masukkan kode kelas yang ingin diperbarui (atau ketik 'batal' untuk kembali) = ")
            if kode_edit.lower() == 'batal' and 'Batal':
                print("Pengeditan kelas dibatalkan.")
                break

            kelas_ditemukan = False
            for kelas in data["Kelas"]:
                if kelas["Kode"] == kode_edit:
                    kelas_ditemukan = True
                    print(f"Anda sedang mengedit kelas: {kelas['Mata_Kuliah']} ({kode_edit})")
                    
                    while True:
                        mata_kuliah = input("Masukkan nama mata kuliah baru (tekan enter untuk melewati) = ")
                        if mata_kuliah.strip() == "":
                            mata_kuliah = kelas["Mata_Kuliah"]  
                            break
                        if any(char.isdigit() for char in mata_kuliah):
                            print("Mata kuliah tidak boleh ada angka")
                            continue
                        if mata_kuliah in set(k["Mata_Kuliah"] for k in data["Kelas"] if k["Kode"] != kode_edit):
                            print("Mata kuliah sudah ada")
                        else:
                            break
                    
                    while True:
                        jadwal = input("Masukkan jadwal baru (contoh: Senin 10:00-12:00) (tekan enter untuk melewati) = ")
                        if jadwal.strip() == "":
                            jadwal = kelas["Jadwal"] 
                            break
                        jadwal = jadwal.replace(" - ", "-").replace(" -", "-").replace("- ", "-")
                        try:
                            hari, waktu = jadwal.split(" ")
                            jam_mulai, jam_selesai = waktu.split("-")
                            
                            hari_valid = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
                            if hari not in hari_valid:
                                raise ValueError("Hari tidak valid")
                            
                            if len(jam_mulai) != 5 or len(jam_selesai) != 5:
                                raise ValueError("Format waktu tidak sesuai")
                            
                            if jadwal in set(k["Jadwal"] for k in data["Kelas"] if k["Kode"] != kode_edit):
                                print("Jadwal sudah ada")
                            else:
                                break
                            
                        except ValueError:
                            print(f"Format jadwal tidak valid")
                            print("Gunakan format yang sesuai (contoh: Senin 17:00-18:00)")
                            continue

                    while True:
                            harga = input("Masukkan harga/sesi baru (tekan enter untuk melewati) = ")
                            if harga.strip() == "":
                                harga = int(kelas["Harga/Sesi"]) 
                                break

                            elif harga.isdigit():
                                harga = int(harga)
                                break
                            
                            else:
                                print("Masukkan harga dengan benar")

                    while True:
                        status = input("Masukkan status baru (terisi/kosong), tekan enter untuk melewati): ")
                        if status.strip() == "":
                            status = kelas["Status"] 
                            break
                        if status not in ["Terisi", "Kosong"]:
                            print("Harap masukkan status (terisi/kosong)")
                            continue
                        break

                    kelas["Mata_Kuliah"] = mata_kuliah
                    kelas["Jadwal"] = jadwal
                    kelas["Harga/Sesi"] = harga
                    kelas["Status"] = status
                    
                    simpan()
                    print("Kelas berhasil diperbarui")
                    input("Tekan tombol enter untuk kembali ke menu admin...")
                    return

            if not kelas_ditemukan:
                print(f"Kelas dengan kode {kode_edit} tidak ditemukan")
                continue

        input("Tekan tombol enter untuk kembali ke menu admin...")
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        barui_kelas()
        return

def menuawal_pelajar():
    os.system("cls")
    
    table = PrettyTable()
    table.title = "LOGIN PELAJAR"
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
                print("Nomor tidak valid, masukkan nomor yang benar")
        except ValueError:
            print("Mohon isi dengan angka")
        except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
            menuawal_pelajar()
            return

def regis():
    os.system("cls")

    print("=== Registrasi Akun Pelajar ===")
    try:
        namalama = set(kelas["Nama"] for kelas in data.get("User",[]))
        while True:
            nama = str(input("Masukkan nama = "))
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
            user = str(input("Masukkan username = "))
            if not user.strip():
                print("Username tidak boleh kosong")
                continue
            
            if user in userlama:
                print("Username sudah terdaftar")
            else:
                userlama.add(user)
                break

        pin = set(kelas["Pin"] for kelas in data.get("User ", []))
        while True:    
            buatpw = pwinput.pwinput("Buat PIN (5 digit) = ")
            
            if len(buatpw) == 5 and buatpw.isdigit():
                if buatpw in pin:
                    print("PIN sudah terdaftar, buatlah PIN yang berbeda")
                else:
                    print("PIN berhasil dibuat")
                    pin.add(buatpw)
                    break
            else:
                print("PIN harus berjumlah 5 digit dan hanya terdiri dari angka")

        while True:
            saldo = input("Masukkan saldo pertama kali (minimal 0) = ")
            if saldo.isdigit():
                saldo = int(saldo)
                break
            print("Saldo harus berupa angka")

        pelajar_baru = {
            "Nama": nama,
            "Username": user,
            "Pin": buatpw,
            "Saldo": saldo
        }
        if "User" not in data:
            data["User"] = [] 
        data["User"].append(pelajar_baru) 

        simpan()
        print("Akun Pelajar berhasil ditambahkan")
        input("Tekan tombol enter untuk kembali ke menu awal pelajar...")
        menuawal_pelajar()
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        regis()
        return

def masuk_pelajar():
    os.system("cls")
    print("=== Login Pelajar ===")
    print("Masukkan Username dan PIN")

    percobaan_login = 3
    try:
        for i in range(percobaan_login):
            input_username = input("Username = ")
            input_pin = pwinput.pwinput("Pin = ")

            for user in data["User"]:
                if input_username == user["Username"] and input_pin == str(user["Pin"]):
                    global pengguna
                    pengguna = user
                    print("Login berhasil")
                    menu_pelajar()  
                    return

            print("Username atau PIN salah")
            
            if i == percobaan_login - 1:
                print("Salah memasukkan lebih dari 3 kali, kembali ke menu awal")
                menu_utama() 
                return
            
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        masuk_pelajar()
        return

def menu_pelajar():
    os.system("cls")
    table = PrettyTable()
    table.title = f"SELAMAT DATANG {pengguna['Nama'].upper()}"
    table.field_names = ["No", "Menu"]
    pilihan_menu = [
        ["1", "Daftar Kelas"],
        ["2", "Beli Kelas"],
        ["3", "Cek Saldo"],
        ["4", "Isi Saldo"],
        ["5", "Cek Kelas"],
        ["6", "Kembali"],
        ["7", "Keluar"]
    ]

    for option in pilihan_menu:
        table.add_row(option)
    while True:
        print(table)

        try:
            choice = int(input("Pilih menu yang ingin digunakan (1/2/3/4/5/6) = "))
            if choice == 1:
                daftar_kelas()
                
            elif choice == 2:
                beli_kelas()
                
            elif choice == 3:
                cek_saldo()

            elif choice == 4:
                isi_saldo()
                
            elif choice == 5:
                cek_kelas()
                
            elif choice == 6:
                menu_utama()  
            elif choice == 7:
                print("Keluar dari program")
                exit()  
            else:
                print("Nomor tidak valid, masukkan nomor yang benar")
        except ValueError:
            print("Mohon isi dengan angka")
        except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
            menu_pelajar()
            return

def beli_kelas():
    os.system("cls")

    try:
        if not data.get("Kelas"):
            print("Tidak ada kelas untuk dibeli")
            input("Tekan tombol enter untuk kembali ke menu pelajar...")
            return

        daftar_kelas()

        while True:
            kode_beli = input("Masukkan kode kelas yang ingin dibeli (atau ketik 'batal' untuk kembali) = ")
            if kode_beli.lower() == 'batal' and 'Batal':
                print("Pembelian kelas dibatalkan")
                break

            kelas_ditemukan = False
            for kelas in data["Kelas"]:
                if kelas["Kode"] == kode_beli:
                    kelas_ditemukan = True
                    if kelas["Status"] == "Terisi":
                        print(f"Kelas dengan kode {kode_beli} sudah terisi")
                        break

                    if int(pengguna["Saldo"]) >= kelas["Harga/Sesi"]:
                        pengguna["Saldo"] = int(pengguna["Saldo"]) - kelas["Harga/Sesi"]
                        
                        info_kelas = {
                            "Kode": kelas["Kode"],
                            "Mata_Kuliah": kelas["Mata_Kuliah"],
                            "Jadwal": kelas["Jadwal"]
                        }
                        
                        if "Kelas" not in pengguna:
                            pengguna["Kelas"] = []
                        pengguna["Kelas"].append(info_kelas)
                        kelas["Status"] = "Terisi"
                        simpan()

                        invoice = PrettyTable()
                        invoice.title = "INVOICE PEMBELIAN KELAS"
                        invoice.field_names = ["Detail", "Informasi"]
                        invoice.add_row(["Nama Pembeli", pengguna["Nama"]])
                        invoice.add_row(["Nama Kelas", kelas["Mata_Kuliah"]])
                        invoice.add_row(["Kode Kelas", kelas["Kode"]])
                        invoice.add_row(["Jadwal", kelas["Jadwal"]])
                        invoice.add_row(["Harga/Sesi", f"Rp {kelas['Harga/Sesi']}"])
                        invoice.add_row(["Saldo Awal", f"Rp {int(pengguna['Saldo']) + kelas['Harga/Sesi']}"])
                        invoice.add_row(["Saldo Tersisa", f"Rp {pengguna['Saldo']}"])
                        print("\nPembelian Berhasil")
                        print(invoice)
                        
                        input("Tekan tombol enter untuk kembali ke menu pelajar...")
                        return
                    else:
                        print("Saldo kurang, mohon isi ulang")
                        input("Tekan tombol enter untuk kembali ke menu pelajar...")
                        return
                    
            if not kelas_ditemukan:
                print(f"Kelas dengan kode {kode_beli} tidak ditemukan")
                continue
        input("Tekan tombol enter untuk kembali ke menu pelajar...")
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        beli_kelas()
        return

def cek_saldo():
    os.system("cls")

    saldo_table = PrettyTable()
    saldo_table.field_names = ["Username", "Saldo"]
    saldo_table.add_row([pengguna['Username'], f"Rp {pengguna['Saldo']}"])
    print(saldo_table)

def isi_saldo():
    os.system("cls")
    print(f"Saldo saat ini: Rp {pengguna['Saldo']}")
    
    table = PrettyTable()
    table.title = "ISI ULANG SALDO"
    table.field_names = ["No", "Pilihan Saldo"]
    pilihan_menu = [
        ["1", "Rp 100.000"],
        ["2", "Rp 150.000"],
        ["3", "Rp 200.000"],
        ["4", "Kembali"]
    ]
    for option in pilihan_menu:
        table.add_row(option)
    
    while True:
        print(table)
        
        try:
            pilihan = int(input("Pilih nominal saldo yang ingin diisi (1/2/3/4) = "))
            if pilihan == 4:
                print("Kembali ke menu pelajar")
                return
            
            nominal_saldo = {
                1: 100000,
                2: 150000,
                3: 200000
            }
            
            if pilihan in nominal_saldo:
                nominal_saldo = nominal_saldo[pilihan]
                konfirmasi = input(f"Anda akan mengisi saldo sebesar Rp {nominal_saldo}. Konfirmasi? (y/n) = ")
                if konfirmasi == 'y' and 'Y':
                    for user in data['User']:
                        if user['Username'] == pengguna['Username']:
                            user['Saldo'] = int(user['Saldo']) + nominal_saldo
                            pengguna['Saldo'] = user['Saldo']
                            break
                    simpan()
                    
                    print(f"Saldo berhasil ditambahkan, saldo sekarang = Rp {pengguna['Saldo']}")
                    input("Tekan tombol enter untuk kembali ke menu pelajar...")
                    return
                elif konfirmasi == 'n' and 'N':
                    print("Pengisian saldo dibatalkan")
                    continue
                else:
                    print("Jawaban tidak sesuai perintah, mohon isi ulang")
            else:
                print("Pilihan tidak valid")
        
        except ValueError:
            print("Mohon masukkan angka")
        except KeyboardInterrupt:
            print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
            isi_saldo()
            return

def cek_kelas():
    os.system("cls")
    
    try:
        if 'Kelas' not in pengguna or not pengguna['Kelas']:
            print("Belum punya kelas")
            input("Tekan tombol enter untuk kembali ke menu pelajar...")
            return

        kelas_tabel = PrettyTable()
        kelas_tabel.title = f"DAFTAR KELAS {pengguna['Nama'].upper()}"
        kelas_tabel.field_names = ["Kode", "Mata Kuliah", "Jadwal"]
        
        for kelas in pengguna['Kelas']:
            kelas_tabel.add_row([
                kelas.get("Kode"),
                kelas.get("Mata_Kuliah"),
                kelas.get("Jadwal")
            ])
        
        print(kelas_tabel)
        
        input("Tekan tombol enter untuk kembali ke menu pelajar...")
    except KeyboardInterrupt:
        print("DILARANG KERAS MENGETIK CTRL + C PAHAM")
        cek_kelas()
        return

menu_utama()