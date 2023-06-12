import os
import pickle
from os.path import dirname, realpath


class SearchEngineRepository(object):
    def __init__(self):
        self.DIRECTORY = str(dirname(dirname((realpath(__file__))))) + '/data/search_engine'
        self.FILE = 'search_engine.bin'

    def save(self, search_engine: object) -> None:
        if not os.path.exists(self.DIRECTORY):
            os.makedirs(self.DIRECTORY)

        with open(self.DIRECTORY + "/" + self.FILE, 'wb') as file:
            pickle.dump(search_engine, file)

    def find(self) -> None:
        try:
            with open(self.DIRECTORY + "/" + self.FILE, 'rb') as file:
                search_engine = pickle.load(file)
                return search_engine
        except:
            return None
