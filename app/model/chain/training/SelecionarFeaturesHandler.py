from app.model.chain.base.BaseHandler import BaseHandler

class SelecionarFeaturesHandler(BaseHandler):
    def handle(self, data):
        return self.set_next(data)