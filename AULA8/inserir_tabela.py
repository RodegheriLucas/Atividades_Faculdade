import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = """ 
    INSERT INTO clientes(nome, idade) VALUES(?, ?);
"""
i_nome = 'lucas'
i_idade = 19
cursor.execute(sql, [i_nome, i_idade])
conexao.commit()
conexao.close()
print('Gravou')