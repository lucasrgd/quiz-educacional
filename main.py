import tkinter as tk
from tkinter import messagebox, simpledialog
from quiz_logico import carregar_perguntas
from database import salvar_resultado, obter_ranking

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Educacional")
        self.root.geometry("600x400")  # Largura x Altura
        self.root.resizable(False, False)  # Impede redimensionamento


        self.perguntas = carregar_perguntas()
        self.indice_pergunta = 0
        self.acertos = 0
        self.erros = 0

        self.nome = simpledialog.askstring("Nome", "Digite seu nome:")

        self.pergunta_var = tk.StringVar()
        self.opcao_var = tk.StringVar()

        self.label_pergunta = tk.Label(root, textvariable=self.pergunta_var, font=("Arial", 14), wraplength=500)
        self.label_pergunta.pack(pady=20)

        self.botoes_opcoes = []
        for i in range(4):
            botao = tk.Radiobutton(root, variable=self.opcao_var, value="", font=("Arial", 12), wraplength=400)
            botao.pack(anchor="w")
            self.botoes_opcoes.append(botao)

        self.botao_responder = tk.Button(root, text="Responder", command=self.verificar_resposta, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.botao_responder.pack(pady=10)

        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.indice_pergunta < len(self.perguntas):
            pergunta_atual = self.perguntas[self.indice_pergunta]
            self.pergunta_var.set(f"{self.indice_pergunta+1}. {pergunta_atual[1]}")

            opcoes = pergunta_atual[2:6]
            for i in range(4):
                self.botoes_opcoes[i]['text'] = opcoes[i]
                self.botoes_opcoes[i]['value'] = opcoes[i]

            self.opcao_var.set(None)
        else:
            self.finalizar_quiz()

    def verificar_resposta(self):
        if not self.opcao_var.get():
            messagebox.showwarning("Aviso", "Selecione uma opção.")
            return

        resposta_correta = self.perguntas[self.indice_pergunta][6]
        if self.opcao_var.get() == resposta_correta:
            self.acertos += 1
        else:
            self.erros += 1

        self.indice_pergunta += 1
        self.mostrar_pergunta()

    def finalizar_quiz(self):
        salvar_resultado(self.nome, self.acertos, self.erros)
        resultado = f"Quiz Finalizado!\nAcertos: {self.acertos}\nErros: {self.erros}"
        messagebox.showinfo("Resultado", resultado)

        ranking = obter_ranking()
        ranking_str = "\n".join([f"{i+1}. {r[0]} - {r[1]} acertos, {r[2]} erros - {r[3]}" for i, r in enumerate(ranking)])
        messagebox.showinfo("Ranking", f"Top 10:\n{ranking_str}")

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
