from app.model.Model import Model

class Controller():
    def __init__(self, view):
        self.view = view
        self.model = Model()

    def abrir_arquivo(self):
        caminho = self.view.selecionar_arquivo()
        if caminho:
            dados = self.model.carregar_arquivo(caminho)
            print("Arquivo lido com sucesso!")
            self.view.show_frame("Inserir")