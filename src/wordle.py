import random

from src.utils import print_error, print_success, print_warning


class GenerateWordFrequency:
    def __init__(self, file_path: str, word_len: int, limit: int):
        self.file_path = file_path
        self.word_len = word_len
        self.limit = limit

    def __call__(self):
        # Build data
        words_freq = []
        with open(self.file_path) as f:
            for line in f:
                word, frequency = line.split(', ')
                frequency = int(frequency)
                words_freq.append((word, frequency))

        # word_len letters words
        filtered_words = list(filter(lambda w_freq: len(w_freq[0]) == self.word_len, words_freq))

        # Sort Data
        words_freq = sorted(filtered_words, key=lambda w_freq: w_freq[1], reverse=True)

        # Limit Data
        words_freq = words_freq[:self.limit]

        # Drop Frequency Data
        words = [w_freq[0] for w_freq in words_freq]

        return words


class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000):
        generate_word_frequency = GenerateWordFrequency(file_path, word_len, limit)
        self.words = generate_word_frequency()
        self.word_len = word_len

    def check_word(self, word, guess_word):
        for w_letter, g_letter in zip(word, guess_word):
            if w_letter == g_letter:
                print_success(f' {g_letter} ', end=' ')

            elif g_letter in word:
                print_warning(f' {g_letter} ', end=' ')

            else:
                print_error(f' {g_letter} ', end=' ')
        print()

    def __call__(self):
        # Random Word
        word = random.choice(self.words)
        word = word.upper()

        # Start Game
        num_try = 6
        while num_try:
            guess_word = input(f'Enter a {self.word_len} letter word (or Q to exit): ')
            if guess_word.lower() == 'q':
                break
            guess_word = guess_word.upper()

            # Word length
            if len(guess_word) != 5:
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}!')
                continue

            # Check valid word
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid!')
                continue

            # Check valid, invalid positions, invalid characters
            self.check_word(word, guess_word)

            if word == guess_word:
                print()
                print_success(' Congratulations! ')
                break

            num_try -= 1

        else:
            print_warning(f'Game over: The word was "{word}".')
