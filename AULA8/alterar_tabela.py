import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = '''
    UPDATE clientes
    SET nome = ?, idade = ?
    WHERE id = ?;
'''
a_nome = 'macaco'
a_idade = '12'
a_id = 2
cursor.execute(sql, [a_nome, a_idade, a_id])
conexao.commit()
conexao.close()