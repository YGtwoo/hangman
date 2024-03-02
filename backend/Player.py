from Game import Game
from GameStatus import GameStatus

points = 0

while True:
    print("Hello my friend, let's play in hangman. You must try to guess word letter by letter. "
          "If you will win - we will let you go free, but if you will loose...We will hang you")
    game = Game()
    word = game.generate_words()
    letters_count = len(word)
    print(f'You have word of {letters_count} letters, good luck')

    while game.game_status == GameStatus.GAME_CONTINUE:
        letter = input('Choose one letter\n')
        try_letter = game.try_open_letter(letter)
        print(game.word_by_str(try_letter))
        print(f'{game.remaining_tries} attempts left')
        print(f'Your selected letters:{game.try_letters}')
    if game.game_status == GameStatus.LOOSE:
        print(f'You dont have any more attempts...Wright word was {word}. HANG HIM!!!')
        print(f'Your points: {points}')
        points = 0
        print('Do you want try again?')
        decision_if_loose = (str(input()))
        if decision_if_loose == 'y':
            continue
        elif decision_if_loose == 'n':
            break
    if game.game_status == GameStatus.WON:
        print(f'Gongratulations, you are wright!!! The word was {word}. Let him go free')
        points += 100
        print(f'Your points: {points}')
        continue




