from tkinter import ttk

class Inicial(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        title = ttk.Label(self, text="Tela Inicial", font=("TkDefaultFont", 16, "bold"))
        title.pack(pady=20)