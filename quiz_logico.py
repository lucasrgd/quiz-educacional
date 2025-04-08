import sqlite3
import random

def carregar_perguntas():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM perguntas")
    perguntas = cursor.fetchall()
    conn.close()
    random.shuffle(perguntas)
    return perguntas

def salvar_pontuacao(nome, pontuacao):
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ranking (nome, pontuacao) VALUES (?, ?)", (nome, pontuacao))
    conn.commit()
    conn.close()

def obter_ranking():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, pontuacao FROM ranking ORDER BY pontuacao DESC LIMIT 10")
    ranking = cursor.fetchall()
    conn.close()
    return ranking
