import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
 
def do_marx(corpus, word_to_find, out_directory='./data/'):
    # german stopwords
    stop_words = set(stopwords.words('german'))
    stop_words.add('dass')

    do_write_out = True

    # redirect all printed text to temp.txt
    if do_write_out:
        sys.stdout = open('temp.txt', 'w')
        # OutputFile = open('output.csv', 'w', encoding='utf8')

        # 'marx_kapital01_1867.txt'
    Kapital = open(corpus, 'rU', encoding="utf8")
    raw = Kapital.read()
    Kapital.close()

    # fixes words divided by hyphens at the end of the line
    raw = raw.replace('-\n', '')
    raw = raw.replace('\n', ' ')
    # remove punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    split = raw.split(" ")

    # tokenize raw text
    tokens = tokenizer.tokenize(raw)

    # get rid of stopwords
    no_stop = []

    for w in tokens:
        if w not in stop_words:
            no_stop.append(w.lower())


    # create NLTK text from the tokens in order to perform all the linguistic processing that NLTK allows us to do
    text = nltk.Text(no_stop)

    # word_to_find = 'entfremden'
    stemmer = nltk.stem.snowball.GermanStemmer()
    stemmed_word = stemmer.stem(word_to_find).lower()
    # print('entfremden:  ' + stemmed_word)
    # print("Entfremdung: " + stemmer.stem('Entfremdung'))
    # print("entfremdeten:" + stemmer.stem(stemmer.stem('entfremdeten')))
    # print("entfremdete: " + stemmer.stem('entfremdete'))
    # print("entfremdet: " + stemmer.stem('entfremdet'))

    # stem all occurrences of a specific word
    word_count = len(text)
    stemmeds = 0
    new_text = []
    for x in range(word_count):
        word = text[x]
        s = stemmer.stem(word.lower())
        if s == stemmed_word:
            new_text.append(s)
            stemmeds += 1
        else:
            new_text.append(word)

    new_text = nltk.Text(new_text)

    # this is written inside of temp.txt
    tmp = text.concordance(stemmed_word, width=100, lines=stemmeds)
    
    # reset stdout
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    

    # now read in the concordance
    concordance_file = open('temp.txt', 'r')
    raw_concordance = concordance_file.read()
    # TODO: remove first line of the file.
    #       if this is done, then you need to remove the line
    #       'words = words[2:]' because that essentially does the same thing
    #       because the first two 'words' are the numbers from the condordance
    #       after the enchant spellcheck remove the english words
    concordance_file.close()

    conc_tokens = nltk.word_tokenize(raw_concordance, language='german')

    no_stop = []
    for w in conc_tokens:
        if w not in stop_words:
            no_stop.append(w.lower())

    import enchant
    d = enchant.Dict('de_DE')

    words = []
    for w in no_stop:
        if d.check(w) and len(w) > 1:
            # is in dictionary
            words.append(w)
    words = words[2:]

    # print(words)

    tokens = nltk.Text(words)



    # for token in tokens:
    #     print(token)

    # calculate length of text (in words)
    # WordCount = len(tokens)
    # print("Words:", WordCount)

    # calculate frequency distribution
    fdist = nltk.FreqDist(tokens)
    mc10 = fdist.most_common(10)
    # print("Most frequent words:", mc10)
    # print("Arbeiter:", fdist['arbeiter'])
    # print("Frequency of 'Arbeiter':", fdist.freq('arbeiter'))

    # TODO don't make the file if the concordance is empty/bad
    # you shouldn't have to worry if it exists already, since the js takes care of that
    with open(out_directory + word_to_find + '.csv', 'w') as csv:
        csv.write('word,frequency')
        for w in mc10:
            csv.write('\n')
            out = "{},{}".format(w[0], w[1])
            csv.write(out)
    csv.closed


    # fdist.plot()

    # dispersion plot
    # text.dispersion_plot(["Markt", "Geld", "Kapital", "Arbeiter", "entfremden"])

    # print(raw)

if __name__ == '__main__':

    word = input('what word: ')
    do_marx(word)
