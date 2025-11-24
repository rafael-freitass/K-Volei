from app.model.Model import Model

class Controller():
    def __init__(self):
        self.model = Model()

    def abrir_arquivo_treino(self, caminho):
        if not caminho:
            print("Caminho inválido")
            return
        
        self.model.carregar_arquivo(caminho, modo="treino")
        print("Passou pelo Controller")

    def prever_individual(self, dados_individuais: dict):
        resultado = self.model.prever_individual(dados_individuais)
        
        resultado["nome"] = dados_individuais.get("nome", "")
        resultado["idade"] = dados_individuais.get("idade", "")
        
        print("Passou pelo Controller (previsão individual)")
        return resultado