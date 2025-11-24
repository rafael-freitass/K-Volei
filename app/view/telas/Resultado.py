import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Resultado(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent, padding=24)
        self.view = view

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.header()
        self.info_pessoa()
        self.grafico()
        self.footer()

    def header(self):
        titulo = ttk.Label(self, text="Resultado da Avaliação", font=("Segoe UI", 16, "bold"))
        titulo.grid(row=0, column=0, sticky="w", pady=(0, 16))

    def info_pessoa(self):
        caixa = ttk.LabelFrame(self, text="Informações do atleta")
        caixa.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)
        caixa.columnconfigure(3, weight=1)

        ttk.Label(caixa, text="Nome:").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=4)
        self.lbl_nome = ttk.Label(caixa, text="-")
        self.lbl_nome.grid(row=0, column=1, sticky="w", padx=(0, 8), pady=4)

        ttk.Label(caixa, text="Idade:").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=4)
        self.lbl_idade = ttk.Label(caixa, text="-")
        self.lbl_idade.grid(row=0, column=3, sticky="w", padx=(0, 8), pady=4)

        ttk.Label(caixa, text="Posição recomendada:").grid(row=1, column=0, sticky="w", padx=(8, 4), pady=4)
        self.lbl_posicao = ttk.Label(caixa, text="-", font=("Segoe UI", 11, "bold"))
        self.lbl_posicao.grid(row=1, column=1, sticky="w", padx=(0, 8), pady=4)

    def grafico(self):
        frame_grafico = ttk.LabelFrame(self, text="Probabilidade por posição (teia de aranha)")
        frame_grafico.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        frame_grafico.columnconfigure(0, weight=1)
        frame_grafico.rowconfigure(0, weight=1)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111, polar=True)

        self.canvas = FigureCanvasTkAgg(self.figure, master=frame_grafico)
        widget_canvas = self.canvas.get_tk_widget()
        widget_canvas.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

    def footer(self):
        btns = ttk.Frame(self)
        btns.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        btns.columnconfigure(0, weight=1)

        btn_voltar = ttk.Button(btns, text="Nova avaliação", command=lambda: self.view.show_frame("Inicial"))
        btn_voltar.grid(row=0, column=0, sticky="e")


    def atualizar(self, resultado: dict):
        nome = resultado.get("nome", "-")
        idade = resultado.get("idade", "-")
        posicao = resultado.get("posicao_prevista", "-")
        proba = resultado.get("proba", None)
        classes = resultado.get("classes", None)

        self.lbl_nome.config(text=nome)
        self.lbl_idade.config(text=f"{idade} anos" if idade not in ("", "-") else "-")
        self.lbl_posicao.config(text=posicao)

        if proba is not None and classes is not None:
            self._desenhar_radar(classes, proba, titulo=f"Distribuição de probabilidade - {posicao}")
        else:
            self._limpar_grafico(titulo="Sem probabilidades disponíveis")

    def _limpar_grafico(self, titulo=""):
        self.ax.clear()
        self.ax.set_title(titulo, pad=20)
        self.canvas.draw_idle()

    def _desenhar_radar(self, classes, proba, titulo=""):
        self.ax.clear()

        classes = list(classes)
        valores = list(proba)

        N = len(classes)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

        angles += angles[:1]
        valores += valores[:1]

        self.ax.plot(angles, valores, linewidth=2)
        self.ax.fill(angles, valores, alpha=0.25)

        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(classes)

        self.ax.set_ylim(0, 1)

        self.ax.set_title(titulo, pad=20)

        self.canvas.draw_idle()