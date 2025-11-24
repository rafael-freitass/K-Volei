from app.model.chain.base.BaseHandler import BaseHandler
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
import joblib
from pathlib import Path

class TreinarKNNHandler(BaseHandler):
    def __init__(
        self,
        target_col: str = "posicao",
        model_path: str = "knn_model.pkl",
        test_size: float = 0.2,
        random_state: int = 42,
        n_neighbors: int = 5,
    ):
        super().__init__()
        self.target_col = target_col
        self.model_path = model_path
        self.test_size = test_size
        self.random_state = random_state
        self.n_neighbors = n_neighbors

    def handle(self, data: pd.DataFrame):
        print("Passou pelo TreinarKNNHandler")

        df = data.copy()

        if self.target_col not in df.columns:
            raise ValueError(
                f"Coluna alvo '{self.target_col}' não encontrada. "
                f"Colunas disponíveis: {list(df.columns)}"
            )

        y = df[self.target_col]
        X = df.drop(columns=[self.target_col])

        X = X.select_dtypes(include=["number"])
        if X.empty:
            raise ValueError("Nenhuma coluna numérica encontrada para treinar o KNN.")

        print(f"Features usadas no treino: {list(X.columns)}")

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y if len(y.unique()) > 1 else None,
        )

        pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("knn", KNeighborsClassifier(n_neighbors=self.n_neighbors)),
            ]
        )

        pipeline.fit(X_train, y_train)

        accuracy = pipeline.score(X_test, y_test)
        print(f"Acurácia no conjunto de teste: {accuracy:.4f}")

        payload = {
            "modelo": pipeline,
            "features": list(X.columns),
            "target_col": self.target_col,
        }
        joblib.dump(payload, self.model_path)
        print(f"Modelo KNN salvo em '{self.model_path}'")

        resultado = {
            "model_path": self.model_path,
            "accuracy": accuracy,
            "features": list(X.columns),
            "target_col": self.target_col,
        }

        return self.next(resultado)