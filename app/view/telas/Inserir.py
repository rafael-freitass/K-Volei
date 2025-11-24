from tkinter import ttk
from tkinter import messagebox

class Inserir(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent, padding=24)
        self.view = view
        self.controller = view.controller
        self.columnconfigure(0, weight=1)

        self.titulo()
        self.identificacao()
        self.medidas()
        self.flexibilidadeibilidade()
        self.abdominal()
        self.arremessoME()
        self.saltos()
        self.footer()

    def titulo(self):
        title = ttk.Label(self, text="Insira seus dados:")
        title.grid(row=0, column=0, sticky="w", pady=(0, 16))

    def identificacao(self):
        caixa = ttk.LabelFrame(self, text="Identificação")
        caixa.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        for i in range(4):
            caixa.columnconfigure(i, weight=1)

        ttk.Label(caixa, text="Nome").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_nome = ttk.Entry(caixa)
        self.input_nome.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Idade (anos)").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=6)
        self.input_idade = ttk.Entry(caixa)
        self.input_idade.grid(row=0, column=3, sticky="ew", padx=(0, 8), pady=6)

    def medidas(self):
        caixa = ttk.LabelFrame(self, text="Medidas")
        caixa.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        for i in range(6):
            caixa.columnconfigure(i, weight=1)

        ttk.Label(caixa, text="Altura em pé (cm)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_estatura = ttk.Entry(caixa)
        self.input_estatura.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Altura sentado (cm)").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=6)
        self.input_alturaTC = ttk.Entry(caixa)
        self.input_alturaTC.grid(row=0, column=3, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Peso (kg)").grid(row=0, column=4, sticky="w", padx=(8, 4), pady=6)
        self.input_peso = ttk.Entry(caixa)
        self.input_peso.grid(row=0, column=5, sticky="ew", padx=(0, 8), pady=6)

    def flexibilidadeibilidade(self):
        caixa = ttk.LabelFrame(self, text="flexibilidadeibilidade")
        caixa.grid(row=3, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Sentar e alcançar (cm)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_flexibilidade = ttk.Entry(caixa)
        self.input_flexibilidade.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def abdominal(self):
        caixa = ttk.LabelFrame(self, text="Resistência abdominal")
        caixa.grid(row=4, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Máximo em 1 min (reps)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_abdominal = ttk.Entry(caixa)
        self.input_abdominal.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def arremessoME(self):
        caixa = ttk.LabelFrame(self, text="arremessoMEdicine Ball 2kg")
        caixa.grid(row=5, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Distância (m)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_arremessoME = ttk.Entry(caixa)
        self.input_arremessoME.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def saltos(self):
        caixa = ttk.LabelFrame(self, text="Saltos")
        caixa.grid(row=6, column=0, sticky="ew", pady=(0, 12))
        for i in range(4):
            caixa.columnconfigure(i, weight=1)

        ttk.Label(caixa, text="Salto vertical (cm)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_Svertical = ttk.Entry(caixa)
        self.input_Svertical.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Salto horizontal (cm)").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=6)
        self.input_Shorizontal = ttk.Entry(caixa)
        self.input_Shorizontal.grid(row=0, column=3, sticky="ew", padx=(0, 8), pady=6)

    def footer(self):
        btns = ttk.Frame(self)
        btns.grid(row=8, column=0, sticky="ew")
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=0)

        self.btn_voltar = ttk.Button(btns, text="Voltar", command=lambda: self.view.show_frame("Inicial"))
        self.btn_voltar.grid(row=0, column=0, sticky="w")

        self.btn_salvar = ttk.Button(btns, text="Salvar dados", command=self.salvar_e_avancar)
        self.btn_salvar.grid(row=0, column=1, sticky="e")

    def salvar_e_avancar(self):
        dados_tela = {
            "nome": self.input_nome.get(),
            "idade": self.input_idade.get(),
            "estatura": self.input_estatura.get(),
            "alturaTC": self.input_alturaTC.get(),
            "peso": self.input_peso.get(),
            "flexibilidade": self.input_flexibilidade.get(),
            "abdominal": self.input_abdominal.get(),
            "arremesso_ME": self.input_arremessoME.get(),
            "S_vertical": self.input_Svertical.get(),
            "S_horizontal": self.input_Shorizontal.get(),
        }
        resultado = self.controller.prever_individual(dados_tela)
        self.view.mostrar_resultado(resultado)