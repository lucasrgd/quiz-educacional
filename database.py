import sqlite3

def criar_banco():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS perguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT,
            alternativa_a TEXT,
            alternativa_b TEXT,
            alternativa_c TEXT,
            alternativa_d TEXT,
            correta TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            pontuacao INTEGER
        )
    ''')

    # Exemplo de perguntas (adicione mais se quiser)
    cursor.execute("INSERT INTO perguntas (pergunta, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta) VALUES (?, ?, ?, ?, ?, ?)",
                   ("Qual a capital do Brasil?", "São Paulo", "Brasília", "Rio de Janeiro", "Salvador", "b"))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_banco()
