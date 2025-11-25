from tkinter import ttk, messagebox

class Inicial(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent, padding=32)
        self.view_controller = view

        # Deixa a coluna principal expansiva para centralizar tudo
        self.columnconfigure(0, weight=1)

        # Estilo para título e textos
        style = ttk.Style(self)
        style.configure(
            "Titulo.TLabel",
            font=("Helvetica", 28, "bold")  # título bem grande
        )
        style.configure(
            "Descricao.TLabel",
            font=("Helvetica", 11),
            wraplength=720
        )
        style.configure(
            "Dica.TLabel",
            font=("Helvetica", 10),
            foreground="#555",
            wraplength=720
        )

        self.titulo()
        self.dica()
        self.buttons()

    def titulo(self):
        # Título principal
        self.titulo = ttk.Label(
            self,
            text="Bem-vindo(a) ao K-Volei!",
            style="Titulo.TLabel",
            anchor="center"
        )
        self.titulo.grid(row=0, column=0, pady=(0, 16), sticky="n")

        # Descrição logo abaixo
        self.descricao = ttk.Label(
            self,
            text="Vamos ajudar a decidir qual é a melhor posição para os alunos da sua turma jogarem vôlei.",
            style="Descricao.TLabel",
            justify="center"
        )
        self.descricao.grid(row=1, column=0, pady=(0, 10), sticky="ew")
    
    def dica(self):
        self.dica = ttk.Label(
            self,
            text="Para começar, você pode importar um dataset do PROESP, usar um modelo já treinado ou visualizar suas turmas.",
            style="Dica.TLabel",
            justify="center"
        )
        self.dica.grid(row=2, column=0, pady=(0, 24), sticky="ew")

    def buttons(self):
        self.btns = ttk.Frame(self)
        self.btns.grid(row=3, column=0, pady=(0, 8))
        
        # 2 colunas para organizar em grade 2x2
        self.btns.columnconfigure((0, 1), weight=1, uniform="btns")

        # Linha 1: ações principais
        self.btn_importar = ttk.Button(
            self.btns,
            text="Importar dataset",
            command=self.view_controller.selecionar_arquivo_treino
        )
        self.btn_importar.grid(row=0, column=0, padx=8, pady=6, sticky="ew")

        self.btn_modelo = ttk.Button(
            self.btns,
            text="Usar modelo já treinado",
            command=self.view_controller.usar_modelo_treinado
        )
        self.btn_modelo.grid(row=0, column=1, padx=8, pady=6, sticky="ew")

        # Linha 2: opções de suporte / navegação
        self.btn_ver_turmas = ttk.Button(
            self.btns,
            text="Ver turmas",
            command=self.view_controller.ver_turmas
        )
        self.btn_ver_turmas.grid(row=1, column=0, padx=8, pady=6, sticky="ew")

        self.btn_info = ttk.Button(
            self.btns,
            text="Quais dados utilizamos?",
            command=self.mostrar_info
        )
        self.btn_info.grid(row=1, column=1, padx=8, pady=6, sticky="ew")

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