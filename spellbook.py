import database
import buku.buku as buku


print ("------------------------------------")
print ("|<<<<Selamat Datang Di SpellBook>>>>|")
print ("------------------------------------")

def menu():
    while True:
        print("\n <<<<< Menu SpellBook >>>>>")
        print("<1> Tambah Buku")
        print("<2> Tampilkan Buku")
        print("<3> Cari Buku ")
        print("<4> Ubah Buku")
        print("<5> Hapus Buku")
        print("<6> Keluar")

        pilihan = input("Pilih Menu: ")

        if pilihan == '1': 
            nama_buku = input("Masukkan nama buku: ")
            while len(nama_buku) == 0:
                nama_buku = input("Masukkan nama buku: ")
            genre = input("Masukkan genre buku: ")
            while len(genre) == 0:
                genre = input("Masukkan genre buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            while len(pengarang) == 0:
                pengarang = input("Masukkan pengarang buku: ")
            penerbit = input("Masukkan penerbit buku: ")
            while len(penerbit) == 0:
                penerbit = input("Masukkan penerbit buku: ")
            while True:
                pilihan = input("Apakah Anda yakin ingin menyimpan (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    buku.tambah(nama_buku, genre, pengarang, penerbit)
                    print(f"\nBuku '{nama_buku}' berhasil ditambahkan!\n")
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    menu()
                else:
                    print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")
                    
        elif pilihan == '2':
            buku.tampilkan()
            
        elif pilihan == '3':
            while True:
                keyword = input("Masukkan kata kunci pencarian: ").strip()
                if len(keyword) > 0:
                    break
                else:
                    print("Kata kunci tidak boleh kosong. Silakan masukkan kata kunci yang valid.")
            
            database.c.execute('SELECT COUNT(*) FROM buku')
            jumlah_buku = database.c.fetchone()[0]
            if jumlah_buku == 0:
                print("Database kosong, tidak ada data untuk dicari.")
                menu() 
                return  
            
            buku.cari(keyword)
            
        elif pilihan == '4':
            buku.tampilkan()
            print()
            
            database.c.execute('SELECT COUNT(*) FROM buku')
            jumlah_buku = database.c.fetchone()[0]
            if jumlah_buku == 0:
                menu()
                return 
            
            while True:
                try:
                    id_buku = int(input("Masukkan ID buku yang ingin diubah: "))
                    if buku.cek_id(id_buku):
                        break
                    else:
                        print("ID buku tidak ditemukan. Silakan masukkan ID yang benar.")
                except ValueError:
                    print("Masukkan angka ID buku yang benar!.")
                
            nama_buku = input("Masukkan nama buku: ")
            while len(nama_buku) == 0:
                nama_buku = input("Masukkan nama buku: ")
            genre = input("Masukkan genre buku: ")
            while len(genre) == 0:
                genre = input("Masukkan genre buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            while len(pengarang) == 0:
                pengarang = input("Masukkan pengarang buku: ")
            penerbit = input("Masukkan penerbit: ")
            while len(penerbit) == 0:
                penerbit = input("Masukkan penerbit buku: ")
            while True:
                pilihan = input("Apakah Anda yakin ingin mengubah (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    buku.ubah(id_buku, nama_buku, genre, pengarang, penerbit)
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    print("Buku tidak berhasil diubah!")
                    menu()
                else:
                        print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")      
                         
        elif pilihan == '5':
            buku.tampilkan()
            print()
            
            database.c.execute('SELECT COUNT(*) FROM buku')
            jumlah_buku = database.c.fetchone()[0]
            if jumlah_buku == 0:
                menu()
                return 
            
            while True:
                try:
                    id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
                    if buku.cek_id(id_buku):
                        break
                    else:
                        print("ID buku tidak ditemukan. Silakan masukkan ID yang benar.")
                except ValueError:
                    print("Masukkan angka ID buku yang benar!.")
            
            while True:
                pilihan = input("Apakah Anda yakin ingin menghapus (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    buku.hapus(id_buku)
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    print("Buku tidak berhasil dihapus!")
                    menu()
                else:
                    print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")
                    
        elif pilihan == '6':
            while True:
                pilihan = input("Apakah Anda yakin ingin keluar (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    print("\nTerima kasih telah menggunakan program ini!")
                    exit()
                elif pilihan == 'no' or pilihan== 'n':
                    menu()
                    break
                else:
                    print("Input tidak valid. Harap masukkan 'yes', 'y', 'no', atau 'n'.")
        else:
            print("\nPilihan tidak valid. Pilih opsi angka 1 - 6")

if __name__ == '__main__':
    menu()
