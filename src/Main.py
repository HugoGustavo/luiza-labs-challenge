import sys
from os.path import dirname, realpath
DIRECTORY = str(dirname(dirname((realpath(__file__)))))
sys.path.insert(0, DIRECTORY)

from src.controller.SearchEngineController import SearchEngineController


def main(words: list = []):
    words = words or sys.argv[1:]
    search_engine_controller = SearchEngineController()
    search_engine_controller.execute(words)


if __name__ == '__main__':
    main()
