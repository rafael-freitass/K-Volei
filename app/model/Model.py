from app.model.chain.padronizar_dados.CarregarArquivoHandler import CarregarArquivoHandler
from app.model.chain.padronizar_dados.SelecionarColunasHandler import SelecionarColunasHandler
from app.model.chain.padronizar_dados.PadronizarDadosHandler import PadronizarDadosHandler

from app.model.chain.treinamento_knn.TreinarKNNHandler import TreinarKNNHandler
from app.model.chain.resultado_knn.ResultadoKnnHandler import ResultadoKnnHandler

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