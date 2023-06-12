from src.model.SearchEngine import SearchEngine


class SearchEngineService(object):
    def __init__(self, search_engine_repository, database_service):
        self.__search_engine_repository = search_engine_repository
        self.__database_service = database_service

    def create(self):
        file_and_content = self.__database_service.find_all()
        search_engine = SearchEngine()
        for (file, content) in file_and_content:
            search_engine.add(content, file)
        return search_engine

    def save(self, search_engine: object) -> None:
        self.__search_engine_repository.save(search_engine)

    def find(self) -> object:
        search_engine = self.__search_engine_repository.find()
        if search_engine is None:
            search_engine = self.create()
            self.__search_engine_repository.save(search_engine)
        return search_engine
