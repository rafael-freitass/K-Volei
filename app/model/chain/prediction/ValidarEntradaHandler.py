from app.model.chain.base.BaseHandler import BaseHandler

class ValidarEntradaHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, dados_aluno):
        return self.set_next(dados_aluno)