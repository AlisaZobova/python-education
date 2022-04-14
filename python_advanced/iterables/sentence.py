"""Task Iterables H/m"""
import re


class MultipleSentencesError(Exception):
    """Class MultipleSentencesError"""


class Sentence:
    """Class sentence"""
    def __init__(self, sentence):
        """Class constructor"""
        try:
            if not isinstance(sentence, str):
                raise TypeError("It is not string!")
            sentence_template = r"([A-Z]\w*){1}(\s\w+)*[.|...|!|?]"
            sentence_count = len(re.findall(sentence_template, sentence))
            if sentence_count < 1:
                raise ValueError("This is an unfinished sentence!")
            if sentence_count > 1:
                raise MultipleSentencesError()
            self._sentence = sentence
            self.word_count = len(re.findall('[A-z]+', sentence))
            self.chars_count = len(re.findall('[^A-z]', sentence))
            self.words = self._words()
            self.other_chars = (i for i in re.findall('[^A-z]', self._sentence))
        except MultipleSentencesError:
            print("Too many sentences!")
        except (TypeError, ValueError) as exception:
            print(f"Incorrect sentence!\n{exception}")

    def __repr__(self):
        """Overridden method __repr__"""
        return f"<Sentence(words={self.word_count}, other_chars={self.chars_count})>"

    def _words(self):
        """Method returning a lazy iterator"""
        words = (i for i in re.findall('[A-z]+', self._sentence))
        return words

    def __iter__(self):
        """Overridden method __iter__"""
        return SentenceIterator(self.word_count, self._sentence)

    def __getitem__(self, i):
        """Overridden method __getitem__"""
        if not isinstance(i, int):
            return f"'{' '.join(list(self._words())[i])}'"
        return f"'{list(self._words())[i]}'"


class SentenceIterator:
    """Class SentenceIterator"""
    def __init__(self, word_count, sentence):
        """Class constructor"""
        self._word_count = word_count
        self._sentence = sentence

    def _get_word(self):
        """Method returning the next word"""
        if self._word_count > 0:
            self._word_count -= 1
            next_word = re.match('[A-z]+', self._sentence).group()
            self._sentence = self._sentence[len(next_word)+1:]
            return next_word
        raise StopIteration

    def __next__(self):
        """Returns the next word"""
        return self._get_word()

    def __iter__(self):
        """Returns an iterator"""
        return self


SENTENCE = Sentence("Good day...Good life!")
SENTENCE1 = Sentence("Good day")
SENTENCE2 = Sentence(1)
SENTENCE3 = Sentence("Good day 5.")
print(repr(SENTENCE3))
#  Знаю, что пайлинт ругается за использование защищеннных методов вне класса,
#  это сделано исключительно для демонстрации
print(SENTENCE3._words())
print(next(SENTENCE3._words()))
for n in SENTENCE3._words():
    print(n)
print(SENTENCE3.words)
print(SENTENCE3.other_chars)
print(SENTENCE3[0])
print(SENTENCE3[:])
for word in SENTENCE3:
    print(word)
SENT_ITER = iter(SENTENCE3)
print(SENT_ITER)
print(next(SENT_ITER))
print(next(SENT_ITER))
