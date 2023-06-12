import pytest
import time

from src.repository.DatabaseRepository import DatabaseRepository
from src.repository.SearchEngineRepository import SearchEngineRepository
from src.service.DatabaseService import DatabaseService
from src.service.SearchEngineService import SearchEngineService


@pytest.fixture
def make_search_engine():
    def make():
        database_repository = DatabaseRepository()
        search_engine_repository = SearchEngineRepository()
        database_service = DatabaseService(
            database_repository
        )
        search_engine_service = SearchEngineService(
            search_engine_repository,
            database_service
        )
        search_engine = search_engine_service.find()
        return search_engine

    return make


@pytest.mark.parametrize(
    "words, expected",
    [
        (["walt disney"], 53)
    ],
)
def test_contains_all(make_search_engine, words, expected):
    search_engine = make_search_engine()
    result = search_engine.contains_all(words)
    assert len(result) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["walt disney"], 0.001)
    ],
)
def test_time_execution_just_engine(make_search_engine, words, expected):
    search_engine = make_search_engine()
    start_time = time.time()
    search_engine.contains_all(words)
    end_time = time.time()
    time_execution = end_time - start_time
    assert time_execution < expected

