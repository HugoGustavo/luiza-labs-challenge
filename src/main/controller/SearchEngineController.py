from repository.DatabaseRepository import DatabaseRepository
from repository.SearchEngineRepository import SearchEngineRepository
from service.DatabaseService import DatabaseService
from service.SearchEngineService import SearchEngineService
from view.SearchEngineView import SearchEngineView


class SearchEngineController(object):
    def __init__(self):
        self.__database_repository = DatabaseRepository()
        self.__search_engine_repository = SearchEngineRepository()

        self.__database_service = DatabaseService(
            self.__database_repository
        )
        self.__search_engine_service = SearchEngineService(
            self.__search_engine_repository,
            self.__database_service
        )
        self.__search_engine_view = SearchEngineView()

    def execute(self, words: list):
        search_engine = self.__search_engine_service.find()
        search = search_engine.contains_all(words)
        self.__search_engine_view.view(words, search)
