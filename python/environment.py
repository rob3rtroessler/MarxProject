# environment.py
# word environment is just 
# Character 0x0C is a page break, also called a form feed

import sys
import nltk
from nltk.tokenize import RegexpTokenizer


def get_word_environment(corpus, word_to_find):

    # for case-insensitivity
    word_to_find = word_to_find.lower()

    with open(corpus, 'rU', encoding='utf8') as file:
        raw_corpus = file.read()

    # remove end hyphenations
    raw_corpus = raw_corpus.replace('-\n', '')
    raw_corpus = raw_corpus.replace('\n', ' ')

    tokenizer = RegexpTokenizer(r'\w+')

    words = tokenizer.tokenize(raw_corpus)
    num_words = len(words)
    counter = 0
    entries = []
    for x in range(num_words):
        if word_to_find == words[x].lower():
            # hit
            entries.append(x)
            counter += 1

    print(entries)
    print(counter)
