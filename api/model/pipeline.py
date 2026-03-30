from pickle import load

class Pipeline:

    def __init__(self):
        self.pipeline = None

    def carrega_pipeline(self, path):

        with open(path, 'rb') as file:
            self.pipeline = load(file)
            file.close()
        return self.pipeline