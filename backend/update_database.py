import sqlite3
from datetime import datetime

# Conecte-se ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Função para adicionar a coluna created_at e atualizar registros existentes
def add_created_at_column(table_name):
    try:
        cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN created_at TIMESTAMP')
        print(f"Coluna 'created_at' adicionada com sucesso na tabela {table_name}.")
    except sqlite3.OperationalError as e:
        print(f"Erro ao adicionar a coluna na tabela {table_name}: {e}")

    # Atualize todos os registros existentes com a data atual
    cursor.execute(f'SELECT id FROM {table_name}')
    records = cursor.fetchall()
    now = datetime.utcnow()

    for record in records:
        cursor.execute(f'UPDATE {table_name} SET created_at = ? WHERE id = ?', (now, record[0]))

# Adicione a coluna created_at nas tabelas recommendation, jurisprudence e article
add_created_at_column('recommendation')
add_created_at_column('jurisprudence')
add_created_at_column('article')

# Salve as alterações e feche a conexão
conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso.")
