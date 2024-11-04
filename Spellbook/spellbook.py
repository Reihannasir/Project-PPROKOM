from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect('spellbook.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS buku (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_buku TEXT NOT NULL,
    genre TEXT NOT NULL,
    pengarang TEXT NOT NULL,
    penerbit TEXT NOT NULL
)
''')
conn.commit()

print ("------------------------------------")
print ("|<<<Selamat Datang Di SpellBook>>>|")
print ("------------------------------------")

def tambah_buku(nama_buku, genre, pengarang, penerbit):
    c.execute('INSERT INTO buku (nama_buku, genre, pengarang, penerbit) VALUES (?, ?, ?, ?)',
              (nama_buku, genre, pengarang, penerbit))
    conn.commit()
    print(f'Buku "{nama_buku}" berhasil ditambahkan!')

def tampilkan_buku():
    c.execute('SELECT * FROM buku')
    buku = c.fetchall()
    if buku:
        table = PrettyTable(["ID", "Nama Buku", "Genre", "Pengarang", "Penerbit"])
        for row in buku:
            table.add_row(row)
        print(table)
    else:
        print("Belum ada buku di database.")

def cari_buku(keyword):
    query = f"%{keyword}%"  # Kata kunci pencarian yang akan cocok dengan bagian apapun dari string
    c.execute('SELECT * FROM buku WHERE nama_buku LIKE ? OR genre LIKE ? OR pengarang LIKE ? OR penerbit LIKE ?', 
              (query, query, query, query))
    hasil = c.fetchall()
    if hasil:
        table = PrettyTable(["ID", "Nama Buku", "Genre", "Pengarang", "Penerbit"])
        for row in hasil:
            table.add_row(row)
        print(table)
    else:
        print(f'Tidak ditemukan buku dengan kata kunci "{keyword}".')

def ubah_buku(id_buku, nama_buku, genre, pengarang, penerbit):
    c.execute('UPDATE buku SET nama_buku = ?, genre = ?, pengarang = ?, penerbit = ? WHERE id = ?', 
              (nama_buku, genre, pengarang, penerbit, id_buku))
    conn.commit()
    if c.rowcount > 0:
        print(f'Buku ID {id_buku} berhasil diubah!')
    else:
        print(f'Buku ID {id_buku} tidak ditemukan.')

def hapus_buku(id_buku):
    c.execute('DELETE FROM buku WHERE id = ?', (id_buku,))
    conn.commit()
    if c.rowcount > 0:
        print(f'Buku ID {id_buku} berhasil dihapus!')
    else:
        print(f'Buku ID {id_buku} tidak ditemukan.')

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
            genre = input("Masukkan genre buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            penerbit = input("Masukkan penerbit buku: ")
            while True:
                pilihan = input("Apakah Anda yakin ingin menyimpan (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    tambah_buku(nama_buku, genre, pengarang, penerbit)
                    print(f"\nBuku '{nama_buku}' berhasil ditambahkan!\n")
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    menu()
                else:
                    print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")
        elif pilihan == '2':
            tampilkan_buku()
        elif pilihan == '3':
            keyword = input("Masukkan kata kunci pencarian: ")
            cari_buku(keyword)
        elif pilihan == '4':
            id_buku = int(input("Masukkan ID buku yang ingin diubah: "))
            nama_buku = input("Masukkan nama buku: ")
            genre = input("Masukkan genre: ")
            pengarang = input("Masukkan pengarang: ")
            penerbit = input("Masukkan penerbit: ")
            while True:
                pilihan = input("Apakah Anda yakin ingin mengubah (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    ubah_buku(id_buku, nama_buku, genre, pengarang, penerbit)
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    menu()
                else:
                        print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")       
        elif pilihan == '5':
            id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
            while True:
                pilihan = input("Apakah Anda yakin ingin menghapus (y/n)?: ").lower()
                if pilihan == 'yes' or pilihan == 'y':
                    hapus_buku(id_buku)
                    break
                elif pilihan == 'no' or pilihan== 'n':
                    menu()
                else:
                    print("\nPilihan tidak valid. Pilih 'yes' atau 'no'")
        elif pilihan == '6':
            pilihan = input("Apakah Anda yakin ingin keluar (y/n)?: ").lower()
            if pilihan == 'yes' or pilihan == 'y':
                print("\nTerima kasih telah menggunakan program ini!")
                break
            elif pilihan == 'no' or pilihan== 'n':
                menu()
        else:
            print("\nPilihan tidak valid. Pilih opsi angka 1 - 6")

if __name__ == '__main__':
    menu()

conn.close()
