import sqlite3
import os

def carregar_perguntas():
    caminho = os.path.join(os.path.dirname(__file__), "quiz.db")
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM perguntas")
    perguntas = cursor.fetchall()
    conn.close()
    return perguntas
