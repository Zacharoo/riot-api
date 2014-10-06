

all:

test: clear
	python -m unittest discover -v -s ./spec/
	
clean:

clear:
	clear

run:
	python main.py
