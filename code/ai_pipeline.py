import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ELM e ESN
from hpelm import ELM
from easyesn import ESN

class AIModelPipeline:
    def __init__(self, X, y):
        self.X_original = X
        self.y = y
        self.X = X.copy()
        self.models = {}
        self.results = {}
        
    def normalize(self):
        self.scaler = MinMaxScaler()
        self.X = self.scaler.fit_transform(self.X)
        print("✔ Dados normalizados")
        
    def apply_pca(self, n_components=2):
        self.pca = PCA(n_components=n_components)
        self.X = self.pca.fit_transform(self.X)
        print(f"✔ PCA aplicado ({n_components} componentes)")
        
    def feature_importance(self):
        rf = RandomForestClassifier()
        rf.fit(self.X, self.y)
        importances = rf.feature_importances_
        print("✔ Importância das features calculada")
        return importances
    
    def feature_extraction(self, k=5):
        self.selector = SelectKBest(score_func=f_classif, k=k)
        self.X = self.selector.fit_transform(self.X, self.y)
        print(f"✔ {k} melhores features selecionadas")
    
    def train_mlp(self):
        model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
        self._train_model(model, "MLP")
    
    def train_dt(self):
        model = DecisionTreeClassifier()
        self._train_model(model, "DecisionTree")
    
    def train_rf(self):
        model = RandomForestClassifier()
        self._train_model(model, "RandomForest")
    
    def train_elm(self, hidden_neurons=100):
        elm = ELM(self.X.shape[1], 1)
        elm.add_neurons(hidden_neurons, "sigm")
        elm.train(self.X, self.y.reshape(-1, 1))
        y_pred = np.round(elm.predict(self.X)).flatten()
        acc = accuracy_score(self.y, y_pred)
        self.models["ELM"] = elm
        self.results["ELM"] = acc
        print(f"✔ ELM treinado - Acurácia: {acc:.4f}")
    
    def train_esn(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2)
        esn = ESN(n_input=X_train.shape[1], n_output=1, n_reservoir=50, sparsity=0.2, random_state=42)
        esn.fit(X_train, y_train)
        y_pred = esn.predict(X_test).flatten()
        y_pred = np.round(y_pred)
        acc = accuracy_score(y_test, y_pred)
        self.models["ESN"] = esn
        self.results["ESN"] = acc
        print(f"✔ ESN treinado - Acurácia: {acc:.4f}")
    
    def train_ram(self):
        # Simulação simples de RAM Neural: Decision Tree com profundidade baixa
        model = DecisionTreeClassifier(max_depth=3)
        self._train_model(model, "RAMNeural")
    
    def _train_model(self, model, name):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        self.models[name] = model
        self.results[name] = acc
        print(f"✔ {name} treinado - Acurácia: {acc:.4f}")
    
    def summary(self):
        print("\n==== RESULTADOS FINAIS ====")
        for name, acc in self.results.items():
            print(f"{name}: Acurácia = {acc:.4f}")
