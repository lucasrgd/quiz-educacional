import sqlite3
import os
from datetime import datetime

def salvar_resultado(nome, acertos, erros):
    caminho = os.path.join(os.path.dirname(__file__), "quiz.db")
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute("""
        INSERT INTO respostas_jogadores (nome, acertos, erros, data)
        VALUES (?, ?, ?, ?)
    """, (nome, acertos, erros, data))

    conn.commit()
    conn.close()

def obter_ranking():
    caminho = os.path.join(os.path.dirname(__file__), "quiz.db")
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, acertos, erros, data
        FROM respostas_jogadores
        ORDER BY acertos DESC, erros ASC
        LIMIT 10
    """)
    ranking = cursor.fetchall()
    conn.close()
    return ranking
