import pandas as pd
from pathlib import Path
from app.model.chain.base.BaseHandler import BaseHandler

class CarregarArquivoHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def ler_dataset(self, caminho_dataset):
        caminho = Path(caminho_dataset) 
        sufixo = caminho.suffix.lower()
        
        if sufixo == ".csv":
            data = pd.read_csv(caminho, sep=";", decimal=",")
        elif sufixo in [".xlsx", ".xls"]:
            data = pd.read_excel(caminho, decimal=",")
        else:
            raise ValueError(f"Extensão não suportada: {sufixo}")
        
        return data

    def handle(self, caminho_dataset):
        print("Leu o dataset")
        df = self.ler_dataset(caminho_dataset)
        return self.next(df)