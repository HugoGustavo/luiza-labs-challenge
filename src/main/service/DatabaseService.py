class DatabaseService(object):
    def __init__(self, database_repository):
        self.__database_repository = database_repository

    def list(self) -> list:
        result = self.__database_repository.list()
        return result

    def find_by_file_name(self, file_name: str) -> list:
        result = self.__database_repository.find_by_file_name(
            file_name
        )
        return result

    def find_all(self) -> list:
        result = self.__database_repository.find_all()
        return result
