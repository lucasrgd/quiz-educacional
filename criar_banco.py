import sqlite3
import os

def criar_banco():
    caminho = os.path.join(os.path.dirname(__file__), "quiz.db")
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    # Tabelas
    cursor.execute("DROP TABLE IF EXISTS perguntas")
    cursor.execute("DROP TABLE IF EXISTS respostas_jogadores")

    cursor.execute("""
        CREATE TABLE perguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enunciado TEXT NOT NULL,
            opcao1 TEXT NOT NULL,
            opcao2 TEXT NOT NULL,
            opcao3 TEXT NOT NULL,
            opcao4 TEXT NOT NULL,
            correta TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE respostas_jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            acertos INTEGER,
            erros INTEGER,
            data TEXT
        )
    """)

    perguntas_exemplo = [
        ("Qual a capital do Brasil?", "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Brasília"),
        ("Quem pintou a Mona Lisa?", "Picasso", "Van Gogh", "Leonardo da Vinci", "Michelangelo", "Leonardo da Vinci"),
        ("Qual o maior planeta do sistema solar?", "Terra", "Júpiter", "Marte", "Saturno", "Júpiter")
    ]

    cursor.executemany("""
        INSERT INTO perguntas (enunciado, opcao1, opcao2, opcao3, opcao4, correta)
        VALUES (?, ?, ?, ?, ?, ?)
    """, perguntas_exemplo)

    conn.commit()
    conn.close()
    print("✅ Banco de dados criado e populado com sucesso!")

if __name__ == "__main__":
    criar_banco()
