from app.model.chain.base.BaseHandler import BaseHandler

class ResultadoKnnHandler(BaseHandler):
    def handle(self, contexto):
        print('Passou pelo selecionar Resultado Knn')
        return