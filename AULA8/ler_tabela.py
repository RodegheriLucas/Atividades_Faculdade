import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = 'SELECT * FROM clientes;'
cursor.execute(sql)
resultados = cursor.fetchall()
print('-->', resultados)
conexao.close()