# obosolete: job is done by MarxWordEnvironment.py
# environment.py
# word environment: checking what's in the concordance of a word over time

import sys
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt


def get_word_environment(corpus, word_to_find):

    # universalize the idea of the word
    stemmer = nltk.stem.snowball.GermanStemmer()
    stemmed_word = stemmer.stem(word_to_find).lower()

    with open(corpus, 'rU', encoding='utf8') as file:
        raw_corpus = file.read()

    # remove end hyphenations, tokenize
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
