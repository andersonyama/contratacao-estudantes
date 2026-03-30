import pickle

class Modelo:

    def __init__(self):
        self.modelo = None

    def carrega_modelo(self, path):

        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.modelo = pickle.load(file)
                file.close()
        else:
            raise Exception('Formato de arquivo não esperado.')
        return self.modelo
    
    def preditor(self, X):
        if self.modelo is None:
            raise Exception('Necessário carregar o modelo antes de fazer a previsão.')
        previsao = self.modelo.predict(X)
        return previsao