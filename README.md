# MarxProject

## Setup


Current setup inside my virtual environment, found in `venv`:


| Package      | Version |
|:------------ |:------- |
| click        |  6.7    |
| Flask        |  0.12.2 |
| itsdangerous |  0.24   |
| Jinja2       |  2.10   |
| MarkupSafe   |  1.0    |
| nltk         |  3.2.5  |
| pyenchant    |  2.0.0  |
| six          |  1.11.0 |
| Werkzeug     |  0.14.1 |

## Running

By default, the website runs on http://localhost:5000.

### PyCharm
If running from PyCharm, then everything should be setup in the `venv`
subdirectory. The interpreter should be set to the python3.6 install
inside of that folder.


### Command Line on Unix

If running from command line:

Navigate to this project's directory.

To activate the venv:
`$ source ./venv/bin/activate`

To run the server:
```
$ export FLASK_APP=server.py
$ flask run

```
