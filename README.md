# MarxProject

Still trying to figure out a good way to set everything up.

Download vagrant from vagrantup.com get a linux box.
Get something better than Ubuntu 12.04 so you can easily install python3's pip.

Make a vagrant install at the root of the project folder.

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-pip python3
$ python3 -m pip install --user virtualenv

```

Create a python virtual environment and set it to run Python 3.

Current setup inside my virtual environment:

```
Package      Version
------------ -------
click        6.7    
Flask        0.12.2 
itsdangerous 0.24   
Jinja2       2.10   
MarkupSafe   1.0    
nltk         3.2.5  
pip          9.0.3  
setuptools   28.8.0 
six          1.11.0 
Werkzeug     0.14.1

```

To activate the venv:
`$ source ./venv/bin/activate`

To run the server:
```
$ export FLASK_APP=server.py
$ flask run

```