import tkinter as tk
from tkinter import ttk

class Visualizar_turma(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent, padding=24)
        self.view = view

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.header()
        self.tabela()
        self.footer()

    def header(self):
        titulo = ttk.Label(self, text="Resumo da Turma", font=("Segoe UI", 16, "bold"))
        titulo.grid(row=0, column=0, sticky="w", pady=(0, 16))

    def tabela(self):
        frame_tab = ttk.Frame(self)
        frame_tab.grid(row=1, column=0, sticky="nsew")

        colunas = ("nome", "idade", "posicao")
        self.tree = ttk.Treeview(frame_tab, columns=colunas, show="headings")

        self.tree.heading("nome", text="Nome")
        self.tree.heading("idade", text="Idade")
        self.tree.heading("posicao", text="Posição recomendada")

        self.tree.column("nome", width=200)
        self.tree.column("idade", width=80, anchor="center")
        self.tree.column("posicao", width=160)

        scrollbar = ttk.Scrollbar(frame_tab, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        frame_tab.columnconfigure(0, weight=1)
        frame_tab.rowconfigure(0, weight=1)

    def footer(self):
        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, sticky="ew", pady=(8, 0))
        btns.columnconfigure(0, weight=1)

        btn_nova_turma = ttk.Button(btns, text="Voltar ao Inicio", command=self.voltar_inicial)
        btn_nova_turma.grid(row=0, column=0, sticky="e")

    def atualizar(self, dados_turma: list[dict]):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for aluno in dados_turma:
            self.tree.insert(
                "",
                "end",
                values=(
                    aluno.get("nome", ""),
                    aluno.get("idade", ""),
                    aluno.get("posicao_prevista", ""),
                ),
            )

    def voltar_inicial(self):
        self.view.controller.model.alunos_turma
        self.view.show_frame("Inicial")