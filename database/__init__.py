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