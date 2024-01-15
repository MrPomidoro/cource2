from players import Player
from utils import load_random_word


def game():
    print(f'Привет, это игра "Слова из слова"!')
    name = input('Как вас зовут? ')
    player = Player(name, [])
    player.hello()
    basic_word = load_random_word()
    print(f'Составьте {basic_word.count_subwords()} слов из слова {basic_word.get_word()}')
    print(f'Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')
    while True:
        if player.get_count_words() == basic_word.count_subwords():
            print(f'Вы угадали всe {basic_word.count_subwords()} слов, это невероятно!')
            break
        user_word = input()
        if user_word == 'stop' or user_word == 'стоп':
            print(f'Игра завершена, вы угадали {player.get_count_words()} слов из {basic_word.count_subwords()}')
            break
        if len(user_word) < 3:
            print('Слишком короткое слово')
            continue
        if user_word in player.using_words:
            print('Такое слово уже было')
            continue
        if basic_word.check_word(user_word):
            player.add_word(user_word)
            print('Верно!')
        else:
            print('Неверно')

    if player.get_count_words() != basic_word.count_subwords():
        print(f'Вы угадали {player.get_count_words()} слов из {basic_word.count_subwords()}')


if __name__ == '__main__':
    game()

