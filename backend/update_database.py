import sqlite3

# Conecte-se ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Função para adicionar uma coluna a uma tabela
def add_column(table_name, column_name, column_type):
    try:
        cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}')
        print(f"Coluna '{column_name}' adicionada com sucesso na tabela {table_name}.")
    except sqlite3.OperationalError as e:
        print(f"Erro ao adicionar a coluna '{column_name}' na tabela {table_name}: {e}")

# Função para adicionar a coluna categoria
def add_categoria_column(table_name):
    add_column(table_name, 'categoria', 'TEXT')

# Adicione a coluna categoria nas tabelas recommendation, jurisprudence e article
tables = ['recommendation', 'jurisprudence', 'article']

for table in tables:
    add_categoria_column(table)

# Salve as alterações e feche a conexão
conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso.")
