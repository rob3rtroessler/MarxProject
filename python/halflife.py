# halflife3.py
# single word, checking for concept relevance over time

import sys
import math
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt


def get_halflife3(corpus, word_to_find):

    # stem the word, to universalize the idea of it
    stemmer = nltk.stem.snowball.GermanStemmer()
    stemmed_word = stemmer.stem(word_to_find).lower()

    with open(corpus, 'rU', encoding='utf8') as file:
        raw_corpus = file.read()

    # remove end hyphenations
    raw_corpus = raw_corpus.replace('-\n', '')
    raw_corpus = raw_corpus.replace('\n', ' ')

    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(raw_corpus)

    graphx, graphy, csv_lines = [], [], []
    hit_counter = prev_hit_x = 0
    y = vel = 0.
    decay_constant = 160.
    num_words = len(words)
    for x in range(num_words):

        # how long have we gone without seeing this word?
        dist = x - prev_hit_x

        # hit: process 'activation':
        is_hit = stemmed_word == stemmer.stem(words[x]).lower()
        if is_hit:
            hit_counter += 1
            vel = 0
            y += 20
            prev_hit_x = x

        # process 'decay':
        # smooth out the 'landing'
        if y + 50*vel < 0:
            vel *= 0.5

        y += vel

        # new velocity: subtract by dist/c
        vel -= dist/decay_constant * 3

        # don't let it go below the 'ground'
        if y <= 0:
            y = 0
            if vel < 0:
                vel = 0

        # after processing, save data only for hits
        if is_hit:
            graphx.append(x)
            graphy.append(y)
            # we're only taking 5 words on either side for the quote
            quote = words[x-5:x+5]
            csv_lines.append([x, int(y), quote])

    do_output = True
    if do_output:
        with open('./data/half_life/' + word_to_find + '.csv', 'w') as csv:
            csv.write('x,y,quote')
            for x, y, quote in csv_lines:
                csv.write('\n')

                # build sentence from the tokens
                quote_string = quote[0]
                for word in quote[1:]:
                    quote_string += ' ' + word

                out = "{},{},{}".format(x, y, quote_string)
                csv.write(out)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(graphx, graphy)
    plt.show()


if __name__ == '__main__':

    word = input('word: ')
    corpus = input('corpus: ')
    if corpus == 'd':
        corpus = './corpus/DasKapitalCleaner.txt'
    get_halflife3(corpus, word)
