

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
