from app.model.chain.base.BaseHandler import BaseHandler

class LimparDadosHandler(BaseHandler):
    def handle(self, data):
        return self.set_next(data)