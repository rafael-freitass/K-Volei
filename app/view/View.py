import tkinter as tk
from tkinter import ttk, filedialog
from app.controller.Controller import Controller

from app.view.telas.Inicial import Inicial
from app.view.telas.Inserir import Inserir
from app.view.telas.Resultado import Resultado

class View(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("K-Volei")
        self.geometry("900x800")

        self.controller = Controller()

        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True)

        self.frames = {}

        for Page in (Inicial, Inserir, Resultado):
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
        self.controller.abrir_arquivo_treino(caminho)
        self.show_frame("Inserir")