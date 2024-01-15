import random
import requests

from basic_word import BasicWord


def load_random_word() -> BasicWord:
    """
    Загружает случайное слово с внешнего ресурса и создает экземпляр класса BasicWord.
    :return: BasicWord
    """
    random_word = get_random_word()
    basic_word = BasicWord(random_word['word'], random_word['subwords'])
    print(repr(basic_word))

    return basic_word


def load_words() -> list:
    """
    Загружает список слов с внешнего ресурса.
    :return: (list) Список слов в формате JSON.
    """
    url = 'https://www.jsonkeeper.com/b/LFWA'
    response = requests.get(url)

    return response.json()


def get_random_word() -> object:
    """
    Возвращает случайное слово из списка.
    :return: (object) Случайный объект из списка.
    """
    words = load_words()
    random_word = random.choice(words)

    return random_word
