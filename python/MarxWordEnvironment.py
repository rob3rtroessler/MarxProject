# MarxWordEnvironment.py
# Generate word environment csv files.

import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
import enchant

do_write_out = True


def marx_do_word_environment(corpus, word_to_find,
                             out_directory='./data/word_environment/'):
    # german stopwords
    stop_words = set(stopwords.words('german'))
    stop_words.update(['dass', 'sein', 'sei', 'war', 'den', 'ein', 'wurde',
                       'wurden', 'auf', 'trotzdem', 'ausser', 'daher', 'dah'])

    # redirect all printed text to temp.txt
    # this is because concordance prints to stdout, and we want it
    if do_write_out:
        sys.stdout = open('temp.txt', 'w')

    with open(corpus, 'rU', encoding="utf8") as Kapital:
        raw = Kapital.read()

    # fixes words divided by hyphens at the end of the line
    raw = raw.replace('-\n', '')
    raw = raw.replace('\n', ' ')

    # remove punctuation, tokenize text
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(raw)

    # get rid of stopwords
    without_stops = []
    for w in tokens:
        if w not in stop_words:
            without_stops.append(w.lower())

    # create NLTK text from the tokens in order to perform all the linguistic
    # processing that NLTK allows us to do
    text = nltk.Text(without_stops)

    stemmer = nltk.stem.snowball.GermanStemmer()
    stemmed_target = stemmer.stem(word_to_find).lower()

    # stem all occurrences of our specific word
    word_count = len(text)
    stemmeds = 0
    new_text = []
    for x in range(word_count):
        word = text[x].lower()
        s = stemmer.stem(word)
        if s == stemmed_target:
            new_text.append(s)
            stemmeds += 1
        else:
            new_text.append(word)

    new_text = nltk.Text(new_text)

    # this gets written inside of temp.txt
    tmp = text.concordance(stemmed_target, width=400, lines=stemmeds)

    # reset stdout back to normal
    sys.stdout.close()
    sys.stdout = sys.__stdout__

    german_dict = enchant.Dict('de_DE')

    # now read in the concordance
    with open('temp.txt', 'r') as concordance_file:
        raw_concordance_lines = concordance_file.readlines()
    conc_lines = [line.strip() for line in raw_concordance_lines]
    # remove first line of the file. it's a metadata line
    conc_lines = conc_lines[1:]

    # loop1: clean up, make a word inventory, generate freqdists
    word_inventory = set()
    counter = 0
    mcs = []
    for line in conc_lines:
        conc_tokens = nltk.word_tokenize(line, language='german')

        without_stops = []
        for word in conc_tokens:
            if word not in stop_words and not word.isdigit():
                without_stops.append(word)

        words = []
        for word in without_stops:
            # is in dictionary?
            if german_dict.check(word) and len(word) > 1:
                stemmed = stemmer.stem(word)
                words.append(stemmed)

        # calculate frequency distribution
        tokens = nltk.Text(words)
        fdist = nltk.FreqDist(tokens)
        mc = fdist.most_common(200)
        mcs.append(mc)

        # build word inventory
        for word, hits in mc:
            word_inventory.add(word)
        counter += 1

    word_scores = dict()
    word_scorelist = dict()
    for word in word_inventory:
        word_scores[word] = 0

    conc_counter = 0
    for mc in mcs:
        conc_counter += 1
        for word in word_inventory:
            word_scores[word] *= 0.5
            if word_scores[word] < 0.05:
                word_scores[word] = 0

        for word, hits in mc:
            word_scores[word] = (word_scores[word] + 1) * hits

        for word in word_inventory:
            if word not in word_scorelist:
                word_scorelist[word] = []
            word_scorelist[word].append(word_scores[word])

    word_maxes = []
    for word in word_inventory:
        max_score = 0
        for num in word_scorelist[word]:
            max_score = max(max_score, num)
        word_maxes.append([word, max_score])
    sorted_maxes = sorted(word_maxes, key=lambda l: l[1], reverse=True)

    for x in range(20):
        word = sorted_maxes[x][0]
        print(word, word_scorelist[word], '\n')

    if do_write_out:
        with open(out_directory + word_to_find + '.csv', 'w') as csv:
            first_line = 'hit'
            for x in range(20):
                word = sorted_maxes[x][0]
                first_line += ',' + word
            csv.write(first_line)

            # TODO: loop over num of concordances
            csv_lines = []
            for x in range(conc_counter):
                this_line = str(x+1)
                for y in range(20):
                    word = sorted_maxes[y][0]
                    this_line += ',' + str(int(3*word_scorelist[word][x]))
                csv_lines.append(this_line)
                print(this_line)
                csv.write('\n' + this_line)


if __name__ == '__main__':

    word = input('what word: ')
    corpus = input('what corpus: ')
    if corpus == 'd':
        corpus = './corpus/DasKapitalCleaner.txt'
    print('doing ({}) ({})'.format(word, corpus))
    marx_do_word_environment(corpus, word)
