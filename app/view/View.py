import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from app.controller.Controller import Controller
from app.view.telas.Inicial import Inicial
from app.view.telas.Inserir import Inserir
from app.view.telas.Resultado import Resultado
from app.view.telas.Visualizar_turma import Visualizar_turma

class View(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("K-Volei")
        self.geometry("900x800")

        self.controller = Controller()

        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True)

        self.frames = {}

        for Page in (Inicial, Inserir, Resultado, Visualizar_turma):
            frame = Page(parent=main_container, view=self)
            name = Page.__name__
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Inicial")

    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()

    def selecionar_arquivo_treino(self):
        caminho = filedialog.askopenfilename(
            title="Selecione um arquivo CSV",
            filetypes=[
                ("Planilhas", "*.csv *.xlsx"),
                ("Arquivos CSV", "*.csv"),
                ("Arquivos Excel", "*.xlsx"),
            ],
            defaultextension=".csv"
        )
        if not caminho:
            return
        self.controller.abrir_arquivo_treino(caminho)
        self.show_frame("Inserir")

    def mostrar_resultado(self, resultado: dict):
        frame_resultado = self.frames["Resultado"]
        frame_resultado.atualizar(resultado)
        self.show_frame("Resultado")

    def ver_turmas(self):
        pasta_turmas = Path("turmas")

        if not pasta_turmas.exists():
            messagebox.showinfo(
                "Turmas",
                "Ainda não há turmas salvas.\nFinalize uma turma para gerar um arquivo CSV.",
                parent=self
            )
            return

        caminho = filedialog.askopenfilename(
            title="Selecione uma turma (CSV)",
            initialdir=pasta_turmas,
            filetypes=[
                ("Arquivos CSV", "*.csv"),
                ("Todos os arquivos", "*.*"),
            ],
            defaultextension=".csv"
        )

        if not caminho:
            return

        try:
            dados_turma = self.controller.carregar_turma(caminho)
        except Exception as e:
            messagebox.showerror(
                "Erro ao abrir turma",
                f"Ocorreu um erro ao carregar a turma:\n{e}",
                parent=self
            )
            return

        if not dados_turma:
            messagebox.showwarning(
                "Turma vazia",
                "Esse arquivo não contém dados de alunos.",
                parent=self
            )
            return

        frame_turma = self.frames["Visualizar_turma"]
        frame_turma.atualizar(dados_turma)
        self.show_frame("Visualizar_turma")

    def usar_modelo_treinado(self):
        caminho = filedialog.askopenfilename(
            title="Selecione um modelo KNN treinado (.pkl)",
            filetypes=[
                ("Modelos treinados", "*.pkl"),
                ("Todos os arquivos", "*.*"),
            ],
            defaultextension=".pkl"
        )
        if not caminho:
            return

        self.controller.carregar_modelo_treinado(caminho)
        self.show_frame("Inserir")