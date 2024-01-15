class Player:
    def __init__(self, name: str, using_words: list):
        """
        Инициализирует экземпляр класса с заданным именем и списком использованных слов.
        :param name: str
        :param using_words: list
        """
        self.name = name
        self.using_words = using_words

    def __repr__(self):
        """
        Возвращает строковое представление объекта Player.
        :return: str
        """
        return f'Player({self.name}, {self.using_words})'

    def hello(self):
        """
        Поздороваться с пользователем.
        :return: none
        """
        print(f'Привет, {self.name}!')

    def get_count_words(self) -> int:
        """
        Возвращает количество использованных слов.
        :return: int
        """
        return len(self.using_words)

    def add_word(self, word: str) -> None:
        """
        Добавляет слово в список использованных.
        :param word: str
        :return: none
        """
        self.using_words.append(word)

    def check_word(self, word: str) -> bool:
        """
        Проверяет, есть ли заданное слово в списке использованных.
        :param word: str
        :return: bool
        """
        return word in self.using_words
