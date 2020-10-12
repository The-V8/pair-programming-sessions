all: test lint init

init:
	pip install -r requirements.txt

lint: init
	flake8

test: lint
	pytest