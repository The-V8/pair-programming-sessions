all: run test lint init

init:
	pip install -r requirements.txt

lint: init
	flake8

test: lint
	pytest

run: test
	python run.py