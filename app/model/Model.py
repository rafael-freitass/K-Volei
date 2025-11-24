from app.model.chain.padronizar_dados.CarregarArquivoHandler import CarregarArquivoHandler
from app.model.chain.padronizar_dados.SelecionarColunasHandler import SelecionarColunasHandler
from app.model.chain.padronizar_dados.PadronizarDadosHandler import PadronizarDadosHandler
from app.model.chain.treinamento_knn.TreinarKNNHandler import TreinarKNNHandler
from app.model.chain.resultado_knn.ResultadoKnnHandler import ResultadoKnnHandler

import joblib
import pandas as pd
from pathlib import Path

class Model:
    def __init__(self):
        self.chain_treinamento = self.montar_corrente(TreinarKNNHandler())
        self.chain_resultado = self.montar_corrente(ResultadoKnnHandler())

    def montar_corrente(self, ultimo_handler):
        self.carregar_dados = CarregarArquivoHandler()
        self.limpar_arquivo = PadronizarDadosHandler()
        self.selecionar_colunas = SelecionarColunasHandler()
        
        self.carregar_dados.set_next(self.limpar_arquivo)
        self.limpar_arquivo.set_next(self.selecionar_colunas)
        self.selecionar_colunas.set_next(ultimo_handler)
        
        return self.carregar_dados

    def carregar_arquivo(self, caminho_dataset, modo="treino"):
        print('Passou pelo model')

        if modo == "treino":
            return self.chain_treinamento.handle(caminho_dataset)
        elif modo == "resultado":
            return self.chain_resultado.handle(caminho_dataset)
        else:
            raise ValueError(f"Modo inválido: {modo}")

    def converter_para_float(self, valor, default=0.0):
        if isinstance(valor, (int, float)):
            return float(valor)

        if isinstance(valor, str):
            valor = valor.strip().replace(",", ".")
            if valor == "":
                return default
            try:
                return float(valor)
            except ValueError:
                return default

        return default

    def prever_individual(self, dados_individuais: dict):
        model_path = Path("knn_model.pkl")

        payload = joblib.load(model_path)
        modelo = payload["modelo"]
        features = payload["features"]

        linha = {}
        for feat in features:
            valor_bruto = dados_individuais.get(feat, 0.0)
            linha[feat] = self.converter_para_float(valor_bruto, default=0.0)

        df = pd.DataFrame([linha])

        pred = modelo.predict(df)[0]

        proba = None
        classes = None
        if hasattr(modelo, "predict_proba"):
            proba = modelo.predict_proba(df)[0]
            classes = modelo.classes_.tolist()

        return {
            "posicao_prevista": pred,
            "features_usadas": features,
            "valores": linha,
            "proba": proba,
            "classes": classes,
        }
    
    def salvar_e_ir_para_proximo_aluno():
        pass

    def encerrar_e_visualizar_turma():
        pass