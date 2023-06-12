import itertools


class SearchEngine(object):
    def __init__(self):
        self.__index = dict()

    def add(self, words: str, file_name: str) -> None:
        for word in words.split(' '):
            self.__index[word] = self.__index.get(word, set())
            self.__index[word].add(file_name)

    def contains(self, word: str) -> set:
        result = self.__index.get(word, set())
        return result

    def contains_all(self, words: list) -> set:
        if words is None or len(words) == 0:
            return set()

        words = [item.split(' ') for item in words]
        words = list(itertools.chain(*words))

        result = self.contains(words[0])
        only_one = len(words) == 1
        if only_one:
            return result

        partial = [self.contains(word) for word in words[1:]]
        result = result.intersection(*partial)
        return result
