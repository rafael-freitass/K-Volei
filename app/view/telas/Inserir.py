from tkinter import ttk

class Inserir(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=24)
        self.controller = controller
        self.columnconfigure(0, weight=1)

        self.titulo()
        self.identificacao()
        self.medidas()
        self.flexibilidade()
        self.abdominais()
        self.medball()
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
        self.input_altura_em_pe = ttk.Entry(caixa)
        self.input_altura_em_pe.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Altura sentado (cm)").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=6)
        self.input_altura_sentado = ttk.Entry(caixa)
        self.input_altura_sentado.grid(row=0, column=3, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Massa (kg)").grid(row=0, column=4, sticky="w", padx=(8, 4), pady=6)
        self.input_massa = ttk.Entry(caixa)
        self.input_massa.grid(row=0, column=5, sticky="ew", padx=(0, 8), pady=6)

    def flexibilidade(self):
        caixa = ttk.LabelFrame(self, text="Flexibilidade")
        caixa.grid(row=3, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Sentar e alcançar (cm)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_flex = ttk.Entry(caixa)
        self.input_flex.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def abdominais(self):
        caixa = ttk.LabelFrame(self, text="Resistência abdominal")
        caixa.grid(row=4, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Máximo em 1 min (reps)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_abdominais = ttk.Entry(caixa)
        self.input_abdominais.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def medball(self):
        caixa = ttk.LabelFrame(self, text="Arremesso Medicine Ball 2kg")
        caixa.grid(row=5, column=0, sticky="ew", pady=(0, 12))
        caixa.columnconfigure(1, weight=1)

        ttk.Label(caixa, text="Distância (m)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_medball = ttk.Entry(caixa)
        self.input_medball.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

    def saltos(self):
        caixa = ttk.LabelFrame(self, text="Saltos")
        caixa.grid(row=6, column=0, sticky="ew", pady=(0, 12))
        for i in range(4):
            caixa.columnconfigure(i, weight=1)

        ttk.Label(caixa, text="Salto vertical (cm)").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=6)
        self.input_salto_vetical = ttk.Entry(caixa)
        self.input_salto_vetical.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=6)

        ttk.Label(caixa, text="Salto horizontal (cm)").grid(row=0, column=2, sticky="w", padx=(8, 4), pady=6)
        self.input_salto_horizontal = ttk.Entry(caixa)
        self.input_salto_horizontal.grid(row=0, column=3, sticky="ew", padx=(0, 8), pady=6)

    def footer(self):
        btns = ttk.Frame(self)
        btns.grid(row=8, column=0, sticky="ew")
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=0)

        self.btn_salvar = ttk.Button(btns, text="Salvar dados")
        self.btn_salvar.grid(row=0, column=0, sticky="w")

        self.btn_voltar = ttk.Button(btns, text="Voltar")
        self.btn_voltar.grid(row=0, column=1, sticky="e")