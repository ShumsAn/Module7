from string import punctuation
class WordsFinder:
    def __init__(self,*file_names):
        self.list_file_names = []
        for name in file_names:
            self.list_file_names.append(name)

    def __str__(self):
        return str(self.list_file_names)

    def get_all_words(self):
        """get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле."""
        all_words = {}
        for name in self.list_file_names:
            word_in_file = []
            with open(name, encoding= 'utf-8') as file:
                for line in file:
                    del_signs = line.translate(str.maketrans('', '', punctuation))
                    line_low = del_signs.lower()
                    for word in line_low.split():
                        word_in_file.append(word)
                        all_words[name] = word_in_file

        return all_words

    def find(self, word):
        '''Метод, где word - искомое слово. Возвращает словарь,
         где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.'''
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                index_w = words.index(word.lower())
                find_dict[name] = index_w+1

        return find_dict

    def count(self, word):
        """ Метод, где word - искомое слово. Возвращает словарь,
         где ключ - название файла, значение - количество слова word в списке слов этого файла."""
        count_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_w = words.count(word.lower())
                count_dict[name] = count_w
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

