from sklearn.metrics import accuracy_score

class Avaliador:

    def __init__(self):
        pass

    def avaliar_modelo(self, modelo, X_teste, Y_teste):
        predicao = modelo.predict(X_teste)

        return accuracy_score(Y_teste, predicao)