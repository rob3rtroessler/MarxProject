import os
from shutil import copyfile
from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, flash, current_app, send_from_directory)
from python import MarxCsv

app = Flask(__name__)

# By default: copy the contents of *words.cvs into words.csv
# Maybe do this differently with callbacks/ajax?
copyfile('./data/*words.csv', './data/words.csv')

# TODO index here the actual words in the /data folder
# perhaps don't need to index, can just check if it exists on the go
# current strategy: just generate a csv and place it in data/words.csv


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # have js check if it's a good word anyways
        word = request.form['input_word']
        print(word)

        if os.path.isfile('./data/' + word + '.csv'):
            print('file exists')
        else:
            MarxCsv.do_marx('./corpus/marx_kapital01_1867.txt',
                            word, out_directory='./data/')

        # TODO: instead of reloading page, send a callback
        #   saying to load the file!
        # this might just be a javascript thing though (ajax?)
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('js', path)


@app.route("/data/<path:path>")
def send_data(path):
    return send_from_directory('data', path)


if __name__ == '__main__':
    app.run()
