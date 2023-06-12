class SearchEngineView(object):
    def __init__(self):
        pass # Execute pass

    def view(self, words: list, search: set):
        words = ' '.join(words)
        occurences = len(search)

        if occurences == 0:
            result = "Não foi encontrado nenhuma ocorrencia pelo termo \"{0}\"".format(
                words
            )
        elif occurences == 1:
            result = "Foi encontrada apenas 1 ocorrência pelo termo \"{0}\"\n".format(
                words
            )
            result = result + "O arquivo que possui \"{0}\" é:".format(
                words
            )
        else:
            result = "Foram encontradas {0} ocorrência pelo termo \"{1}\"\n".format(
                occurences,
                words
            )
            result = result + "Os arquivos que possuem \"{0}\" são:".format(
                words
            )
        print(result)

        for item in sorted(list(search)):
            print('data/'+item)
