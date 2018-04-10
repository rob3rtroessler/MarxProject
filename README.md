# MarxProject

Still trying to figure out a good way to set everything up.

Download vagrant from vagrantup.com so we can run everything in a virtual machine.

I made a Vagrantfile that has some configuration for python3.6. If you do use Vagrant, everything should be setup. Otherwise, you'll need to create a virtual environment for the project and install all the requirements into it.

Current setup inside my virtual environment:	

```
Package      Version
------------ -------
click		6.7
Flask		0.12.2
itsdangerous	0.24
Jinja2		2.10
MarkupSafe	1.0
nltk		3.2.5
pyenchant	2.0.0
six		1.11.0
Werkzeug	0.14.1

```

To activate the venv:
`$ source ./venv/bin/activate`

To run the server:
```
$ export FLASK_APP=server.py
$ flask run

```