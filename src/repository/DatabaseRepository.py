import os
import sys
from os.path import dirname, realpath


class DatabaseRepository(object):
    DIRECTORY = str(dirname(dirname((realpath(__file__))))) + '/data/'

    def __init__(self):
        pass

    def list(self):
        result = [item for item in os.walk(self.DIRECTORY)]
        result = result[0][-1]
        return result

    def find_by_file_name(self, file_name):
        file_name = str(self.DIRECTORY) + "/" + str(file_name)
        if 'win' in sys.platform:
            file_name = file_name.replace('/', '\\')
        file = open(file_name, "r")
        file_line = file.readline()
        return file_line

    def find_all(self):
        result = [
            (file_name, self.find_by_file_name(file_name))
            for file_name in self.list()
        ]
        return result
