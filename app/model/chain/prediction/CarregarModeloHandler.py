from app.model.chain.base.BaseHandler import BaseHandler

class CarregarModeloHandler(BaseHandler):
    def handle(self, dados):
        return self.set_next(dados)