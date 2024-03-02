import random
from typing import Iterable
from backend.GameStatus import GameStatus
from Setting import Config


class InvalidOperationError(Exception):
    pass


class Game:

    def __init__(self, tries: int = 6):
        self.__tries = tries
        self.__miss_counter = 0
        self.__try_letters = []
        self.__opened_letters = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ""

    def generate_words(self) -> str:
        dir = Config()
        tx = dir.get_setting("settings.ini", "Settings", "directory")
        with open(tx, encoding='utf8') as file:
            lines = file.readlines()
            random_word = random.choice(lines)
            self.__word = random_word.rstrip().lower()
            self.__opened_letters = [False for _ in self.__word]
            self.__game_status = GameStatus.GAME_CONTINUE
            return self.__word

    def try_open_letter(self, letter: str) -> Iterable[str]:

        if self.miss_counter == self.tries:
            raise InvalidOperationError(f"You choose {self.tries} tries. Your tries is over")

        if self.game_status != GameStatus.GAME_CONTINUE:
            raise InvalidOperationError(f'Game is {self.game_status}. Please, start new game by generate word')

        open_any_letter = False
        result = []

        for i, c in enumerate(self.word):

            if c == letter:
                self.__opened_letters[i] = True
                open_any_letter = True

            if self.__opened_letters[i]:
                result.append(c)
            else:
                result.append(' _ ')

        if not open_any_letter:
            self.__miss_counter += 1

        self.__try_letters.append(letter)

        if self.__winner():
            self.__game_status = GameStatus.WON
        elif self.miss_counter == self.tries:
            self.__game_status = GameStatus.LOOSE

        return result

    def __winner(self):
        for letter in self.__opened_letters:
            if not letter:
                return False
        return True

    def word_by_str(self, try_letter):
        return ''.join(try_letter)

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def tries(self) -> int:
        return self.__tries

    @property
    def miss_counter(self) -> int:
        return self.__miss_counter

    @property
    def try_letters(self) -> Iterable[str]:
        return sorted(self.__try_letters)

    @property
    def remaining_tries(self) -> int:
        return self.tries - self.miss_counter
