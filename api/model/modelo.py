import pickle

class Modelo:

    def __init__(self):
        self.modelo = None

    def carrega_modelo(self, path):
        '''Carrega modelo armazenado em arquivo .pkl em path

        Arguments:
        path: caminho do arquivo .pkl'''

        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.modelo = pickle.load(file)
                file.close()
        else:
            raise Exception('Formato de arquivo não esperado.')
        return self.modelo
    
    def preditor(self, X):
        '''Faz a predição do item X informado, com o modelo carregado

        Arguments:
        X: atributos do item X a ser estimado'''
        if self.modelo is None:
            raise Exception('Necessário carregar o modelo antes de fazer a previsão.')
        previsao = self.modelo.predict(X)
        return previsao