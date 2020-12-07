import sqlite3

conexao = sqlite3.connect('usuarios.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 Name TEXT NOT NULL,
 Email TEXT NOT NULL,
 User TEXT NOT NULL,
 Password TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")