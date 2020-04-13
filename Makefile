setup:
	python3 -m venv ~/.login-api-test

install:
	source ~/.login-api-test/bin/activate &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

start-api:
	source ~/.login-api-test/bin/activate &&\
		python web.py

all: setup install start-api