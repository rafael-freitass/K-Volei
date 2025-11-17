from app.model.chain.base.BaseHandler import BaseHandler
import pandas as pd

class SelecionarColunasHandler(BaseHandler):
    def __init__(self):
        super().__init__()

        self.colunas_relevantes = [
            "peso",
            "estatura",
            "alturatc",
            "altura_tc",
            "flexibilidade",
            "abdominal",
            "arremessomb",
            "arremesso_mb",
            "arremessome",
            "arremesso_me",
            "s_horizontal",
            "s_vertical",
        ]

    def handle(self, data: pd.DataFrame):
        print('Passou pelo selecionar colunas')

        df = data.copy()

        colunas_existentes = [
            c for c in self.colunas_relevantes if c in df.columns
        ]

        if not colunas_existentes:
            raise ValueError(
                f"Nenhuma das colunas relevantes foi encontrada no dataset. "
                f"Esperado: {self.colunas_relevantes} - "
                f"Encontrado: {list(df.columns)}"
            )

        df_filtrado = df[colunas_existentes].copy()

        df_filtrado.to_csv("dados_filtrados.csv", index=False, float_format="%.2f")
        print("Arquivo salvo em 'dados_filtrados.csv'")

        return self.next(df_filtrado)