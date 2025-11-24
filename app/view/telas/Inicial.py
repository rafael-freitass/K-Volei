from tkinter import ttk, messagebox

class Inicial(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent, padding=32)
        self.view_controller = view
        self.columnconfigure(0, weight=1)
        
        self.titulo()
        self.dica()
        self.buttons()

    def titulo(self):
        self.titulo = ttk.Label(self, text="Bem-vindo(a) ao K-volei!")
        self.titulo.grid(row=0, column=0, pady=(0, 12), sticky="n")

        self.descricao = ttk.Label(
            self,
            text="Iremos decidir qual a melhor posição para os alunos da sua turma jogar no volei",
            wraplength=720,
            justify="center"
        )
        self.descricao.grid(row=1, column=0, pady=(0, 8), sticky="ew")
    
    def dica(self):
        self.dica = ttk.Label(
            self,
            text="Importe um dataset com os testes do PROESP para começar!",
            foreground="#555",
            wraplength=720,
            justify="center"
        )
        self.dica.grid(row=2, column=0, pady=(0, 24), sticky="ew")

    def buttons(self):
        self.btns = ttk.Frame(self)
        self.btns.grid(row=3, column=0, pady=(0, 8))
        self.btns.columnconfigure((0,1), weight=1)

        self.btn_importar = ttk.Button(self.btns, text="Importar dataset", command=lambda: self.view_controller.selecionar_arquivo_treino())
        self.btn_importar.grid(row=0, column=0, padx=6)

        self.btn_info = ttk.Button(self.btns, text="Quais dados utilizamos?", command=self.mostrar_info)
        self.btn_info.grid(row=0, column=1, padx=6)

    def mostrar_info(self):
        info = (
            "Utilizamos dados de testes do PROESP:\n"
            "• Medidas de altura em pé, altura sentado e massa\n"
            "• Flexibilidade com Sentar e Alcançar\n"
            "• Máximo de Abdominais em 1 min\n"
            "• Arremesso Med Ball 2kg\n"
            "• Salto Vertical e Salto Horizontal\n"
            "\nEsses indicadores sugerem a posição ideal no voleibol."
        )
        messagebox.showinfo("Quais dados utilizamos?", info, parent=self)