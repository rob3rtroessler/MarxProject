# halflife.py
# single word, checking for relevance
# Character 0x0C is a page break, also called a form feed

import sys
import math
import nltk
from nltk.tokenize import RegexpTokenizer


def get_halflife(corpus, word_to_find):

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
    growth_ticks = 0
    t0_grow = 0
    t0_decay = 0
    c_grow = 1
    c_decay = 0
    y = velocity = 0
    lam = 0.5
    entries = []
    graph = []
    counter = 0
    for x in range(num_words):
        if word_to_find == words[x].lower():
            # hit
            growth_ticks = 5
            t0_grow = x
            c_grow = y
            t0_decay = x
            c_decay = x
            entries.append(x)
            counter += 1
        # everything else
        if growth_ticks > 0:
            # do some growth stuff
            y = 1 + c_grow * math.exp(1 * lam * (x - t0_grow))
            c_decay = y
            t0_decay = x
            growth_ticks -= 1
        else:
            # not growing: either fast for or half life decay

            # half life
            y = c_decay * math.exp(-1 / lam * (x - t0_decay))
            c_grow = y
            t0_grow = x

        if y > 1.5:
            graph.append((x, y))

    print(entries)
    print(counter)
    print(graph)

    '''
    with open(out_directory + word_to_find + '.csv', 'w') as csv:
        csv.write('word,frequency')
        for w in mc10:
            csv.write('\n')
            out = "{},{}".format(w[0], w[1])
            csv.write(out)
    '''
    with open('./data/hl/' + word_to_find + '1.csv', 'w') as csv:
        csv.write('x,y')
        for x, y in graph:
            csv.write('\n')
            out = "{},{}".format(x, y)
            csv.write(out)


if __name__ == '__main__':

    word = input('word: ')
    corpus = input('corpus: ')
    get_halflife(corpus, word)




