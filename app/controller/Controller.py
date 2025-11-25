from app.model.Model import Model

class Controller():
    def __init__(self):
        self.model = Model()

    def abrir_arquivo_treino(self, caminho):
        if not caminho:
            print("Caminho inválido")
            return
        
        self.model.carregar_arquivo(caminho)
        print("Passou pelo Controller")

    def prever_individual(self, dados_individuais: dict):
        resultado = self.model.prever_individual(dados_individuais)
        
        resultado["nome"] = dados_individuais.get("nome", "")
        resultado["idade"] = dados_individuais.get("idade", "")
        
        print("Passou pelo Controller (previsão individual)")
        return resultado
    
    def registrar_aluno_turma(self, dados_individuais: dict, resultado: dict):
        self.model.registrar_aluno_turma(dados_individuais, resultado)

    def encerrar_e_visualizar_turma(self, nome_planilha: str | None = None):
        return self.model.encerrar_e_visualizar_turma(nome_planilha)
