import database
from prettytable import PrettyTable

def tambah(nama_buku, genre, pengarang, penerbit):
    database.c.execute('SELECT * FROM buku WHERE nama_buku = ?', (nama_buku,))
    existing_data = database.c.fetchone()
    if existing_data:
        print(f"Error: Buku dengan nama '{nama_buku}' sudah ada di database.")
    else:
        database.c.execute('INSERT INTO buku (nama_buku, genre, pengarang, penerbit) VALUES (?, ?, ?, ?)',
                (nama_buku, genre, pengarang, penerbit))
        database.conn.commit()
        print(f"\nBuku '{nama_buku}' berhasil ditambahkan!\n")

def tampilkan():
    database.c.execute('SELECT * FROM buku')
    buku = database.c.fetchall()
    if buku:
        table = PrettyTable(["ID", "Nama Buku", "Genre", "Pengarang", "Penerbit"])
        for row in buku:
            table.add_row(row)
        print(table)
    else:
        print("Belum ada buku di database.")
        
def cek_id(id_buku):
    database.c.execute("SELECT id FROM buku WHERE id = ?", (id_buku,))
    result = database.c.fetchone()
    return result is not None

def cari(keyword):
    query = f"%{keyword}%"  # Kata kunci pencarian yang akan cocok dengan bagian apapun dari string
    database.c.execute('SELECT * FROM buku WHERE nama_buku LIKE ? OR genre LIKE ? OR pengarang LIKE ? OR penerbit LIKE ?', 
              (query, query, query, query))
    hasil = database.c.fetchall()
    if hasil:
        table = PrettyTable(["ID", "Nama Buku", "Genre", "Pengarang", "Penerbit"])
        for row in hasil:
            table.add_row(row)
        print(table)
    else:
        print(f"Tidak ditemukan buku dengan kata kunci '{keyword}'")

def ubah(id_buku, nama_buku, genre, pengarang, penerbit):
    database.c.execute('SELECT id FROM buku WHERE nama_buku = ? AND id != ?', (nama_buku, id_buku))
    buku_sama = database.c.fetchone()
    
    if buku_sama:
        print(f"Error: Buku dengan nama '{nama_buku}' sudah ada di database.")
    else:
        # Lakukan update jika tidak ada konflik nama
        database.c.execute(
            'UPDATE buku SET nama_buku = ?, genre = ?, pengarang = ?, penerbit = ? WHERE id = ?', 
            (nama_buku, genre, pengarang, penerbit, id_buku)
        )
        database.conn.commit()
        
        if database.c.rowcount > 0:
            print(f'Buku ID {id_buku} berhasil diubah!')
        else:
            print(f'Buku ID {id_buku} tidak ditemukan.')

def hapus(id_buku):
    database.c.execute('DELETE FROM buku WHERE id = ?', (id_buku,))
    database.conn.commit()
    if database.c.rowcount > 0:
        print(f'Buku ID {id_buku} berhasil dihapus!')
    else:
        print(f'Buku ID {id_buku} tidak ditemukan.')
