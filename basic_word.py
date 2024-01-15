class BasicWord:
    def __init__(self, word: str, subwords: list):
        """
        Инициализирует экземпляр класса с заданным словом и подсловами.
        :param word: (str) Базовое слово.
        :param subwords: (list) Список подслов.
        """
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        """
        Возвращает строковое представление объекта BasicWord.
        :return: (str) Строковое представление объекта.
        """
        return f'BasicWord({self.word}, {self.subwords})'

    def get_word(self):
        """
        Возвращает базовое слово.
        :return    str: Базовое слово.
        """
        return self.word

    def check_word(self, word):
        """
        Проверяет, есть ли заданное слово в списке подслов.
        :param word: (str) Слово для проверки.
        :return    bool: True, если слово есть в списке подслов, иначе False.
        """
        return word in self.subwords

    def count_subwords(self):
        """
        Возвращает количество подслов в списке подслов.
        :return    int: Количество подслов.
        """
        return len(self.subwords)