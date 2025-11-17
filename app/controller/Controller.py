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