import tkinter as tk
from tkinter import messagebox
from quiz_logic import carregar_perguntas, salvar_pontuacao, obter_ranking # type: ignore

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Educacional")
        self.pontuacao = 0
        self.indice_pergunta = 0
        self.perguntas = carregar_perguntas()
        self.nome_jogador = ""

        self.iniciar_quiz()

    def iniciar_quiz(self):
        self.tela_inicio()

    def tela_inicio(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Digite seu nome:").pack(pady=10)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)
        tk.Button(self.root, text="Iniciar Quiz", command=self.comecar_quiz).pack(pady=10)
        tk.Button(self.root, text="Ver Ranking", command=self.mostrar_ranking).pack()

    def comecar_quiz(self):
        self.nome_jogador = self.nome_entry.get()
        if not self.nome_jogador:
            messagebox.showwarning("Aviso", "Digite seu nome.")
            return
        self.pontuacao = 0
        self.indice_pergunta = 0
        self.perguntas = carregar_perguntas()
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.indice_pergunta >= len(self.perguntas):
            self.finalizar_quiz()
            return

        pergunta = self.perguntas[self.indice_pergunta]
        self.id_atual, texto, a, b, c, d, correta = pergunta
        self.resposta_correta = correta

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=texto, wraplength=400).pack(pady=10)
        self.var_resposta = tk.StringVar()

        tk.Radiobutton(self.root, text=a, variable=self.var_resposta, value='a').pack(anchor='w')
        tk.Radiobutton(self.root, text=b, variable=self.var_resposta, value='b').pack(anchor='w')
        tk.Radiobutton(self.root, text=c, variable=self.var_resposta, value='c').pack(anchor='w')
        tk.Radiobutton(self.root, text=d, variable=self.var_resposta, value='d').pack(anchor='w')

        tk.Button(self.root, text="Próxima", command=self.verificar_resposta).pack(pady=10)

    def verificar_resposta(self):
        resposta = self.var_resposta.get()
        if resposta == self.resposta_correta:
            self.pontuacao += 1
        self.indice_pergunta += 1
        self.mostrar_pergunta()

    def finalizar_quiz(self):
        salvar_pontuacao(self.nome_jogador, self.pontuacao)
        messagebox.showinfo("Fim de Jogo", f"Pontuação: {self.pontuacao}")
        self.tela_inicio()

    def mostrar_ranking(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🏆 Ranking", font=("Helvetica", 16)).pack(pady=10)

        ranking = obter_ranking()
        for i, (nome, pontuacao) in enumerate(ranking):
            tk.Label(self.root, text=f"{i+1}º {nome}: {pontuacao} pontos").pack()

        tk.Button(self.root, text="Voltar", command=self.tela_inicio).pack(pady=10)

if __name__ == "__main__":
    from database import criar_banco
    criar_banco()

    root = tk.Tk()
    root.geometry("500x400")
    app = QuizApp(root)
    root.mainloop()
