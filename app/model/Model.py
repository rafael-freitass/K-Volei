from app.model.chain.training.CarregarArquivoHandler import CarregarArquivoHandler
from app.model.chain.prediction.ValidarEntradaHandler import ValidarEntradaHandler

class Model:
    def __init__(self):
        self.train_entry = CarregarArquivoHandler()
        self.predict_entry = ValidarEntradaHandler()

    def carregar_arquivo(self, caminho_dataset):
        return self.train_entry.handle(caminho_dataset)

    def gerar_resultado(self, dados_aluno):
        return self.predict_entry.handle(dados_aluno)