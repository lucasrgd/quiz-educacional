# 🧠 Quiz Educacional com Ranking

Projeto desenvolvido para a disciplina **RAD - Aplicações Rápidas em Python**, com foco no uso de **Tkinter** e **SQLite** para criar uma aplicação educacional com interface gráfica, pontuação e ranking de desempenho.

---

## 📚 Objetivo

Criar um sistema de quiz interativo com perguntas de múltipla escolha, que registre respostas corretas e erradas, exiba a pontuação final e armazene os resultados em um banco de dados para geração de ranking.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- Tkinter (interface gráfica)
- SQLite3 (banco de dados local)
- Git e GitHub (controle de versão)

---

## ⚙️ Funcionalidades

- Interface gráfica com tamanho ajustado para melhor visualização
- Registro de acertos e erros durante o quiz
- Armazenamento dos resultados no banco de dados
- Exibição do ranking com nome, pontuação, acertos, erros e data
- Banco de dados populado automaticamente com perguntas de exemplo

---

## 📁 Estrutura dos Arquivos

 quiz-educacional ├── criar_banco.py # Criação e população do banco de dados ├── database.py # Conexão e manipulação do banco de dados ├── main.py # Arquivo principal com a interface gráfica ├── quiz_logico.py # Lógica do quiz e carregamento das perguntas ├── quiz.db # Banco de dados SQLite └── README.md # Documentação do projeto

yaml
Copiar
Editar


---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/lucasrgd/quiz-educacional.git
cd quiz-educacional

2. Crie e popule o banco de dados:
bash
python criar_banco.py

3. Inicie a aplicação:
python main.py

👤 Desenvolvedor
Lucas Rodrigues Da Silva
Estudante de Análise e Desenvolvimento de Sistemas - 23 anos
Iniciando a jornada no mundo da tecnologia!

GitHub: @lucasrgd

📌 Observações
Projeto acadêmico — não utilizar em produção sem adaptações.

Todos os arquivos necessários estão no repositório para funcionamento imediato.

Se houver erro de banco, execute criar_banco.py antes de iniciar o sistema.


---

Agora é só colar no seu `README.md`, salvar, e fazer o commit:

```bash
git add README.md
git commit -m "Atualização final do README"
git push origin principal
