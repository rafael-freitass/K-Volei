from app.model.chain.base.BaseHandler import BaseHandler

class CarregarArquivoHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, caminho_dataset):
        return self.set_next(caminho_dataset)