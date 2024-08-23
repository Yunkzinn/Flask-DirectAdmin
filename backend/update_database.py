import sqlite3
from datetime import datetime

# Conecte-se ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Adicione a coluna created_at
try:
    cursor.execute('ALTER TABLE jurisprudence ADD COLUMN created_at TIMESTAMP')
    print("Coluna 'created_at' adicionada com sucesso.")
except sqlite3.OperationalError as e:
    print(f"Erro: {e}")

# Atualize todos os registros existentes com a data atual
cursor.execute('SELECT id FROM jurisprudence')
jurisprudences = cursor.fetchall()
now = datetime.utcnow()

for j in jurisprudences:
    cursor.execute('UPDATE jurisprudence SET created_at = ? WHERE id = ?', (now, j[0]))

# Salve as alterações e feche a conexão
conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso.")
