from sklearn.metrics import accuracy_score

class Avaliador:

    def __init__(self):
        pass

    def avaliar_modelo(self, modelo, X_teste, Y_teste):
        '''Retorna avaliação de acurácia do modelo informado, dado o conjuto de dados

        Arguments:
        modelo: modelo de predição
        X_teste: conjunto de dados de variáveis explicativas
        Y_teste: conjunto de dados da variável explicada a ser comparada'''
        predicao = modelo.predict(X_teste)

        return accuracy_score(Y_teste, predicao)