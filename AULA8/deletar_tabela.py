import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = 'DELETE FROM clientes WHERE id = ?'

d_id = 3
cursor.execute(sql, [d_id])

conexao.commit()
conexao.close()