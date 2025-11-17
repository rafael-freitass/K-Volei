from tkinter import ttk

class Resultado(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent)
        self.controller = view.controller

        title = ttk.Label(self, text="Tela Resultado", font=("TkDefaultFont", 16, "bold"))
        title.pack(pady=20)