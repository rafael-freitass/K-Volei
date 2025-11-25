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
    
    def carregar_modelo_treinado(self, caminho):
        if not caminho:
            print("Caminho inválido para modelo treinado")
            return
        
        self.model.carregar_modelo_treinado(caminho)

    def carregar_turma(self, caminho_turma):
        if not caminho_turma:
            print("Caminho inválido para turma")
            return []
        return self.model.carregar_turma(caminho_turma)
    
    def listar_turmas_disponiveis(self):
        return self.model.listar_turmas_disponiveis()
    
    def obter_pasta_turmas(self):
        return self.model.obter_pasta_turmas()

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
