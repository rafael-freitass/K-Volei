from app.model.chain.base.BaseHandler import BaseHandler

class PrepararDadosHandler(BaseHandler):
    def handle(self, dados):
        return self.set_next(dados)