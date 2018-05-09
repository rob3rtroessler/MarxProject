# halflife4.py
# single word, checking for relevance
# Character 0x0C is a page break, also called a form feed

import sys
import math
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt


def get_halflife4(corpus, word_to_find):

    # universalize the idea of the word
    stemmer = nltk.stem.snowball.GermanStemmer()
    stemmed_word = stemmer.stem(word_to_find).lower()

    with open(corpus, 'rU', encoding='utf8') as file:
        raw_corpus = file.read()

    # remove end hyphenations
    raw_corpus = raw_corpus.replace('-\n', '')
    raw_corpus = raw_corpus.replace('\n', ' ')

    tokenizer = RegexpTokenizer(r'\w+')

    words = tokenizer.tokenize(raw_corpus)

    growth_ticks = 0
    t0_grow = 0
    t0_decay = 0
    c_grow = 1
    c_decay = 0
    y = velocity = 0.
    lam = 0.5
    entries = []
    graphx = []
    graphy = []
    counter = 0
    prev_hit_x = -1
    vel = 0.
    y_old = 0.
    c = 150.
    changeset = set()
    num_words = len(words)
    for x in range(num_words):

        # hit
        if stemmed_word == stemmer.stem(words[x]).lower():
            counter += 1

            if prev_hit_x == -1:
                y = 1.
            else:
                dist = x - prev_hit_x
                y_old = y
                delta = c/dist - dist/c
                if delta > 0:
                    delta *= 0.2
                new = y_old + delta
                changeset.add(int(delta))

                y = new
                if y > 100:
                    y = 100

                if y < 0:
                    y = 0

            prev_hit_x = x
        # everything else

        else:
            
        booly = True
        if booly:
            graphx.append(x)
            graphy.append(y)

    # print(entries)
    # print(counter)
    # print(graph)
    print(changeset)

    do_output = False
    if do_output:
        with open('./data/hl/' + word_to_find + '4.csv', 'w') as csv:
            csv.write('x,y')
            for x, y in graph:
                csv.write('\n')
                out = "{},{}".format(x, y)
                csv.write(out)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(graphx, graphy)
    plt.show()


if __name__ == '__main__':

    word = input('word: ')
    corpus = input('corpus: ')
    if corpus == 'd':
        corpus = '../corpus/DasKapitalCleaner.txt'
    get_halflife4(corpus, word)




