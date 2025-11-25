import joblib
import pandas as pd
from pathlib import Path

from app.model.chain.padronizar_dados.CarregarArquivoHandler import CarregarArquivoHandler
from app.model.chain.padronizar_dados.SelecionarColunasHandler import SelecionarColunasHandler
from app.model.chain.padronizar_dados.PadronizarDadosHandler import PadronizarDadosHandler
from app.model.chain.treinamento_knn.TreinarKNNHandler import TreinarKNNHandler

class Model:
    def __init__(self):
        self.chain_treinamento = self.montar_corrente(TreinarKNNHandler())

        self.alunos_turma = []

        self.modelo_knn = None
        self.features_knn = None
        self.caminho_modelo_knn = None
        self.pasta_turmas = Path("turmas")

    def montar_corrente(self, ultimo_handler):
        self.carregar_dados = CarregarArquivoHandler()
        self.limpar_arquivo = PadronizarDadosHandler()
        self.selecionar_colunas = SelecionarColunasHandler()
        
        self.carregar_dados.set_next(self.limpar_arquivo)
        self.limpar_arquivo.set_next(self.selecionar_colunas)
        self.selecionar_colunas.set_next(ultimo_handler)
        
        return self.carregar_dados

    def carregar_arquivo(self, caminho_dataset):
        caminho = Path(caminho_dataset)
        return self.chain_treinamento.handle(caminho)
    
    def carregar_modelo_treinado(self, caminho_modelo):
        caminho = Path(caminho_modelo)

        payload = joblib.load(caminho)
        self.modelo_knn = payload["modelo"]
        self.features_knn = payload["features"]
        self.caminho_modelo_knn = caminho

        print(f"Modelo KNN carregado de: {caminho}")

    def carregar_turma(self, caminho_turma):
        caminho = Path(caminho_turma)
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        df = pd.read_csv(caminho)

        return df.to_dict(orient="records")

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
        if self.modelo_knn is None or self.features_knn is None:
            model_path = Path("knn_model.pkl")
            payload = joblib.load(model_path)
            self.modelo_knn = payload["modelo"]
            self.features_knn = payload["features"]
            self.caminho_modelo_knn = model_path
            print("Modelo padrão knn_model.pkl carregado automaticamente")
    
        modelo = self.modelo_knn
        features = self.features_knn

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
    
    def registrar_aluno_turma(self, dados_individuais: dict, resultado: dict):
        registro = {
            "nome": dados_individuais.get("nome", ""),
            "idade": dados_individuais.get("idade", ""),
            "posicao_prevista": resultado.get("posicao_prevista", ""),
        }

        valores = resultado.get("valores", {})
        registro.update(valores)

        self.alunos_turma.append(registro)

    def salvar_planilha_turma(self, caminho: Path | None = None):
        if caminho is None:
            pasta = Path("turmas")
            pasta.mkdir(parents=True, exist_ok=True)
            caminho = pasta / "turma_atual.csv"

        df = pd.DataFrame(self.alunos_turma)
        df.to_csv(caminho, index=False)

    def listar_turmas_disponiveis(self):
        if not self.pasta_turmas.exists():
            return []
        return list(self.pasta_turmas.glob("*.csv"))
    
    def obter_pasta_turmas(self) -> Path:
        self.pasta_turmas.mkdir(parents=True, exist_ok=True)
        return self.pasta_turmas

    def encerrar_e_visualizar_turma(self, nome_planilha: str | None = None):
        caminho = None

        if nome_planilha:
            nome_arquivo = nome_planilha.strip()

            if not nome_arquivo.lower().endswith(".csv"):
                nome_arquivo += ".csv"

            pasta = Path("turmas")
            pasta.mkdir(parents=True, exist_ok=True)

            caminho = pasta / nome_arquivo

        self.salvar_planilha_turma(caminho)

        return self.alunos_turma