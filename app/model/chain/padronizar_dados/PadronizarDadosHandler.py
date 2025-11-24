from app.model.chain.base.BaseHandler import BaseHandler
import pandas as pd
import re
import unicodedata

class PadronizarDadosHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def para_snake_case(self, text: str) -> str:
        text = unicodedata.normalize("NFKD", str(text))
        text = "".join(ch for ch in text if not unicodedata.combining(ch))
        text = re.sub(r"[^0-9a-zA-Z]+", "_", text)
        text = re.sub(r"_+", "_", text).strip("_")
        return text.lower()

    def padronizar_titulo_colunas(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.columns = [self.para_snake_case(col) for col in df.columns]
        return df

    def padronizar_textos(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in df.select_dtypes(include=["object", "string"]):
            df[col] = (
                df[col]
                .astype("string")
                .str.strip()
                .str.lower()
            )
        return df

    def padronizar_numeros(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        cols_numericas = df.select_dtypes(include=["number"]).columns

        for col in cols_numericas:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(float).round(2)

        return df
    
    def tratar_dados_vazios(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df = df.replace(r"^\s*$", pd.NA, regex=True)

        col_num = df.select_dtypes(include=["number"]).columns
        for col in col_num:
            if df[col].isna().any():
                mediana = df[col].median()
                df[col] = df[col].fillna(mediana)

        col_cat = df.select_dtypes(include=["object", "string"]).columns
        for col in col_cat:
            if df[col].isna().any():
                moda = df[col].mode(dropna=True)
                if not moda.empty:
                    df[col] = df[col].fillna(moda.iloc[0])

        return df


    def handle(self, data: pd.DataFrame):
        print("Passou pelo padronizar dados")

        df = data.copy()

        df = self.padronizar_titulo_colunas(df)
        df = self.padronizar_textos(df)
        df = self.padronizar_numeros(df)
        df = self.tratar_dados_vazios(df)

        return self.next(df)